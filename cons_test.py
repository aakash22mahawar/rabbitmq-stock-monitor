import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Declare the queue and bind it to the exchange with a routing key
channel.queue_declare(queue='hello')
channel.queue_bind(exchange='direct_logs', queue='hello', routing_key='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Consume messages from the queue
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
