#c.py

from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'pkc-v12gj.northamerica-northeast2.gcp.confluent.cloud:9092',
    'group.id': 'test_group',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '34KB32LT7ENBK3GQ',
    'sasl.password': 'X4LBVjcWSSP662znQHHmD2eBuQvQ+m/tOGLKeAO/jvOyEU95wkLfHBhi76vedBL9',
    'session.timeout.ms': 30000,
    'auto.offset.reset': 'earliest'
})


consumer.subscribe(['poems'])

while True:
    a = consumer.poll(1.0)


    if a is None:
        continue


    print('', a.value().decode('utf-8'))


consumer.close()