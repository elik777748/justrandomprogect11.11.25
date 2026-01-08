import time
import config
import ssl
import pika
import json

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(

    host=config.RMQ_HOST,
    port=config.RMQ_PORT,
    virtual_host=config.RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=config.RMQ_USER,password=config.RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)

def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)



def produce_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties,body):
    data = json.loads(body.decode("utf-8"))
    print(f"Новий лог: {data["event"]}, user_id: {data["user_id"]}")

 

def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = "news"
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=produce_message,
        auto_ack=True
    )
    channel.start_consuming()

def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_message(channel)


if __name__ == "__main__":
    main()
