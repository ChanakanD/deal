from django.db.models import Q, Prefetch
from datetime import datetime
from .models import Exchange
from api.models import User, Notification
from message_control.models import Message, MatchEX, ChatRoom


def check_ex(exchange):
    exchange_case = Exchange.objects.exclude(id=exchange.id).filter(category=exchange.category, status='Wait')
    matching = False
    if exchange.status == 'Matching':
        print('Matched')
        pass
    else:
        print('check ex' )
        for obj in exchange_case:
            print(obj.id, obj.category)
            if exchange.case_have == obj.case_want or exchange.option != obj.option:
                print('match case_have')
                if exchange.case_want == obj.case_have and exchange.task == obj.task:
                    print('match case_want')
                    start_date1 = datetime.strptime(obj.start_date, '%d/%m/%Y')
                    end_date1 = datetime.strptime(obj.stop_date, '%d/%m/%Y')
                    start_date2 = datetime.strptime(exchange.start_date, '%d/%m/%Y')
                    end_date2 = datetime.strptime(exchange.stop_date, '%d/%m/%Y')
                    if start_date1 <= end_date2 and end_date1 >= start_date2:
                        print('There is an overlap in the date ranges')
                        datetime_target = exchange.date_time.all()
                        datetime_dt = obj.date_time.all()
                        for dt_tg in datetime_target:
                            for dt in datetime_dt:
                                if dt_tg.value == dt.value and dt_tg.checked == True and dt.checked == True and matching == False:
                                    print(dt_tg.value, dt_tg.checked, dt.value, dt.checked)
                                    if dt_tg.am == True and dt.am == True:
                                        match = obj.id
                                        print('match case: ', match)
                                        exchange.status = 'Matching'
                                        obj.status = 'Matching'
                                        exchange.case_match = obj
                                        obj.case_match = exchange
                                        exchange.save()
                                        obj.save()
                                        matching = True
                                        # matching user and send message
                                        send_message(obj, exchange)
                                    elif dt_tg.pm == True and dt.pm == True and obj.status != 'Matching':
                                        match = obj.id
                                        print('match case: ', match)
                                        exchange.status = 'Matching'
                                        obj.status = 'Matching'
                                        exchange.case_match = obj
                                        obj.case_match = exchange
                                        exchange.save()
                                        obj.save()
                                        matching = True
                                        # matching user and send message
                                        send_message(obj, exchange)
                                    else: pass
                                else: pass
                    else: pass
                else: pass   
            else: pass

def send_message(obj, exchange):
    print('list id: ', exchange.author.id, obj.author.id)
    # add matching
    matching = MatchEX.objects.filter(
        Q(author=exchange.author.id, user=obj.author.id) | Q(author=obj.author.id, user=exchange.author.id)
    )
    print(matching)
    if matching.exists():
        print('non empty')
        # add case in MatchEx
        matching[0].case_match.add(obj)
        print('add matching finish')
        # send first message
        message = Message.objects.create(
            sender_id = exchange.author.id, 
            receiver_id = obj.author.id, 
            message = 'Hi',
            is_read = False,
        )
        # add message to ChatRoom
        chat_room = ChatRoom.objects.filter(users__id__exact=exchange.author.id).filter(users__id__exact=obj.author.id)
        print(chat_room)
        chat = ChatRoom.objects.get(id=chat_room[0].id)
        chat.newMessages += 1
        chat.lastMessage = message
        chat.message.add(message.id)
        chat.save()
        # collect in notification
        Notification.objects.create(user_id=obj.author.id, author_id=exchange.author.id, category="new match", no_case="-")
        print('create notification')
    else:
        # ChatRoom.objects.all().delete()
        # Message.objects.all().delete()
        print('empty')
        # create MatchEx
        match_case = MatchEX.objects.create(author_id=exchange.author.id, user_id=obj.author.id)
        print(match_case)
        match_case.case_match.add(obj)
        print('add matching finish')
        # add friend for send message
        author_case = User.objects.get(id=exchange.author.id)
        user_case = User.objects.get(id=obj.author.id)
        author_case.friends.add(user_case.id)
        user_case.friends.add(author_case.id)
        print('add friend finish')
        # send first message
        message = Message.objects.create(
            sender_id = exchange.author.id, 
            receiver_id = obj.author.id, 
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
        Notification.objects.create(user_id=obj.author.id, author_id=exchange.author.id, category="new match", no_case="-")
        print('create notification')


