from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'pkc-v12gj.northamerica-northeast2.gcp.confluent.cloud:9092',
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':'CQAIHGDLFKB355G2',
    'sasl.password':'RRZCzkDmHmihWLJtPVnz3ByHSd0gghRBs0Gz9k+nwy2f5+tZyR/aveyud0Njt75d',
    'session.timeout.ms': 45000
})

def acked(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(
            msg.topic(), msg.partition()))


for i in range(10):
    producer.poll(0)

    producer.produce(
        'cars',
        key=i.to_bytes(5, 'big'),
        value=b'Outback',
        callback=acked
    )

producer.flush()