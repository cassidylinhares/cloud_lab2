#Producer.py

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'])


producer.send(topic='yeet', value = bytes('hi','utf-8'), partition=0)
producer.send(topic='something', value = bytes('1','utf-8'), partition=1)
producer.send(topic='something', value = bytes('2','utf-8'), partition=0)
producer.send(topic='last', value = bytes('bye','utf-8'), partition=0)






producer.close()
