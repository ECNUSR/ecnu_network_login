import argparse
import logging
import time
from getpass import getpass

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
    parser.add_argument('-ip',
                        '--ip',
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
    parser.add_argument('-i',
                        '--interval',
                        type=int,
                        default=60,
                        help='检查网络是否正常的间隔，仅在LOOP模式有效')
    parser.add_argument('-v',
                        '--verbose',
                        type=str.upper,
                        default='INFO',
                        choices=['DEBUG', 'INFO', 'ERROR'],
                        help='检查网络是否正常的间隔，仅在LOOP模式有效')
    args = parser.parse_args()
    args.ip = args.ip or get_host_ip()
    args.password = getpass('password: ')
    return args


def _login(username: str, password: str) -> str:
    try:
        code = send_encu_login_post(username, password)
        return code, ('登录失败~', '登陆成功！')[code]
    except Exception as e:
        return False, str(e)


def login():
    # 用户参数
    args = parse_options()

    # logger
    logger = logging.getLogger('ecnu_network_login')
    logger.setLevel({
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'ERROR': logging.ERROR,
    }[args.verbose])
    format_str = '%(asctime)s %(levelname)s: %(message)s'
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(format_str))
    logger.addHandler(stream_handler)
    logger.propagate = False

    if args.mode == 'PRINT':
        url = get_encu_login_post(args.username, args.password, args.ip)
        logger.fatal(f'远程服务器的登录url为: {url}')
    elif args.mode == 'ONCE':
        code, info = _login(args.username, args.password)
        logger.info(info) if code else logger.error(info)
    else:
        while True:
            if not is_network_ok():
                code, info = _login(args.username, args.password)
                logger.info(info) if code else logger.error(
                    f'{info}\n等待{args.interval}s后重试')
            else:
                logger.debug('网络在线~~无需重新登录~~')
            time.sleep(args.interval)
