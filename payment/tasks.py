from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order  


@shared_task
def payment_completed(order_id):
	"""
	TASK TO SEND AN E-MAIL NOTIFICATION WHEN AN ORDER IS SUCCESSFULLY PAID.
	"""
	subject = f"My shop - Invoice no. {order.id}"
	message = 'please, find attached the invoice for your recent purchase.'
	email = EmailMessage(subject,message,'sbijay433@gmail.com',[order.email])

	html = render_to_string("orders/order/pdf.html",{"order":order})
	out=BytesIO()
	stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'shop/pdf.css')]
	weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)

	email.attach(f"order_{order.id}.pdf",out.getvalue(),'application/pdf')

	email.send()