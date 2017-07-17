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
> 该命令将挂载主机的/opt/data目录到容器内的/var/lib/postgresql/data目录上，任何在/opt/data目录的文件都将会出现在容器内。这可以用来实现主机和容器之间的文件共享。当容器中的指定的目录不存在的时候会自动创建，当已存在的时候，该目录下的文件并不会同步到主机上的Volume，然后Volume中的数据则会被复制到容器中。

## 挂载数据卷容器
通常使用数据容器来持久化数据库和数据文件    
docker run --name dbdata postgres:9.5 echo "data only"   
创建了一个名为dbdata的数据容器，运行完echo之后就停止了。数据容器是不需要运行的，只要创建好了就可以了。   
sudo docker run -d --volumes-from dbdata --name pgtest -p 8090:5432 -e "POSTGRES_USER=test" -e "POSTGRES_DB=postgres" postgres:9.5  启动一个数据库服务容器，连接到dbdata数据容器上。



## 备份、恢复或迁移volume
docker run --rm --volumes-from dbdata -v $(pwd):/backup 0f3af79d8673 tar cvf /backup/pg_test.tar.gz /var/lib/postgresql/data

## 查看容器信息
docker inspect f1c87508fe97

## 容器内外互相拷贝数据
docker cp foo.txt mycontainer:/foo.txt   
docker cp mycontainer:/foo.txt foo.txt