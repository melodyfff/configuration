# docker 上运行 sonarqube

## 首先确保 已经有sonarqube镜像

### 官方运行指令
> $ docker run -d --name sonarqube \  
    -p 9000:9000 -p 9092:9092 \  
	-e SONARQUBE_JDBC_USERNAME=sonar \  
	-e SONARQUBE_JDBC_PASSWORD=sonar \  
	-e SONARQUBE_JDBC_URL=jdbc:postgresql://localhost/sonar \  
	sonarqube
    
#### 运行指令实例
docker run -d --name sonarqube -p 9000:9000 -e SONARQUBE_JDBC_USERNAME=xinchen -e SONARQUBE_JDBC_PASSWORD= -e SONARQUBE_JDBC_URL=jdbc:postgresql://192.168.201.128:8089/postgres sonar 



