# Run the docker file

docker run --rm sprintapp:0.9

## To run the playbook on your localhost
ansible-playbook -i "localhost," playbook.yml

- or you can pass in one node that we want to target

## Downloads
- 4 types of OS, need a different case for each

## Complementary Config files alongside playbook
- Otherwise we can setup an *.ini file (spec sheet) to define hosts groups
- In Ansible, an inventory is a list of target hosts or nodes on which Ansible will execute tasks. The inventory can be defined in various formats, including INI-style, YAML, or dynamically generated using scripts or external sources.

##### Ansible background
- '-' means order