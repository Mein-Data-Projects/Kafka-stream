import os

from confluent_kafka import KafkaException, Producer
from dotenv import load_dotenv

def main():
    settings = 
    
    producer = Producer(settings)
    producer.produce(
        topic="MeineKafkaTopic",
        key=None,
        value="MeineKafkaTopic-111"
    )
    # Wait for the confirmation that the message was received
    producer.finish()


if __name__ == "__main__":
    load_dotenv()
    main()