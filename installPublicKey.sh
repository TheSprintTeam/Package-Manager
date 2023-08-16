cd ~
mkdir ".ssh"
cd ".ssh"
touch id_rsa.pub
touch /authorized_keys
wget -O - https://storage.googleapis.com/artifacts.sprint-391123.appspot.com/Keys/id_rsa.pub > id_rsa.pub
cat id_rsa.pub > /authorized_keys
