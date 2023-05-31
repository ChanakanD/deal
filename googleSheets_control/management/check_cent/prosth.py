import random
from googleSheets_control.models import Prosth
from api.models import User, Notification


def prosth(obj, one_week_ago, today):
    selects = obj.selects.all()
    fixed_PostCore = 1
    fixed_CB = 2
    removable_APD = 1
    removable_RPD = 3
    double_CD = 2
    single_CD = 2
    contrast_CD = 2
    users = []
    # user_selects
    for select in selects:
        user_data = Prosth.objects.filter(first_name=select.first_name, last_name=select.last_name, date_update__range=(one_week_ago, today))
        # print(select.first_name, select.last_name)
        for user in user_data:
            # print(user.complete, user.screen)
            if (obj.option == 'Fixed_PostCore'):
                if (user.fixed_PostCore < fixed_PostCore):
                    fixed_PostCore = user.fixed_PostCore
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.fixed_PostCore == fixed_PostCore):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Fixed_CB'):
                if (user.fixed_CB < fixed_CB):
                    fixed_CB = user.fixed_CB
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.fixed_CB == fixed_CB):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Removable_APD'):
                if (user.removable_APD < removable_APD):
                    removable_APD = user.removable_APD
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.removable_APD == removable_APD):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Removable_RPD'):
                if (user.removable_RPD < removable_RPD):
                    removable_RPD = user.removable_RPD
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.removable_RPD == removable_RPD):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Double_CD'):
                if (user.double_CD < double_CD):
                    double_CD = user.double_CD
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.double_CD == double_CD):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Single_CD'):
                if (user.single_CD < single_CD):
                    single_CD = user.single_CD
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.single_CD == single_CD):
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
            elif (obj.option == 'Contrast_CD'):
                if (user.contrast_CD < contrast_CD):
                    contrast_CD = user.contrast_CD
                    # print(user.id)
                    if (len(users) >= 1):
                        del users[len(users) - 1]
                    users.append({
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    })
                elif (user.contrast_CD == contrast_CD):
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