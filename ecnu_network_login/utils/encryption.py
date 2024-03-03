import hashlib
import hmac
import json

import js2py
import requests


def get_token(username: str, ip: str, timestamp: int) -> str:
    content = json.loads(
        requests.get(
            f'https://login.ecnu.edu.cn/cgi-bin/get_challenge?callback=x&username={username}&ip={ip}&_={timestamp}'  # noqa
        ).content[2:-1])
    return content['challenge']


def hmac_md5(password: str, token: str) -> str:
    mac = hmac.new(token.encode(), password.encode(), hashlib.md5)
    mac.digest()
    return mac.hexdigest()


def get_info(username: str, password: str, ip: str, token: str) -> str:
    with open(__file__[:-3] + '.js', 'r', encoding='utf8') as f:
        context = js2py.EvalJs()
        context.execute(f.read())

    result = context.encode(
        "{\"username\":\"" + username + "\",\"password\":\"" + password +
        "\",\"ip\":\"" + ip + "\",\"acid\":\"1\",\"enc_ver\":\"srun_bx1\"}",
        token)
    result = '{SRBX1}' + context.base64(result)
    return result


def get_chksum(token: str, username: str, password_hmd5: str, ip: str,
               info: str) -> str:
    all = (token + username + token + password_hmd5 + token + '1' + token +
           ip + token + '200' + token + '1' + token + info)
    return hashlib.sha1(all.encode()).hexdigest()
