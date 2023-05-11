from kafka import KafkaConsumer

# Configura el consumidor de Kafka con la dirección del broker y el topic a consumir
consumer = KafkaConsumer('ejemplo', bootstrap_servers='localhost:9092')

# Lee y muestra los mensajes del topic
for message in consumer:
    print(message.value.decode('utf-8'))