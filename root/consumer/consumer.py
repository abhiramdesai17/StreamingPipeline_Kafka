from kafka import KafkaConsumer, KafkaProducer
import json
import os

# Kafka configuration
bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']
input_topic = os.environ['INPUT_TOPIC']
output_topic = os.environ['OUTPUT_TOPIC']

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    input_topic,
    bootstrap_servers=bootstrap_servers,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    data = message.value
    
    # Basic processing (e.g., filtering out certain locales)
    if data.get('locale') != 'RU':
        continue

    # Example of adding a new field
    data['processed_timestamp'] = 'some_new_value'  # Add appropriate value

    # Produce the processed message to the new topic
    producer.send(output_topic, value=data)

    # Commit the message
    producer.flush()

print("Kafka Consumer has finished processing.")
