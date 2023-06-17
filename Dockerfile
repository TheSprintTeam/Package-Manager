# Current build sprintapp:2.0
FROM python:3.9-slim

# Install Ansible and other dependencies
RUN apt-get update && apt-get install -y \
    openssh-client \
    rsync \
    sshpass \
 && rm -rf /var/lib/apt/lists/* 

RUN pip install ansible

# Copy your Ansible playbook and inventory file to the container
COPY . /ansible

# Set the working directory
WORKDIR /ansible

# Run the Ansible playbook
CMD ["ansible-playbook", "-i", "inventory.ini", "playbook.yml", "-e", "technologies_list=['mysql, terraform']"]
# CMD ["ansible-playbook", "-i", "inventory.ini", "playbook.yml"]