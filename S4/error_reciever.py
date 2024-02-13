import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

result = ch.queue_declare(queue='' , exclusive=True)
qname = result.method.queue

severity = 'error'

ch.queue_bind(exchange='direct_logs',queue=qname,routing_key=severity)

print('wating for message')

def callback(ch, method ,properties , body):
    with open('error_logs.log' , 'a') as el :
        el.write(str(body)+'\n')

ch.basic_consume(queue=qname , on_message_callback=callback , auto_ack=True)

ch.start_consuming()
