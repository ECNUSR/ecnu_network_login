# ECNU_NETWORK_LOGIN

华师大上网需要进行校园网验证，验证一般是通过网页操作。然而在学校机房放置的linux服务器，不太方便打开网页进行验证，所以开发一个通过python的自动验证程序。

# Preparation

1. Install dependencies:

```
pip install ecnu-network-login==1.1
```

# Usage

```bash
# 帮助文档，ecnu_net_login和ecnu_network_login均能识别
ecnu_net_login --help
ecnu_network_login --help

# 登录（循环登录）
ecnu_net_login -u {{学号}}
ecnu_net_login -u {{学号}} -m LOOP

# 登录（仅一次）
ecnu_net_login -u {{学号}} -m ONCE

# 远程获取登录URL（如果远程服务器没网，没法安装此包，可以在有校园网环境的机器上远程支持获取URL，然后在服务器上wget该URL）
ecnu_net_login -u {{学号}} --ip {{服务器IP}} -m PRINT
```
