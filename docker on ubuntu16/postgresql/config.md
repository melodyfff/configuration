# docker 上运行 postgresql

## 首先确保 已经有postgres镜像
sudo docker run --name pg_test -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=postgres -d -p 8090:5432 postgres:9.6

## 访问postgres
psql -h localhost -p 8090 -d postgres -U postgres --password