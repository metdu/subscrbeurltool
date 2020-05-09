#!/bin/bash
#首先删掉文件,替换文件,然后运行命令
#运行指令 sh ./restart.sh
# AUTHOR  demo

#删除容器
docker rm -f $(docker ps -a | grep func_app | awk '{print $1}')
#删除镜像
docker rmi func_app
#打包镜像
docker build . -t func_app
#启动容器
docker run -d -p 8085:8888  --name func_app func_app