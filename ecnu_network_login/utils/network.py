import socket
from typing import Optional

import requests

from .encryption import get_chksum, get_info, get_token, hmac_md5
from .misc import get_timestamp


def get_host_ip() -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def disable_requests_warnings():
    """绕过高版本SSL强制验证."""
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'  # noqa
    except AttributeError:
        pass


def is_network_ok(url: str = 'https://www.baidu.com/'):
    """' 检查网络是否能够连通."""
    try:
        status = requests.get(url, timeout=3, verify=False).status_code
        return 200 <= status < 300
    except Exception as e:
        print(e)
        return False


def get_encu_login_post(username: str,
                        password: str,
                        ip: Optional[str] = None) -> str:
    """发送校园网登录请求."""
    ip = ip or get_host_ip()
    timestamp = get_timestamp()

    token = get_token(username, ip, timestamp)

    password_hmac = hmac_md5(password, token)
    password_last = '{MD5}' + password_hmac

    info = get_info(username, password, ip, token)

    chksum = get_chksum(token, username, password_hmac, ip, info)

    url = f'callback=1&action=login&username={username}&password={password_last}&double_stack=0&chksum={chksum}&info={info}&ac_id=1&ip={ip}&n=200&type=1&_={timestamp}'  # noqa
    url = url.replace('{', '%7B')
    url = url.replace('}', '%7D')
    url = url.replace('+', '%2B')
    url = url.replace('/', '%2F')
    return 'https://login.ecnu.edu.cn/cgi-bin/srun_portal?' + url


def send_encu_login_post(username: str,
                         password: str,
                         ip: Optional[str] = None) -> bool:
    """发送校园网登录请求."""
    url = get_encu_login_post(username, password, ip or get_host_ip())
    requests.get(url)
    return is_network_ok()
