from asyncio import constants
from kafka import KafkaConsumer
from confluent_kafka import Consumer

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9093', auto_offset_reset='earliest')

consumer.subscribe(['topic'])
print("Consumer subscribed")

for msg in consumer:
    if msg.key is not None:
        print(
            f"Topic:{msg.topic} Msg:{int.from_bytes(msg.key, 'big')}:{msg.value.decode('utf-8')} Partition:{msg.partition}")
    else:
        print(
            f"Topic:{msg.topic} Msg:{msg.value.decode('utf-8')} Partition:{msg.partition}")

consumer.close()
