# StreamingPipeline_Kafka

# Real-Time Streaming Data Pipeline with Kafka and Docker

This project demonstrates a real-time streaming data pipeline using Kafka and Docker. The pipeline ingests streaming data, processes it in real-time, and stores the processed data into a new Kafka topic.

## Table of Contents
- [Project Setup](#project-setup)
- [Services](#services)
- [Kafka Consumer](#kafka-consumer)
- [How to Run](#how-to-run)
- [Design Choices and Considerations](#design-choices-and-considerations)

## Project Setup

Ensure you have Docker installed locally. The provided `docker-compose.yml` file sets up the necessary Docker containers for Kafka, Zookeeper, and a data generator.

### Services

1. **Zookeeper**: Manages and coordinates Kafka brokers.
2. **Kafka**: A distributed streaming platform for building real-time data pipelines and streaming applications.
3. **Data Generator**: Produces sample messages to the `user-login` topic.
4. **Kafka Consumer**: Consumes data from the `user-login` topic, processes it, and produces the processed data to a new topic `processed-user-login`.

### Sample Message

Sample message schema produced by the data generator:

```json
{
  "user_id": "424cdd21-063a-43a7-b91b-7ca1a833afae",
  "app_version": "2.3.0",
  "device_type": "android",
  "ip": "199.172.111.135",
  "locale": "RU",
  "device_id": "593-47-5928",
  "timestamp": "1694479551"
}


## Kafka Consumer
The Kafka consumer is implemented in Python. It consumes messages from the user-login topic, processes them (e.g., filtering based on certain conditions), and produces the processed messages to a new topic processed-user-login.

## Consumer Script
The consumer script (consumer/consumer.py) performs the following tasks:

Consumes messages from the user-login topic.
Processes the messages (e.g., filtering out certain locales).
Adds new fields to the messages (if necessary).
Produces the processed messages to the processed-user-login topic.

## How to Run
Clone the repository and navigate to the project root directory.

Build and start the Docker containers:

docker-compose up --build

This command will set up the local development environment with Kafka, Zookeeper, the data generator, and the Kafka consumer.

## Design Choices and Considerations

### Efficiency
The pipeline is designed to handle streaming data continuously and efficiently. Kafka's distributed nature ensures high throughput and low latency.

### Scalability
Kafka's scalability features allow the pipeline to handle increasing volumes of data by adding more brokers and partitions.

### Fault Tolerance
Kafka ensures fault tolerance by replicating data across multiple brokers. The consumer can handle errors and retries, ensuring robust data processing.

### Data Flow
Data Ingestion: The data generator produces messages to the user-login topic.
Data Processing: The Kafka consumer consumes messages from the user-login topic, processes them, and produces the processed messages to the processed-user-login topic.
Data Storage: The processed data is stored in the processed-user-login topic for further consumption or analysis.

# Conclusion
This project demonstrates a basic real-time streaming data pipeline using Kafka and Docker. It highlights the setup of a local development environment, implementation of a Kafka consumer for data processing, and design considerations for efficiency, scalability, and fault tolerance.