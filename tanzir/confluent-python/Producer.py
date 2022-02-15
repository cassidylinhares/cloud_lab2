from confluent_kafka import Producer

producer=Producer({
    'bootstrap.servers':'pkc-6ojv2.us-west4.gcp.confluent.cloud:9092',
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':'TAP55C7F4XNTFKVV',
    'sasl.password':'UQyq3c3hLWw+SDNFUYy26iOyFx8EupH+tairRmBuFN+ZU4SDNBGuwI8HAOPqjsuZ',  
    'session.timeout.ms': 45000,
})

print("connected")

def err_report(err,msg):
    if err is not None:
        print('message delivery failed: {}'.format(err))
    else:
        print('message delivery sent to: {}'.format(msg.topic()))

for i in range(10):
    producer.poll(0)
    producer.produce(
        'tests',
        key=i.to_bytes(3,'big'),
        value=b'Testing123',
        callback=err_report
    )

producer.flush()

