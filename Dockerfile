# Current build sprintapp:1.0
FROM python:3.9-slim

# Install Ansible and other dependencies
RUN apt-get update && apt-get install -y \
    openssh-client \
    rsync \
    sshpass \
 && rm -rf /var/lib/apt/lists/* 

RUN pip install ansible \
    pymongo \
    flask\
    bson

# Copy your Ansible playbook and inventory file to the container
COPY . /ansible

# Set the working directory
WORKDIR /ansible
# Specify group_id arg 

#CMD ["ansible-playbook", "-i", "inventory.ini", "playbook.yml"]
CMD ["python", "app.py"]