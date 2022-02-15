from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'pkc-3w22w.us-central1.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'N6X6STEHV7XVBGBC',
    'sasl.password': 'A9gGbpJ1DbzpJ/iTAYDAzl3Os+K2hQXNbTEecxohpOP9bQw3rAunZHESgoDKnVHa',
    'session.timeout.ms': 45000,
})

print("Connected!")


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(
            msg.topic(), msg.partition()))


for i in range(10):
    producer.poll(0)

    producer.produce(
        'poems',
        key=i.to_bytes(2, 'big'),
        value=b'It is what it is',
        callback=delivery_report
    )

producer.flush()
