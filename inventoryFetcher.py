import pymongo
import sys
import subprocess

## grab group id arg from CLI
group_id = int(sys.argv[1])

## methods to parse host data
class hostStrings:

    def __init__(self, host):
        self.user = host["hostInfo"]["user"]
        self.ip  = host["hostInfo"]["host"]
        self.password = host["hostInfo"]["password"]
        self.host_vars = " ansible_ssh_user="+self.user + "ansible_ssh_password=" + self.password 

def parseGroupToInventoryAndRunPlaybook(group):
    hostGroup = "[hosts] \n"
    for host in group:
        strings = hostStrings(host)
        with open("inventories/" +strings.ip + ".ini", "w") as vars:
            vars.write(hostGroup+strings.ip+strings.host_vars)
            subprocess.run(['ansible-playbook', '-i', "inventories/" +strings.ip + ".ini", 'playbook.yml'], cwd='/ansible')

    
    
#using connection string to access db
client = pymongo.MongoClient('mongodb+srv://h64shah:titanic2@sprint-cluster.lneibho.mongodb.net/')
db = client['inventory']
collection = db['hosts']

#query for group using group_id
group = list(collection.find({"group_id" : group_id }))

#create string of hosts and write to inventory file and run playbook
parseGroupToInventoryAndRunPlaybook(group)



