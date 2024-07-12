from kafka import KafkaConsumer, KafkaProducer
import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka configuration
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS', 'localhost:9092')
input_topic = os.environ.get('INPUT_TOPIC', 'user-login')
output_topic = os.environ.get('OUTPUT_TOPIC', 'processed-user-login')

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    input_topic,
    bootstrap_servers=bootstrap_servers,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=False
)

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    try:
        data = message.value
        
        # Basic processing (e.g., filtering based on locale)
        if 'locale' not in data or data['locale'] != 'RU':
            continue

        # Example of adding a new field
        data['processed_timestamp'] = 'some_new_value'  # Add appropriate value

        # Produce the processed message to the new topic
        producer.send(output_topic, value=data)

        # Log the processed message
        logger.info(f"Processed message: {data}")

    except Exception as e:
        # Log the error
        logger.error(f"Error processing message: {e}")

    # Commit the message
    producer.flush()

print("Kafka Consumer has finished processing.")




# from kafka import KafkaConsumer, KafkaProducer
# import json
# import os

# # Kafka configuration
# bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']
# input_topic = os.environ['INPUT_TOPIC']
# output_topic = os.environ['OUTPUT_TOPIC']

# # Initialize Kafka Consumer
# consumer = KafkaConsumer(
#     input_topic,
#     bootstrap_servers=bootstrap_servers,
#     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
# )

# # Initialize Kafka Producer
# producer = KafkaProducer(
#     bootstrap_servers=bootstrap_servers,
#     value_serializer=lambda x: json.dumps(x).encode('utf-8')
# )

# for message in consumer:
#     data = message.value
    
#     # Basic processing (e.g., filtering out certain locales)
#     if data.get('locale') != 'RU':
#         continue

#     # Example of adding a new field
#     data['processed_timestamp'] = 'some_new_value'  # Add appropriate value

#     # Produce the processed message to the new topic
#     producer.send(output_topic, value=data)

#     # Commit the message
#     producer.flush()

# print("Kafka Consumer has finished processing.")
