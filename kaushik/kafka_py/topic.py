from kafka import KafkaAdminClient
from kafka.admin import NewTopic

def main():
    try: 
        print("Attempting to Connect...!")
        admin = KafkaAdminClient(
            bootstrap_servers= ["localhost:9093", "localhost:9094", "localhost:9095"]
        )
        print("Connected!") 

        cars = NewTopic(name='cars', num_partitions=2, replication_factor=3)
        admin.create_topics(new_topics=[cars])
        print("Topics created!")
    except Exception as e:
        print("Something went wrong:" + e)

if __name__ == "__main__":
    main()