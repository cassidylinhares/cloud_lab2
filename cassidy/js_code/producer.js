const { Kafka } = require("kafkajs")

run();

async function run() {
    try {
        const kafka = new Kafka({
            "clientId": "lab2",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        });

        const producer = kafka.producer();
        console.log("Trying to connect ...");
        await producer.connect();
        console.log("Connected");

        const result = await producer.send({
            "topic": "topic2",
            "messages": [{
                "value": "ayoo",
                "partition": 0
            }]
        });

        console.log(`Message sent: ${JSON.stringify(result)}`);

        await producer.disconnect();

    } catch(e) {
        console.error(e);
    } finally {
        process.exit(0);
    }
}
