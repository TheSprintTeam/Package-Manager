#!/bin/bash/
while getopts g: flag
do
    case "${flag}" in
        g) group_id=${OPTARG};;
        
    esac
done
python inventoryFetcher.py $group_id inventory.ini
ansible-playbook -i inventory.ini playbook.yml
