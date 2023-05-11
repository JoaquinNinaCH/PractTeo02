from kafka import KafkaProducer

# Configura el productor de Kafka con la dirección del broker
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Envia un mensaje al topic 'ejemplo'
producer.send('ejemplo', b'Hola mundo desde Kafka!')

# Cierra el productor
producer.close()