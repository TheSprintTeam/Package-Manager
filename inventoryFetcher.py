import pymongo
import sys

## grab group id arg from CLI
group_id = int(sys.argv[1])
inventory_file = sys.argv[2]

## methods to parse host data
def hostString(host):
    user = host["hostInfo"]["user"]
    ip  = host["hostInfo"]["host"]
    password = host["hostInfo"]["password"]
    hoststring = ip + " ansible_ssh_user="+user + " ansible_ssh_password=" + password + "\n"
    return hoststring

def parseGroupToInventory(group):
    dumpString = "[hosts] \n"
    for host in group:
        dumpString += hostString(host)
    with open(inventory_file, "w") as inventory:
        inventory.write(dumpString)
    print(dumpString)

#using connection string to access db
client = pymongo.MongoClient('mongodb+srv://h64shah:titanic2@sprint-cluster.lneibho.mongodb.net/')
db = client['inventory']
collection = db['hosts']

#query for group using group_id
group = list(collection.find({"group_id" : group_id }))

#create string of hosts and write to inventory file
parseGroupToInventory(group)




