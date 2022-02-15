from asyncio import constants
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'], auto_offset_reset='earliest')

consumer.subscribe(['cars'])
print("Consumer subscribed")

for msg in consumer:
    print(
        f"Topic:{msg.topic} Msg:{msg.value.decode('utf-8')} Partition:{msg.partition}")

consumer.close()