#Consumer2.py


from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9093', auto_offset_reset='earliest')

consumer.subscribe('something')


for message in consumer:

    print(f"Message:{message.value.decode('utf-8')} Partition:{message.partition}")

consumer.close()
