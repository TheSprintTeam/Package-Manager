#!/bin/bash/

sshpass -f 'pass' ansible-playbook -i inventory.ini playbook.yml
