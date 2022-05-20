# ECNU_NETWORK_LOGIN

华师大上网需要进行校园网验证，验证一般是通过网页操作。然而在学校机房放置的linux服务器，不太方便打开网页进行验证，所以开发一个通过python的自动验证程序。

# Usage

> usage: login.py [-h] --username USERNAME [--interval INTERVAL] [--lark LARK [LARK ...]]
> optional arguments:
>
>  -h, --help            show this help message and exit
>
>  --username USERNAME   username, 也就是学号
>
>  --interval INTERVAL   检查网络是否正常的间隔
>
>  --lark LARK [LARK ...]   如果登录失败，通过飞书发送给接收者（搭配飞书机器人食用）

为了保护你的密码安全，使用getpass库输入密码，密码也就是你idc账号的密码。
