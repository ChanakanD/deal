from django.db.models import Q
from message_control.models import MatchEX
from exchange_control.models import Exchange, SelectedEx
def setDone(instance):
    if instance.case_match != None:
        # add case
        user_case = Exchange.objects.get(id=instance.case_match.id)
        user_case.status = instance.status
        user_case.save()
        print(user_case.id, user_case.author.id)
        print(instance.id, instance.author.id)
        matching = MatchEX.objects.filter(
            Q(author=user_case.author.id, user=instance.author.id) | Q(author=instance.author.id, user=user_case.author.id)
        )
        print(matching)
        for m in matching:
            m.case_match.remove(instance)
            m.save()
            print('remove case')
        if instance.status == 'Wait':
            instance.case_match = None
            instance.save()
            user_case.case_match = None
            user_case.save()
        else:
            pass
    else:
        # select case
        selected = SelectedEx.objects.filter(caseEx=instance.id)
        print(selected)
        
        for i in selected:
            matching = MatchEX.objects.filter(
                Q(author=i.user.id, user=instance.author.id) | Q(author=instance.author.id, user=i.user.id)
            )
            print(matching)
            for m in matching:
                m.case_match.remove(instance)
                m.save()
                print('remove case')

            sel = SelectedEx.objects.get(id=i.id)
            sel.delete()
            print('delete')
        
