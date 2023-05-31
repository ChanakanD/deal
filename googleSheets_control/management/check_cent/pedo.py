import random
from googleSheets_control.models import Pedo
from api.models import User, Notification


def pedo(obj, one_week_ago, today):
    selects = obj.selects.all()
    treatmentPlan_full = 2
    treatmentPlan_half = 2
    users = []
    # user_selects
    for select in selects:
        user_data = Pedo.objects.filter(first_name=select.first_name, last_name=select.last_name, date_update__range=(one_week_ago, today))
        # print(select.first_name, select.last_name)
        for user in user_data:
            # print(user.complete, user.screen)
            if (obj.option == 'Complete'):
                if (user.treatmentPlan_full < treatmentPlan_full):
                    treatmentPlan_full = user.treatmentPlan_full
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.treatmentPlan_full == treatmentPlan_full):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Screen'):
                if (user.treatmentPlan_half < treatmentPlan_half):
                    treatmentPlan_half = user.treatmentPlan_half
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.treatmentPlan_half == treatmentPlan_half):
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