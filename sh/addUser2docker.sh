sudo gpasswd -a ${USER} docker
sudo systemctl restart docker
sudo service docker restart