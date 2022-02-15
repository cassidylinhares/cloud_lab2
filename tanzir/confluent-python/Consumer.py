from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers':'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':'TAP55C7F4XNTFKVV',
    'sasl.password':'UQyq3c3hLWw+SDNFUYy26iOyFx8EupH+tairRmBuFN+ZU4SDNBGuwI8HAOPqjsuZ',  
    'session.timeout.ms':45000,
    'auto.offset.reset':'earliest',
    'group.id':'testGroup'
})

consumer.subscribe(['tests'])
print("consumer subbed")

while True:
    msg=consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("consumer error:{}".format(msg.error()))
        continue
    print('Received msg: {} on partition:{}'.format(msg.value().decode('utf-8'),msg.partition()))