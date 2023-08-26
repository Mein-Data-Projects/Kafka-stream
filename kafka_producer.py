"""
Customize our produce method with support for various errors
and automatically flush message once produced
"""

from confluent_kafka import KafkaError, KafkaException, Producer

from kafka_producer_message import ProducerMessage
from kafka_settings import KafkaSettings

class KafkaProducer:
    def __init__(self, settings: KafkaSettings) -> None:
        self._producer = Producer(settings.conf)

    def produce(self, message: ProducerMessage):
        try:
            self._producer.produce(message.topic, key=message.key, value=message.value)
            # makes all buffered records immediately available to send
            # will block until the requests associated with sending these
            # records are completed
            self._producer.flush()
        except KafkaException as exc:
            # skip over the message if it's too large for the Kafka cluster
            # to consume
            if exc.args[0].code() == KafkaError.MSG_SIZE_TOO_LARGE:
                pass # Handle the error here
            else:
                raise exc