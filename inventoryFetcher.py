import pymongo
import sys
import subprocess
import json
from bson.objectid import ObjectId
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
        subprocess.run(['ansible-playbook', '-i', "inventories/" + strings.ip + ".ini", 'playbook.yml'])
    
    
#using connection string to access db
client = pymongo.MongoClient('mongodb+srv://sprintteam03:Dasphy03@dev-backend-cluster.ohvhxe6.mongodb.net/?retryWrites=true&w=majority')
db = client['sprint']
collection = db['users']

#group_id from payload
with open('payload.json', "r") as f:
    user_id = int(json.load(f)["user_id"])

#query for group using group_id
group = list(collection.find({"user_id" : ObjectId(user_id)}))

#create string of hosts and write to inventory file and run playbook
parseGroupToInventoryAndRunPlaybook(group)