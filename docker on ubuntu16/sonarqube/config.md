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

#### 当 -v 绑定本地目录时，需要先 -v /opt/bin/run.sh:/opt/sonarqube/bin 运行启动脚本
docker run -d --name sonarqube -p 9000:9000 -v /opt/sonarqube-docker/sonar_bin/:/opt/sonarqube/bin -v /opt/sonarqube-docker/sonar_plugs:/opt/sonarqube/extensions/plugins -v /opt/sonarqube-docker/sonar_conf:/opt/sonarqube/conf 9a23ac22b32b




