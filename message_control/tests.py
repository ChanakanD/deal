from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.
class TestMessage(APITestCase):
    message_url = "/message/messages/"

    def setUp(self):
        from api.models import User

        # sender
        self.sender = User.objects.get(username=6109610144)
        # receiver
        self.receiver = User.objects.get(username=6113600156)

    def test_post_message(self):
        payload = {
            "sender_id": self.sender.id,
            "receiver_id": self.receiver.id,
            "message": "test message"
        }

        response = self.client.post(self.message_url, data=payload)
        result = response.json()

        print(result)