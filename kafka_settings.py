"""
Encapsulate our Apache Kafka settings
"""

import os

class KafkaSettings:
    def __init__(self) -> None:
        self.conf = {
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
        'security.protocol': os.getenv('KAFKA_SECURITY_PROTOCOL'),
        'sasl.mechanisms': os.getenv('KAFKA_SASL_MECHANISMS', "PLAIN"),
        'sasl.username': os.getenv('KAFKA_SASL_USERNAME'),
        'sasl.password': os.getenv('KAFKA_SASL_PASSWORD'),
    }