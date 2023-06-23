/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
const database = 'inventory';

use(database);

// Insert records
db.hosts.insertMany([
    {
        "group_id" : 1,
        "host_id" : 1,
        "hostInfo":{
            "host" : "host1",
            "user" : "1",
            "password" : "pass1"
        }
           
    },
    {
        "group_id" : 1,
        "host_id" : 2,
        "hostInfo":{
            "host" : "host2",
            "user" : "2",
            "password" : "pass2"
        }
           
    },
    {
        "group_id" : 2,
        "host_id" : 3,
        "hostInfo":{
            "host" : "host3",
            "user" : "3",
            "password" : "pass3"
        }
           
    }
]);

// Delete all records
//db.hosts.deleteMany({});

// use connection string to connect playground
// mongodb+srv://h64shah:titanic2@sprint-cluster.lneibho.mongodb.net/