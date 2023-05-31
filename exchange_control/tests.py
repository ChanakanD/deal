from django.test import TestCase
from .models import Exchange, DateTime
from api.models import User

from datetime import datetime

class MyModelTestCase(TestCase):
    @classmethod
    def setUp(cls):
        User.objects.create(
            id=1,
            username='6109610144',
            first_name='ชนากานต์',
            last_name='ดีรักษา',
            pic='http://127.0.0.1:8000/img/image4_fNOrRen.png',
            role='admin',
            group='12',
        )
        User.objects.create(
            id=2,
            username='6103618493',
            first_name='สุธินี',
            last_name='คหาปนะ',
            pic='http://127.0.0.1:8000/img/image4_fNOrRen.png',
            role='user',
            group='8',
        )
        data1 = {
            "date_time" : [
                {
                    "value": "M",
                    "checked": True,
                    "am": True,
                    "pm": True
                },
                {
                    "value": "T",
                    "checked": False,
                    "am": False,
                    "pm": False
                },
                {
                    "value": "W",
                    "checked": False,
                    "am": False,
                    "pm": False
                },
                {
                    "value": "TH",
                    "checked": False,
                    "am": False,
                    "pm": False
                },
                {
                    "value": "F",
                    "checked": True,
                    "am": True,
                    "pm": False
                }
            ],
        }
        exchange = Exchange.objects.create(
            author_id=1,
            category='Refer',
            case_have='Endo',
            case_want='Ortho',
            option='-',
            task='-',
            start_date=datetime.strptime('03/05/2023', '%d/%m/%Y').date(),
            stop_date=datetime.strptime('12/05/2023', '%d/%m/%Y').date(),
            detail='This is detail from RN.',
            status='Wait'
        )
        for date_time in data1['date_time']:
            exchange.date_time.create(
                value=date_time['value'],
                checked=date_time['checked'],
                am=date_time['am'],
                pm=date_time['pm']
        )
        
        data2 = {
            "date_time": [
                {
                    "value": "M",
                    "checked": True,
                    "am": True,
                    "pm": False
                },
                {
                    "value": "T",
                    "checked": False,
                    "am": False,
                    "pm": False
                },
                {
                    "value": "W",
                    "checked": True,
                    "am": True,
                    "pm": False
                },
                {
                    "value": "TH",
                    "checked": True,
                    "am": True,
                    "pm": False
                },
                {
                    "value": "F",
                    "checked": False,
                    "am": False,
                    "pm": False
                }
            ],
        }
        exchange = Exchange.objects.create(
            author_id=2,
            category='Refer',
            case_have='Ortho',
            case_want='Endo',
            option='-',
            task='-',
            start_date=datetime.strptime('02/05/2023', '%d/%m/%Y').date(),
            stop_date=datetime.strptime('05/05/2023', '%d/%m/%Y').date(),
            detail='This is detail from RN.',
            status='Wait'
        )
        for date_time in data2['date_time']:
            exchange.date_time.create(
                value=date_time['value'],
                checked=date_time['checked'],
                am=date_time['am'],
                pm=date_time['pm']
        )
        
        data3 = {
            "date_time": [
                {
                    "value": "M",
                    "checked": True,
                    "am": True,
                    "pm": False
                },
                {
                    "value": "T",
                    "checked": True,
                    "am": True,
                    "pm": True
                },
                {
                    "value": "W",
                    "checked": True,
                    "am": True,
                    "pm": False
                },
                {
                    "value": "TH",
                    "checked": False,
                    "am": False,
                    "pm": False
                },
                {
                    "value": "F",
                    "checked": False,
                    "am": False,
                    "pm": False
                }
            ],
        }
        exchange = Exchange.objects.create(
            author_id=2,
            category='Refer',
            case_have='Ortho',
            case_want='Endo',
            option='-',
            task='-',
            start_date=datetime.strptime('04/05/2023', '%d/%m/%Y').date(),
            stop_date=datetime.strptime('10/05/2023', '%d/%m/%Y').date(),
            detail='This is detail from RN.',
            status='Wait'
        )
        for date_time in data3['date_time']:
            exchange.date_time.create(
                value=date_time['value'],
                checked=date_time['checked'],
                am=date_time['am'],
                pm=date_time['pm']
        )



    def test_matching(self):

        exchange = Exchange.objects.all()

        for index, obj in enumerate(exchange):
            print(index)
            if (index > 0):
                self.assertEqual(exchange[0].category, exchange[index].category)
                self.assertEqual(exchange[0].case_have, exchange[index].case_want)
                self.assertEqual(exchange[0].case_want, exchange[index].case_have)
                

                if exchange[index].start_date <= exchange[0].stop_date and exchange[index].stop_date >= exchange[0].start_date:
                    print('There is an overlap in the date ranges')
                    
                    datetime_target = exchange[0].date_time.all()
                    datetime = exchange[index].date_time.all()
                    for dt_tg in datetime_target:
                       for dt in datetime:
                            if dt_tg.value == dt.value and dt_tg.checked == True and dt.checked == True:
                                print(dt_tg.value, dt_tg.checked, dt.value, dt.checked)
                                if dt_tg.am == True and dt.am == True:
                                    match = exchange[index].id
                                    print('match', match)
                                    exchange[0].status = 'Matching'
                                    exchange[index].status = 'Matching'
                                    print('author: ',exchange[0].author.id)
                                    print('user: ',exchange[index].author.id)


                                elif dt_tg.pm == True and dt.pm == True:
                                    match = exchange[index].id
                                    print('match', match)
                                    exchange[0].status = 'Matching'
                                    exchange[index].status = 'Matching'
                                    # print(exchange[0].status, exchange[index].status)
                                
                else:
                    print('There is no overlap in the date ranges')

                



            

        
