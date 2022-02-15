from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'pkc-v12gj.northamerica-northeast2.gcp.confluent.cloud:9092',
    'group.id': 'car',
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':'CQAIHGDLFKB355G2',
    'sasl.password':'RRZCzkDmHmihWLJtPVnz3ByHSd0gghRBs0Gz9k+nwy2f5+tZyR/aveyud0Njt75d',
    'session.timeout.ms': 45000,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['cars'])
print("Subscribed to topic!")

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