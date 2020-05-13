# 访问 localhost:9000 填入zk集群地址： zoo1:2181/kafka1,zoo2:2181/kafka1,zoo3:2181/kafka1
COMPOSE_PROJECT_NAME=kafka_test docker-compose -f docker-compose.yml up -d