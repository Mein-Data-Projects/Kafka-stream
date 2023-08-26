import os

from confluent_kafka import KafkaException, Producer
from dotenv import load_dotenv


def main():
    settings = {
        "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        "security.protocol": os.getenv("KAFKA_SECURITY_PROTOCOL"),
        "sasl.mechanisms": os.getenv("KAFKA_SASL_MECHANISMS", "PLAIN"),
        "sasl.username": os.getenv("KAFKA_SASL_USERNAME"),
        "sasl.password": os.getenv("KAFKA_SASL_PASSWORD"),
    }

    producer = Producer(settings)
    producer.produce(topic="MeineKafkaTopic", key=None, value="MeineKafkaTopic-111")
    # Wait for the confirmation that the message was received
    producer.finish()


if __name__ == "__main__":
    load_dotenv()
    main()
