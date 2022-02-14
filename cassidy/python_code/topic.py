from kafka import KafkaAdminClient
from kafka.admin import NewTopic


def main():
    try:
        admin = KafkaAdminClient(
            bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'])
        print("Connected")

        topic = NewTopic(name='topic', num_partitions=3, replication_factor=3)
        topic2 = NewTopic(name='topic2', num_partitions=3,
                          replication_factor=2)

        admin.create_topics(new_topics=[topic, topic2])
        print("Topics created.")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
