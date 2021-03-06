const {Kafka} = require("kafkajs")



run();



async function run(){
    try
    {
        const kafka = new Kafka({
            "clientId": "yeet",
            "brokers" :["localhost:9093", "localhost:9094", "localhost:9095"]
       })

       const consumer = kafka.consumer({"groupId":"control_group"});
       console.log("Connecting.....")
       await consumer.connect()
       console.log("Connected!")

       await consumer.subscribe({

         "topic": "yeet",
         "fromBeginning": true
       })




       await consumer.run({
            "eachMessage": async result => {
                console.log(`${result.message.value} on partition ${result.partition}`)
            }
         })



    }
    catch(ex)
    {
        console.error(`Error code ${ex}`)
    }

    finally{}
}