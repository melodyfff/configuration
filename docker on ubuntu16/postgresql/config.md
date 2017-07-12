# docker 上运行 postgresql

## 首先确保 已经有postgres镜像
sudo docker run --name pg_test -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=postgres -d -p 8090:5432 postgres:9.6

### 或者
sudo docker run -d --name pgtest -p 8090:5432 -e "POSTGRES_USER=test" -e "POSTGRES_DB=postgres" postgres:9.5

## 访问postgres
psql -h localhost -p 8090 -d postgres -U postgres --password
> `localhost`为虚拟机IP地址,`docker`的IP地址为内部通讯使用

## 查看容器内数据文件、配置文件、网络授权文件设置
sudo docker exec -it 3bf3b533ba05 /bin/bash

## 挂载容器内部数据
sudo docker run --name ps_test -d -v /opt/data:/var/lib/postgresql/data -p 8090:5432 -e POSTGRES_USER=test -e POSTGRES_DB=sonar 0f3af79d8673

