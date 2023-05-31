import random
from googleSheets_control.models import Diag
from api.models import User, Notification


def diag(obj, one_week_ago, today):
    selects = obj.selects.all()
    complete = 10
    screen = 10
    users = []
    # user_selects
    for select in selects:
        user_data = Diag.objects.filter(first_name=select.first_name, last_name=select.last_name, date_update__range=(one_week_ago, today))
        # print(select.first_name, select.last_name)
        for user in user_data:
            # print(user.first_name, user.last_name, user.date_update)
            if (obj.option == 'Complete'):
                if (user.complete < complete):
                    complete = user.complete
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.complete == complete):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Screen'):
                if (user.screen < screen):
                    screen = user.screen
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.screen == screen):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
    # print(users)
    random_index = 0
    if (len(users) > 0):
        if (len(users) > 1):
            random_index = random.randint(0, len(users) - 1)
        user = User.objects.filter(first_name=users[random_index]['first_name'], last_name=users[random_index]['last_name'])
        for u in user:
            print(u.id)
            author = User.objects.get(id=u.id)
            obj.author = author
            obj.save()
            # collect in notification
            Notification.objects.create(user_id=u.id, author_id=obj.admin.id, category="case cent", no_case=obj.no)
            print('create notification')