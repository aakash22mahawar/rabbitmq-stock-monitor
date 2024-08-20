import pika
import time

# Set the interval duration (in seconds)
INTERVAL_DURATION = 30  # 30 seconds

# Set the RabbitMQ connection URL
url = "amqp://localhost"

def start_timer():
    connection = None
    try:
        # Establish connection to RabbitMQ server
        connection = pika.BlockingConnection(pika.URLParameters(url))
        channel = connection.channel()
        print('Connection established successfully!')

        # Declare the exchange with durability
        exchange_name = 'stock'
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

        # Declare the queue with durability
        queue_name = 'stock_queue'
        channel.queue_declare(queue=queue_name, durable=True)

        # Bind the queue to the exchange
        routing_key = 'event'
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

        while True:
            # Message to be sent
            message = "<< get apple stock new price >>"
            print('Sending to queue:', message)

            # Publish the message to the direct exchange with persistence
            channel.basic_publish(exchange=exchange_name,
                                  routing_key=routing_key,
                                  body=message,
                                  properties=pika.BasicProperties(
                                      delivery_mode=2,  # make message persistent
                                  ))

            # Wait for the interval duration before sending the next message
            time.sleep(INTERVAL_DURATION)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if connection and not connection.is_closed:
            connection.close()
            print("Connection closed.")

# Start the timer
start_timer()
