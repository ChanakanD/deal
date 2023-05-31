from django.db.models import Q
from .models import Exchange
from api.models import User, Notification
from message_control.models import Message, MatchEX, ChatRoom


def matching(user, caseEx):
    print(user, caseEx)
    exchange = Exchange.objects.get(id=caseEx)
    matching = MatchEX.objects.filter(
        Q(author=exchange.author.id, user=user) | Q(author=user, user=exchange.author.id)
    )
    print(matching)
    if matching.exists():
        print('non empty')
        for match in matching:
            # add case in MatchEx
            match.case_match.add(caseEx)
            print('add matching finish')
            # send first message
            message = Message.objects.create(
                sender_id = user, 
                receiver_id = exchange.author.id, 
                message = 'Hi',
                is_read = False,
            )
            # add message to ChatRoom
            chat_room = ChatRoom.objects.filter(users__id__exact=exchange.author.id).filter(users__id__exact=user)
            print(chat_room)
            chat = ChatRoom.objects.get(id=chat_room[0].id)
            chat.newMessages += 1
            chat.lastMessage = message
            chat.message.add(message.id)
            chat.save()
            # collect in notification
            Notification.objects.create(user_id=exchange.author.id, author_id=user, category="new match", no_case="-")
            print('create notification')
    else:
        # ChatRoom.objects.all().delete()
        # Message.objects.all().delete()
        print('empty')
        # create MatchEx
        match_case = MatchEX.objects.create(author_id=user, user_id=exchange.author.id)
        print(match_case)
        match_case.case_match.add(caseEx)
        print('add matching finish')
        # add friend for send message
        author_case = User.objects.get(id=user)
        user_case = User.objects.get(id=exchange.author.id)
        author_case.friends.add(user_case.id)
        user_case.friends.add(author_case.id)
        print('add friend finish')
        # send first message
        message = Message.objects.create(
            sender_id = user, 
            receiver_id = exchange.author.id, 
            message = 'Hi',
            is_read = False,
        )
        print('send message')
        # create ChatRoom
        chat_room = ChatRoom.objects.create(newMessages=1, lastMessage_id=message.id)
        chat_room.users.add(author_case)
        chat_room.users.add(user_case)
        chat_room.message.add(message.id)
        # collect in notification
        Notification.objects.create(user_id=exchange.author.id, author_id=user, category="new match", no_case="-")
        print('create notification')
