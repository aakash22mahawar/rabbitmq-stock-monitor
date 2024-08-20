import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Declare the queue and bind it to the exchange with a routing key
channel.queue_declare(queue='hello')
channel.queue_bind(exchange='direct_logs', queue='hello', routing_key='hello')

# Publish a message to the direct exchange
channel.basic_publish(exchange='direct_logs',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()
