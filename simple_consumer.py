from confluent_kafka import Consumer
from kafka_settings import KafkaSettings
from kafka_producer import KafkaProducer
from kafka_producer_message import ProducerMessage

if __name__ == "__main__":
    settings = KafkaSettings()
    consumer = Consumer(settings.conf)
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is not None and msg.error() is None:
                print(
                    "key = {key:12} value= {value:12}".format(
                        key=msg.key().decode("utf-8"), value=msg.value().decode("utf-8")
                    )
                )
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
