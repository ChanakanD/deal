from django.db import models
# from api.models import User


class MatchEX(models.Model):
    author = models.ForeignKey('api.User', related_name="author_match", on_delete=models.CASCADE)
    user = models.ForeignKey('api.User', related_name="user_match", on_delete=models.CASCADE)
    case_match = models.ManyToManyField('exchange_control.Exchange', related_name="matchCase", blank=True)
    matched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.id} - {self.user.id}"


class Message(models.Model):
    sender = models.ForeignKey(
        'api.User', related_name="message_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        'api.User', related_name="message_receiver", on_delete=models.CASCADE)
    message = models.TextField(default='')
    is_read = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message between {self.sender.id} and {self.receiver.id}"



class ChatRoom(models.Model):
    users = models.ManyToManyField('api.User', related_name='chat_user')
    newMessages = models.IntegerField(blank=True, null=True)
    lastMessage = models.OneToOneField(Message, related_name="lastmessage", on_delete=models.CASCADE)
    message = models.ManyToManyField(Message, related_name="message_user",)

    def __str__(self):
        return f"user: {self.lastMessage.sender.id} {self.lastMessage.receiver.id}"