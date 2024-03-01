# ECNU_NETWORK_LOGIN

华师大上网需要进行校园网验证，验证一般是通过网页操作。然而在学校机房放置的linux服务器，不太方便打开网页进行验证，所以开发一个通过python的自动验证程序。

# Preparation

1. Install dependencies:

```
pip install -r requirements.txt
```

# Usage

> usage: login.py [-h] --username USERNAME [--interval INTERVAL] [--lark LARK [LARK ...]]
> optional arguments:
>
> -h, --help            show this help message and exit
>
> --username USERNAME   username, 也就是学号
>
> --interval INTERVAL   检查网络是否正常的间隔

为了保护你的密码安全，使用getpass库输入密码，密码也就是你idc账号的密码。

# 第一次使用

服务器如果完全没有网，无法联网，可以通过在自己机器上（连上校园网）执行

```
python get_login_url.py --username {{学号}} --ip {{服务器ip}}
```

便可以得到登录网址，然后在**几分钟内**服务器上请求该网址就行。
