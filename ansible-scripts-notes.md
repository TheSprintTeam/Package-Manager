# Run the docker file

docker run --rm sprintapp:0.9

## To run the playbook on your localhost
ansible-playbook -i "localhost," playbook.yml

- or you can pass in one node that we want to target

## Otherwise we can setup an inventory.ini file later it is like a spec sheet.

In Ansible, an inventory is a list of target hosts or nodes on which Ansible will execute tasks. The inventory can be defined in various formats, including INI-style, YAML, or dynamically generated using scripts or external sources.