from celery import shared_task
from django.core.mail import send_mail
from .models import Order  


@shared_task
def order_created(order_id):
	"""
	TASKS TO SEND AN E-MAIL NOTIFICATION WHEN AN ORDER IS SUCCESSFULLY CREATED.
	"""

	order = Order.objects.get(id=order_id)
	subject= f'Order no. {order.id}'
	message= f'Dear {order.first_name}, \n\n You have successfully placed an order. Your order ID is {order.id}.'
	mail_sent = send_mail(subject,message,"sbijay433@gmail.com",[order.email])

	return mail_sent