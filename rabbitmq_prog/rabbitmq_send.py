#!/usr/bin/env python
import pika
import time
body = "Hello world!!! this is a test program"
'''first thing is to connect to the RabbitMQ server'''
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
'''we are connected now, to the server on local machine'localhost' '''

'''Now declare the queue'''
channel.queue_declare(queue='hello')

'''In RabbitMQ a message can never be sent directly to the queue, it always needs 
to go through an exchange.'''
i = 10
while i:
	time.sleep(1) #Introduces 1 second delay in the loop
	channel.basic_publish(exchange='', routing_key='hello', body=body)
	channel.basic_publish(exchange='', routing_key='hello', body='Hello World!!!!')
	channel.basic_publish(exchange='', routing_key='hello', body='i = %r!!!' % i)

	print (" [x] Sent 'Hello World!'")
	i -= 1

''' Before exiting the program we need to make sure the network buffers were flushed 
and our message was actually delivered to RabbitMQ. We can do it by gently closing 
the connection.'''

connection.close()
