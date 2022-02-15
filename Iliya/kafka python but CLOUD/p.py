#p.py


from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'pkc-v12gj.northamerica-northeast2.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '34KB32LT7ENBK3GQ',
    'sasl.password': 'X4LBVjcWSSP662znQHHmD2eBuQvQ+m/tOGLKeAO/jvOyEU95wkLfHBhi76vedBL9',
    'session.timeout.ms': 30000
})


producer.poll(0)

producer.produce('poems', key = bytes('15','utf-8'), value = bytes('line 15','utf-8'))

producer.flush()

