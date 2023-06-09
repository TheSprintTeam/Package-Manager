FROM python:3.9-slim

# Install Ansible and other dependencies
RUN apt-get update && apt-get install -y \
    openssh-client \
    rsync \
 && rm -rf /var/lib/apt/lists/*

RUN pip install ansible

# Copy your Ansible playbook and inventory file to the container
COPY playbook.yml /ansible/playbook.yml
##COPY inventory.ini /ansible/inventory.ini

# Set the working directory
WORKDIR /ansible

# Run the Ansible playbook
CMD ["ansible-playbook", "-i", "localhost", "playbook.yml"]
