from celery import shared_task
from mail_templated import send_mail

@shared_task
def send_email(template_name: str, from_email:str, context:dict, recipient_list: list):
    send_mail(template_name=template_name, from_email=from_email, context=context,
              recipient_list=recipient_list)