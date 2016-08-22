#!/usr/bin/env python
import pika


'''first thing is to connect to the RabbitMQ server'''
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
'''we are connected now, to the server on local machine'localhost' '''

'''Now declare the queue'''
channel.queue_declare(queue='hello')

'''Receiving messages from the queue is more complex. It works by subscribing a callback 
function to a queue. Whenever we receive a message, this callback function is called by 
the Pika library. In our case this function will print on the screen the contents of the 
message.'''
print (' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body))

'''Next, we need to tell RabbitMQ that this particular callback function should receive 
messages from our hello queue'''
channel.basic_consume(callback, queue='hello', no_ack=True)
'''And finally, we enter a never-ending loop that waits for data and runs callbacks 
whenever necessary.'''
channel.start_consuming()
