# 运行
```bash
docker-compose up -d --build
```

# 操作
```bash
# 进入容器
docker exec -it kafka /bin/bash

# 创建topic
# 参数 --topic 指定 Topic 名，--partitions 指定分区数，--replication-factor 指定备份数
kafka-topics.sh --create --topic hello --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1
# 增加 Topic 的 partition 数
kafka-topics.sh --zookeeper zookeeper:2181 --alter --topic hello --partitions 5


# 列出所有topic
./kafka-topics.sh --bootstrap-server localhost:9092 --list
# 查看topic
./kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic hello 
# 查看 topic 指定分区 offset 的最大值或最小值
# time 为 -1 时表示最大值，为 -2 时表示最小值：
kafka-run-class.sh kafka.tools.GetOffsetShell --topic hello --time -1 --broker-list 127.0.0.1:9092 --partitions 0 
# 删除 Topic
kafka-topics.sh --zookeeper zookeeper:2181 --topic hello --delete



# 生产消息
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic hello

# 消费消息
# 从头开始消费，--max-messages 1 ，指定取数个数
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic hello --from-beginning --max-messages 1
# 从尾部开始消费，指定分区
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic hello --offset latest --partition 0
# 查看消费者分组列表
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
# 查看消费者分组Group详情
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group console-consumer-96707 --describe
# 删除group
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group console-consumer-96707 --delete

# 平衡 leader
kafka-preferred-replica-election.sh --bootstrap-server localhost:9092

# 自带压测工具
kafka-producer-perf-test.sh --topic hello --num-records 100 --record-size 1 --throughput 100 --producer-props bootstrap.servers=localhost:9092
```