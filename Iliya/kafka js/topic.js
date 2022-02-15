const {Kafka} = require("kafkajs")



run();



async function run(){
    try
    {
        const kafka = new Kafka({
            "clientId": "yeet",
            "brokers" :["localhost:9093", "localhost:9094", "localhost:9095"]
       })

       const admin = kafka.admin();
       console.log("Connecting.....")
       await admin.connect()
       console.log("Connected!")


       await admin.createTopics({

            "topics": [{

                "topic": "yeet",
                "numPartitions": 2,
                "replicationFactor": 2
            }, {
                "topic": "something",
                "numPartitions": 2,
                "replicationFactor": 1
            }]
        })
        console.log("Nothing wrong so far")
        await admin.disconnect();




    }
    catch(ex)
    {
        console.error(`Error code ${ex}`)
    }

    finally{
        process.exit(0);
    }
}