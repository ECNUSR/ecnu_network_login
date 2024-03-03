import argparse
import time
from getpass import getpass

from .utils.misc import info_with_time
from .utils.network import (disable_requests_warnings, get_encu_login_post,
                            get_host_ip, is_network_ok, send_encu_login_post)


def parse_options():
    """parse options."""
    disable_requests_warnings()  # 禁用高版本SSL验证

    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
                        '--username',
                        type=str,
                        required=True,
                        help='username, 也就是学号')
    parser.add_argument('--ip',
                        type=str,
                        default=None,
                        help='ip, 远程服务器ip地址（如果不输入则会使用本机ip）')
    parser.add_argument('-m',
                        '--mode',
                        type=str.upper,
                        choices=[
                            'PRINT',
                            'ONCE',
                            'LOOP',
                        ],
                        default='LOOP',
                        help='模式，默认为LOOP')
    parser.add_argument('--interval',
                        type=int,
                        default=60,
                        help='检查网络是否正常的间隔，仅在LOOP模式有效')
    args = parser.parse_args()
    args.ip = args.ip or get_host_ip()
    args.password = getpass('password: ')
    return args


def _login(username: str, password: str) -> str:
    try:
        code = send_encu_login_post(username, password)
        return ('登录失败~', '登陆成功！')[code]
    except Exception as e:
        return str(e)


def login():
    args = parse_options()
    if args.mode == 'PRINT':
        url = get_encu_login_post(args.username, args.password, args.ip)
        print(url)
    elif args.mode == 'ONCE':
        info = _login(args.username, args.password)
        print(info_with_time(info))
    else:
        while True:
            if not is_network_ok():
                info = _login(args.username, args.password)
                print(info_with_time(info))
            time.sleep(args.interval)
