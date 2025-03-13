# from celery import shared_task
# from django.core.mail import send_mail
# from django.conf import settings
# from time import sleep


# @shared_task
# def send_task_confimation_email(task_id, user_email):
#     subject = "Task Confimation"
#     sleep(5)
#     print("send email")
#     message = f'Your task with id {task_id} has been received is being processed.'
#     return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
