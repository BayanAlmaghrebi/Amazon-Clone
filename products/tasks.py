from celery import shared_task 
import time




@shared_task
def send_emails(data):
    #for x in range(10):
     #   time.sleep(2)
      #  print(f'sending email to {x}')
    for user in data:
        send_mail(
                "Activate Your Account",
                f" Welcome {user.username} \nUse this code {profile.code} to activate your account\nMystroTeam",
                "pythondeveloper6@gmail.com",  # send from 
                [user.email],  # send to
                fail_silently=False,)