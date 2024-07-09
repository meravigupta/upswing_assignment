import pika
import time 
import json
import random

rabbitmq_server = 'localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_server))
channel = connection.channel()

queue_name = 'record_timestamp'
channel.queue_declare(queue=queue_name, durable=True)

def publish_status():
    while True:
        status = random.randint(0, 6)
        message = json.dumps({'record_time':True, 'status':status})
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message
            )
        time.sleep(1)


if __name__ == "__main__":
    publish_status()
