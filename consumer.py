import pika
import json
from pymongo import MongoClient
from datetime import datetime

rabbitmq_server = 'localhost'  

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_server))
channel = connection.channel()

queue_name = 'record_timestamp'
channel.queue_declare(queue=queue_name, durable=True)


mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client["MQ_db"]
collection = db["statuses"]

def callback(ch, method, properties, body):
    print(f"Message Received - {body}")
    data = json.loads(body)
    data['timestamp'] = datetime.now()

    collection.insert_one(data)


channel.basic_consume(queue=queue_name, on_message_callback=callback)

print('Waiting for messages.')
channel.start_consuming()