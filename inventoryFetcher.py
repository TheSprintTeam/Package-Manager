import pymongo
import sys
import subprocess
import json
from bson.objectid import ObjectId

CONNECTION_STRING = 'mongodb+srv://pacmanuser:Dasphy03.@dev-backend-cluster.ohvhxe6.mongodb.net/?retryWrites=true&w=majority'
## methods to parse host data
class hostStrings:

    def __init__(self, host):
        self.user = host["user"]
        self.ip  = host["ip"]
        self.password = host["password"]
        self.host_vars = " ansible_ssh_user="+self.user + " ansible_ssh_password=" + self.password 

def parseGroupToInventoryAndRunPlaybook(group):
    hostGroup = "[hosts] \n"
    for host in group:
        strings = hostStrings(host)
        with open("inventories/" +strings.ip + ".ini", "w") as vars:
            vars.write(hostGroup+strings.ip+strings.host_vars)
        subprocess.run(['ansible-playbook', '-i', "inventories/" + strings.ip + ".ini", 'playbook.yml'])
    
    
#using connection string to access db
client = pymongo.MongoClient(CONNECTION_STRING)
db = client['sprint']
collection = db['users']

#group_id from payload
with open('payload.json', "r") as f:
    user_id = json.load(f)["user_id"]
    

#query for user using user_id
user = list(collection.find({"_id" : ObjectId(user_id)}))

#create string of hosts and write to inventory file and run playbook
parseGroupToInventoryAndRunPlaybook(user)