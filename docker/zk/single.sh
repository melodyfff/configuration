docker run --name some-zookeeper -p 2181:2181 --restart always -d zookeeper:3.4.14

# 连接
# docker run -ti --rm --link some-zookeeper:zookeeper zookeeper:3.4.14 zkCli.sh -server zookeeper