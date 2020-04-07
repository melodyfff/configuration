# 15672是管理界面的端口，5672是服务的端口,设置用户admin:admin
docker run -tid --name rabbitmq \
-e RABBITMQ_DEFAULT_USER=admin \
-e RABBITMQ_DEFAULT_PASS=admin \
-p 15672:15672 -p 5672:5672 \
rabbitmq:3-management