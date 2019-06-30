# mvn archetype:generate 已经废弃改为mvn archetype:generate
```html
mvn archetype:generate -DgroudId=org.test -DartifactId=test -DarchetypeArtifactId=maven-archetype-webapp
```
#以下方案依旧可行
```html
mvn org.apache.maven.plugins:maven-archetype-plugin:2.2:create -DgroupId=org.test -DartifactId=test -DarchetypeArtifactId=maven-archetype-webapp
```