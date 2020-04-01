#2020.03.30start studying spider

#使用阿里云作为自己的代理服务器
1、配置安全组的端口7731
2、进入ubuntu,apt install tinyproxy
3、vim /ect/tinyproxy.conf --> 将端口port改成7731 将 #Allow127.0.0.1
4、tail -f /var/log/tinyproxy/tinyproxy.log观察日志
5、在06try_proxies中就可以使用代理