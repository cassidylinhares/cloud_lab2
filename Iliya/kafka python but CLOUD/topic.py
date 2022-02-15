#Topic.py

from kafka import KafkaAdminClient

from kafka.admin import NewTopic



try:
    client_adm = KafkaAdminClient(bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'])
    
    yeet = NewTopic(
        name='yeet', 
        num_partitions=2, 
        replication_factor=2
    )
    
    something = NewTopic(
        name='something', 
        num_partitions=2,
        replication_factor=1
    )
    
    last = NewTopic(
        name='last', 
        num_partitions=2
        ,
        replication_factor=3
    )

    client_adm.create_topics(new_topics=[yeet, something, last])
    print ("We got this far")

    
except Exception as error:
        
        
    print("Error messsage:  ", error)

