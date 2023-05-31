import random
from googleSheets_control.models import Sur
from api.models import User, Notification


def sur(obj, one_week_ago, today):
    selects = obj.selects.all()
    tooth = 13
    users = []
    # user_selects
    for select in selects:
        user_data = Sur.objects.filter(first_name=select.first_name, last_name=select.last_name, date_update__range=(one_week_ago, today))
        # print(select.id)
        for user in user_data:
            # print(user.first_name, user.last_name, user.date_update)
            if (obj.option == 'Complete'):
                print('complete')
            elif(obj.option == 'Surendo'):
                if (user.tooth_extraction < tooth):
                    tooth = user.tooth_extraction
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.tooth_extraction == tooth):
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