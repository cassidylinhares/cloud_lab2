const {Kafka} = require("kafkajs")

run();
async function run(){
    try
    {
         const kafka = new Kafka({
              "clientId": "myapp",
              "brokers" :["localhost:9093", "localhost:9094", "localhost:9095"]
         })

        const consumer = kafka.consumer({"groupId":"test"});
        console.log("Connecting.....")
        await consumer.connect()
        console.log("Connected!")
        
        consumer.subscribe({
            "topic": "Users",
            "fromBeginning": true
        })

        await consumer.run({
            "eachMessage": async result => {
                console.log(`Received msg: ${result.message.value} on partition ${result.partition}`)
            }
        })
    }
    catch(ex)
    {
        console.error(`Something bad happened ${ex}`)
    }
    finally{
        
    }


}