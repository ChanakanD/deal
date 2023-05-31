import random
from googleSheets_control.models import Oper
from api.models import User, Notification


def oper(obj, one_week_ago, today):
    selects = obj.selects.all()
    class_I = 7
    class_II = 3
    class_III = 2
    class_IV = 1
    class_V = 10
    users = []
    # user_selects
    for select in selects:
        user_data = Oper.objects.filter(first_name=select.first_name, last_name=select.last_name, date_update__range=(one_week_ago, today))
        # print(select.first_name, select.last_name)
        for user in user_data:
            if (obj.option == 'Complete'):
                print('complete')
            elif (obj.option == 'Class_I'):
                if (user.class_I < class_I):
                    class_I = user.class_I
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.class_I == class_I):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Class_II'):
                if (user.class_II < class_II):
                    class_II = user.class_II
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.class_II == class_II):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Class_III'):
                if (user.class_III < class_III):
                    class_III = user.class_III
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.class_III == class_III):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Class_IV'):
                if (user.class_IV < class_IV):
                    class_IV = user.class_IV
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.class_IV == class_IV):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Class_V'):
                if (user.class_V < class_V):
                    class_V = user.class_V
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.class_V == class_V):
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