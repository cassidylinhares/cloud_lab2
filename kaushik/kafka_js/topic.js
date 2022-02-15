const {Kafka} = require("kafkajs")

run();

async function run() {
    try {
        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        })

        const admin = kafka.admin();
        console.log("Waiting to Connect...!")
        await admin.connect //promise, therefore, we need AWAIT
        console.log("Connected!")

        await admin.createTopics({
            "topics": [{
                "topic": "Users",
                "numPartitions": 2 
            }]
        })
        console.log("Topics created successfully!")
        await admin.disconnect();
    } catch (error) {
        console.error(`Something bad happened ${error}`)
    }
    finally{
        process.exit(0);
    }
}