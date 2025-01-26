from django.core.mail import send_mail
from django.conf import settings

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-created_at']


class Office(models.Model):
    city_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()
    photo = models.ImageField(upload_to='offices/')
    created_at = models.DateTimeField(auto_now_add=True)
    main = models.BooleanField(default=False, verbose_name="Is this office HeadQuarter ?")

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'
        ordering = ['-created_at']


class General(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone}|{self.email}"

    class Meta:
        verbose_name = 'General'
        verbose_name_plural = 'Generals'
        ordering = ['-created_at']


class Post(models.Model):
    title = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    content = CKEditor5Field('Content')
    photo = models.ImageField(upload_to='posts_news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        ordering = ['-created_at']


class Partner(models.Model):

    logo_photo = models.ImageField(upload_to='partners_funds/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Partner/Fund'
        verbose_name_plural = 'Partners/Funds'
        ordering = ['-created_at']


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-created_at']


class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)
    since = models.DateField(verbose_name="Since", default='2024-12-08')
    till = models.DateField(verbose_name="Till", default='2024-12-08')
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']


class Application(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    document = models.FileField(upload_to="applications/documents/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Form {self.id}"

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'
        ordering = ['-created_at']


class UserEmail(models.Model):
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User Email {self.id}"

    class Meta:
        verbose_name = 'User Email'
        verbose_name_plural = 'User Emails'
        ordering = ['-created_at']


class TeamMember(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    position = models.CharField(max_length=255, verbose_name="Position")
    image = models.ImageField(upload_to='team_members/', verbose_name="Image")
    facebook = models.CharField(max_length=255, verbose_name="Facebook",
                                null=True, blank=True)
    linked_in = models.CharField(max_length=255, verbose_name="LinkedIn",
                                 null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'


class SMSCampaign(models.Model):
    subject = models.CharField(max_length=255)  # Тема смс
    message = models.TextField()  # Содержание сообщения
    sent_at = models.DateTimeField(auto_now_add=True)  # Время отправки

    def __str__(self):
        return f"SMS Campaign: {self.subject}"

    def send_sms_to_emails(self):
        # Логика отправки смс на все почты
        emails = UserEmail.objects.all()
        for user_email in emails:
            self.send_sms(user_email.email)

    def send_sms(self, email):
        # Здесь можно подключить реальную систему отправки смс
        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        )

class News(models.Model):
    title = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    content = CKEditor5Field('Content')
    photo = models.ImageField(upload_to='posts_news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

