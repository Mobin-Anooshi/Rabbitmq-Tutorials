import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch1 = connection.channel()

ch1.queue_declare(queue='first',durable=True)  #Survive reboots of the broker

messages = 'this is test message'

for i in range(10):
    ch1.basic_publish(exchange='' , routing_key='first',body=str(i) ,properties=pika.BasicProperties(delivery_mode=2,)) #write in hard
    
    print('Message Send')

ch1.close()