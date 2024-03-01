"""login ecnu network for linux."""
import argparse
from getpass import getpass

from utils.network import disable_requests_warnings, get_encu_login_post


def parse_options():
    """parse options."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--username',
                        type=str,
                        required=True,
                        help='username, 也就是学号')
    parser.add_argument('--ip', type=str, required=True, help='ip, 远程服务器ip地址')
    parser.add_argument('--interval', type=int, default=60, help='检查网络是否正常的间隔')
    args = parser.parse_args()
    args.password = getpass('password: ')
    return args


def main():
    """login ecnu network for linux."""
    # 禁用高版本SSL验证
    disable_requests_warnings()

    # 获取用户信息
    args = parse_options()

    print(get_encu_login_post(args.username, args.password, args.ip))


if __name__ == '__main__':
    main()
