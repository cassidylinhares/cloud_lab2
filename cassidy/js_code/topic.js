const { Kafka } = require("kafkajs")

run();

async function run() {
    try {
        const kafka = new Kafka({
            "clientId": "lab2",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        });

        const admin = kafka.admin();
        console.log("Trying to connect ...");
        await admin.connect();
        console.log("Connected");

        admin.createTopics({
            "topics": [{
                "topic": "topic",
                "numPartitions": 3,
                "replicationFactor": 3
            }, {
                "topic": "topic2",
                "numPartitions": 3,
                "replicationFactor": 2
            }]
        });

        console.log("Topics created");

        await admin.disconnect();

    } catch(e) {
        console.error(e);
    } finally {
        process.exit(0);
    }
}
