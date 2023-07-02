#!/bin/bash/
while getopts g: flag
do
    case "${flag}" in
        g) ip=${OPTARG};;
        
    esac
done

ansible-playbook -i inventories/$ip.ini playbook.yml