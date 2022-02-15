const {Kafka} = require("kafkajs")



run();



async function run(){
    try
    {
        const kafka = new Kafka({
            "clientId": "yeet",
            "brokers" :["localhost:9093", "localhost:9094", "localhost:9095"]
       })

       const producer = kafka.producer();
       console.log("Connecting.....")
       await producer.connect()
       console.log("Connected!")

       
       const result = await producer.send({

            "topic": "yeet", "messages": [{"value": "2nd msg","partition": 0}]
        });

        console.log(`Message sent: ${JSON.stringify(result)}`);



        console.log("Nothing wrong so far")
        await producer.disconnect();




    }
    catch(ex)
    {
        console.error(`Error code ${ex}`)
    }

    finally{
        process.exit(0);
    }
}