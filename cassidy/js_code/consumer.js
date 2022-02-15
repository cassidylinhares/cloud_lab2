const { Kafka } = require("kafkajs")

run();

async function run() {
    try {
        const kafka = new Kafka({
            "clientId": "lab2",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        });

        const consumer = kafka.consumer({groupId:"boop"});
        console.log("Trying to connect ...");
        await consumer.connect();
        console.log("Connected");

        await consumer.subscribe({
            "topic": "topic",
            "fromBeginning": true
        });

        await consumer.run({
            "eachMessage": async result => {
                console.log(`Topic: ${result.topic} Message: ${result.message.value} on partition ${result.partition}`);
            }
        })

    } catch(e) {
        console.error(e);
    } 
}
