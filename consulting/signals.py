from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Application, SMSCampaign

@receiver(post_save, sender=Application)
def send_email_on_new_application(sender, instance, created, **kwargs):
    if created:
        subject = f"New Application from {instance.first_name} {instance.last_name}"
        message = f"New application details:\n\nFirst Name: {instance.first_name}\nLast Name: {instance.last_name}\nEmail: {instance.email}\nPhone: {instance.phone}\nMessage: {instance.message}"
        recipient_list = ['azamat.yakhyayeff@gmail.com']  # Замените на свой email для получения заявок
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)


@receiver(post_save, sender=SMSCampaign)
def send_sms_on_create(sender, instance, created, **kwargs):
    if created:
        # Отправляем смс сразу после создания кампании
        instance.send_sms_to_emails()