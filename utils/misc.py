''' misc '''
import time


def info_with_time(info: str):
    ''' info with time '''
    return f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: {info}'
