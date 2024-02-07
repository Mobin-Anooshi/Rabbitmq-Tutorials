import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


ch1 = connection.channel()

ch1.queue_declare(queue='hello')

for i in range(10):

    ch1.basic_publish(exchange='' , routing_key='hello',body=str(i))

    print('SEND')

connection.close()  