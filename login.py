''' login ecnu network for linux '''
import time
from getpass import getpass
import argparse
from utils.network import disable_requests_warnings, is_network_ok, send_encu_login_post
from utils.misc import info_with_time


def parse_options():
    ''' parse options '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, required=True, help='username, 也就是学号')
    parser.add_argument('--interval', type=int, default=60, help='检查网络是否正常的间隔')
    args = parser.parse_args()
    args.password = getpass("password: ")
    return args


def login(username: str, password: str):
    '''' login '''
    try:
        send_encu_login_post(username, password)
        return True, '登陆成功！'
    except Exception as e:
        return False, str(e)


def main():
    ''' login ecnu network for linux '''
    # 禁用高版本SSL验证
    disable_requests_warnings()

    # 获取用户信息
    args = parse_options()

    # 循环登录
    first = True
    while True:
        if not is_network_ok() or first:
            status, info = login(args.username, args.password)
            print(info_with_time(info))
        first = False
        time.sleep(args.interval)



if __name__ == '__main__':
    main()
