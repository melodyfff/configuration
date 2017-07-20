#!/bin/bash

set -e

if [ "${1:0:1}" != '-' ]; then
  exec "$@"
fi

export TZ=Asia/Shanghai
export SONARQUBE_JDBC_USERNAME=test
export SONARQUBE_JDBC_PASSWORD=
export SONARQUBE_JDBC_URL=jdbc:postgresql://192.168.201.130:8090/sonar

exec java -jar lib/sonar-application-$SONAR_VERSION.jar \
  -Dsonar.jdbc.username="$SONARQUBE_JDBC_USERNAME" \
  -Dsonar.jdbc.password="$SONARQUBE_JDBC_PASSWORD" \
  -Dsonar.jdbc.url="$SONARQUBE_JDBC_URL" \
  -Dsonar.web.port=9000 \
  "$@"