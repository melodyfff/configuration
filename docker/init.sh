# 初始化环境

# redis环境
export REDIS_DATA_PATH=/opt/databases/redis-3.2.8/data
docker run --name redis -d -v $REDIS_DATA_PATH:/data -p 6379:6379 redis:3.2.8

# mysql环境
export MYSQL_PATH=/opt/databases/mysql
docker run -d --name mysql -v $MYSQL_PATH:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 mysql:5.6

# privoxy代理
docker run -d --restart unless-stopped --name privoxy -p 8118:8118 splazit/privoxy-alpine