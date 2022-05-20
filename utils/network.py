''' ssl utils '''
import requests


def disable_requests_warnings():
    ''' 绕过高版本SSL强制验证 '''
    # pylint: disable=no-member
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        pass


def is_network_ok(url: str = "https://www.baidu.com/"):
    '''' 检查网络是否能够连通 '''
    try:
        status = requests.get(url, timeout=3, verify=False).status_code
        return 200 <= status < 300
    except Exception as e:
        print(e)
        return False


def send_encu_login_post(username: str, password: str):
    ''' 发送校园网登录请求 '''
    requests.post("https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&", data={
        'username': username,
        'password': password,
        'action': 'login',
        'ac_id': '1',
        'is_second': '0'
    }, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False)
