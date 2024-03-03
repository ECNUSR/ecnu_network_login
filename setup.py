from setuptools import find_packages, setup

setup(name='ecnu_network_login',
      version='1.1',
      author='ccjiahao',
      author_email='jhchao502@163.com',
      description='ecnu network login',
      python_requires='>=3.7.3',
      include_package_data=True,
      install_requires=['requests==2.31.0', 'urllib3==1.26.18', 'js2py==0.74'],
      entry_points={
          'console_scripts': [
              'ecnu_net_login=ecnu_network_login.login:login',
              'ecnu_network_login=ecnu_network_login.login:login',
          ],
      },
      packages=find_packages())
