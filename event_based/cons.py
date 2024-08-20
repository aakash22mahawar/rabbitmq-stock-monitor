import pika

# Set the RabbitMQ connection URL
url = "amqp://localhost"  # Replace with your RabbitMQ URL if necessary

# Import your apple_stock_price function
from apple_stock_monitor import apple_stock_price

def start_consume():
    connection = None
    try:
        # Establish connection to RabbitMQ server
        connection = pika.BlockingConnection(pika.URLParameters(url))
        channel = connection.channel()
        print('Connection established successfully!')

        # Declare the exchange with durability
        exchange = 'stock'
        channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)

        # Declare the queue with durability
        queue_name = 'stock_queue'
        channel.queue_declare(queue=queue_name, durable=True)

        # Bind the queue to the exchange
        routing_key = 'event'  # This should match the routing key used in the producer
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)

        # Set QoS for fair dispatch (only 1 unacknowledged message at a time)
        channel.basic_qos(prefetch_count=1)

        # Consume messages from the queue
        def callback(ch, method, properties, body):
            print(f"Received message: {body.decode()}")
            apple_stock_price()  # Call your scraping function
            ch.basic_ack(delivery_tag=method.delivery_tag)

        # Start consuming
        channel.basic_consume(queue=queue_name, on_message_callback=callback)

        print('Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if connection and not connection.is_closed:
            connection.close()
            print("Connection closed.")

# Start the consumer
start_consume()
