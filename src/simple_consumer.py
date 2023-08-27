from dotenv import load_dotenv
from confluent_kafka import Consumer
from kafka_settings import KafkaSettings

if __name__ == "__main__":
    load_dotenv()

    settings = KafkaSettings()
    settings.conf["group.id"] = "python-group-1"
    consumer = Consumer(settings.conf)
    consumer.subscribe(["MeinKafkaTopic",])
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
