from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'pkc-3w22w.us-central1.gcp.confluent.cloud:9092',
    'group.id': 'boop',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'N6X6STEHV7XVBGBC',
    'sasl.password': 'A9gGbpJ1DbzpJ/iTAYDAzl3Os+K2hQXNbTEecxohpOP9bQw3rAunZHESgoDKnVHa',
    'session.timeout.ms': 45000,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['poems'])
print("Consumer subscribed")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {} on Partition: {}'.format(
        msg.value().decode('utf-8'), msg.partition()))


consumer.close()
