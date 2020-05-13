# COMPOSE_PROJECT_NAME=zk_test 这个环境变量, 这是为我们的 compose 工程起一个名字, 以免与其他的 compose 混淆
# 查询状态
# COMPOSE_PROJECT_NAME=zk_test docker-compose ps

# 停止集群
# COMPOSE_PROJECT_NAME=zk_test docker-compose stop

# 删除集群
# COMPOSE_PROJECT_NAME=zk_test docker-compose rm
COMPOSE_PROJECT_NAME=zk_test docker-compose -f docker-compose.yml up -d