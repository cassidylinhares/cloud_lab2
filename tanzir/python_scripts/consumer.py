from kafka import KafkaConsumer

TOPIC_NAME="greetings"
KAFKA_SERVER=["localhost:9093","localhost:9094","localhost:9095"]
consumer=KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER,auto_offset_reset='earliest')
print("Consumer subscribed")
for msg in consumer:
    print( f"Msg:{msg.value.decode('utf-8')} Partition:{msg.partition}")

consumer.close()