# Specify group_id arg 
ARG group_id
# Current build sprintapp:1.0
FROM python:3.9-slim

# Install Ansible and other dependencies
RUN apt-get update && apt-get install -y \
    openssh-client \
    rsync \
    sshpass \
 && rm -rf /var/lib/apt/lists/* 

RUN pip install ansible \
    pymongo
# Copy your Ansible playbook and inventory file to the container
COPY . /ansible

# Set the working directory
WORKDIR /ansible


#Use Inventory In DB to create inventory files and run them
CMD ["python", "inventoryFetcher.py", group_id]
