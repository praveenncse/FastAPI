class EmailNotification:
    def send(self):
        print("Sending email notification")


class SMSNotification:
    def send(self):
        print("Sending SMS notification")


class PushNotification:
    def send(self):
        print("Sending push notification")  


class NotificationFactory:
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()

        
user_input=input("Enter notification type: ")

n=NotificationFactory.create_notification(user_input)
try:
    n.send()
except :
    print("Invalid notification type")

