import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs', exchange_type='direct')


result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

severities = ('info', 'Warning', 'error')

for severrity in severities :
    ch.queue_bind(exchange='direct_logs' , queue=qname ,routing_key=severrity )
    
print('wating for message')


def callback(ch, method ,properties ,body):
    print(f'{method.routing_key} , {body}')

ch.basic_consume(queue=qname , on_message_callback=callback , auto_ack=True)
ch.start_consuming()    