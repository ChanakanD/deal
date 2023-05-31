from django.core.management.base import BaseCommand
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleSheets_control.models import Link, Gs, Diag,Sur, Perio, Oper, Pedo, Endo, Prosth
from googleSheets_control.management.check_cent import diag, sur, perio, oper, pedo, endo, prosth
from exchange_control.models import Exchange, Central
from api.models import User
from exchange_control.models import Central

from django.utils import timezone
from datetime import datetime, timedelta
import time
import schedule


class Command(BaseCommand):
    help = 'Load data from Google Sheets'

    def handle(self, *args, **options):

        # Schedule the function to run
        schedule.every().saturday.at("00:00").do(self.load_data)
        schedule.every().tuesday.at("00:00").do(self.cent_timeout)
        schedule.every(1).day.at("00:00").do(self.ex_timeout)

        # for test
        # schedule.every(1).minutes.do(self.load_data)
        # schedule.every(1).minutes.do(self.ex_timeout)

        # Continuously check if any scheduled functions should be run
        while True:
            schedule.run_pending()
            time.sleep(1)

    def ex_timeout(self):
        print('ex_timeout')
        exchange = Exchange.objects.filter(status='Wait')
        today = timezone.now().date()
        for ex in exchange:
            date_object = datetime.strptime(ex.stop_date, '%d/%m/%Y').date()
            if date_object < today:
                ex.status = 'Fail'
                ex.save()
                print('status: ', ex.id, ex.status)
            else: 
                pass
            
    
    def cent_timeout(self):
        print('cent_timeout')
        three_days = timezone.now() - timedelta(days=2)
        central = Central.objects.filter(post=True, timeout=True, timestamp_out__lt=three_days)
        for cent in central:
            cent.post = False
            cent.save()
            print('set post', cent.id, cent.post)


    def check_case(self):
        print('command run function2')
        one_week_ago = datetime.now() - timedelta(weeks=1)
        today = datetime.now() 
        # print(one_week_ago)
        case_cent = Central.objects.filter(post=True)

        for obj in case_cent:
            print(obj.case, obj.option)
            obj.timeout = True
            obj.save()
            
            if (obj.case == 'Diag'):
                diag.diag(obj, one_week_ago, today)
            elif (obj.case == 'Sur'):
                sur.sur(obj, one_week_ago, today)
            elif (obj.case == 'Perio'):
                perio.perio(obj, one_week_ago, today)
            elif (obj.case == 'Oper'):
                oper.oper(obj, one_week_ago, today)
            elif (obj.case == 'Pedo'):
                pedo.pedo(obj, one_week_ago, today)
            elif (obj.case == 'Endo'):
                endo.endo(obj, one_week_ago, today)
            elif (obj.case == 'Prosth'):
                prosth.prosth(obj, one_week_ago, today)

        self.cent_timeout()

    
    def load_data(self):
        print('command run')
        
        link = Link.objects.all()

        for obj in link:
            x = obj.link.split('/')
            # self.stdout.write(f'{obj.link}')
        # print(x[5])
        
        credentials = Credentials.from_service_account_file('/Users/mill/React_native/APIDeal/secret_key/deal-integrate.json')
        service = build('sheets', 'v4', credentials=credentials)

        # Load data from nameList sheet
        gs = Gs.objects.all()
        user = User.objects.all()
        sheet_id = x[5]
        sheet1_range = 'รายชื่อกลุ่ม!A2:K'

        sheet1_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet1_range).execute()
        sheet1_values = sheet1_result.get('values', [])

        if user.exists():
            print('pass')
            pass
        else:
            id = 0
            group = 0;
            for row in sheet1_values:
                if row == []:
                    # print("pass")
                    pass
                else:    
                    # print(row)
                    id += 1
                    objuser = User()
                    if row[1] == '1':
                        group += 1
                        objuser.group = group
                    else:
                        objuser.group = group
                    objuser.first_name = row[4]
                    objuser.last_name = row[5]
                    objuser.username = row[6]
                    objuser.save()

        if gs.exists():
            print('pass')
            pass
        else:
            id = 0
            group = 0;
            for row in sheet1_values:
                if row == []:
                    # print("pass")
                    pass
                else:    
                    # print(row)
                    id += 1
                    obj = Gs()
                    if row[1] == '1':
                        group += 1
                        obj.no_group = group
                    else:
                        obj.no_group = group
                    obj.first_name = row[4]
                    obj.last_name = row[5]
                    obj.stID = row[6]
                    obj.save()

        # Load data from Diag sheet
        Diag.objects.all().delete()
        sheet2_range = 'Diag!B4:M'
        sheet2_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet2_range).execute()
        sheet2_values = sheet2_result.get('values', [])

        id = 0
        for row in sheet2_values:
            if row == [] or row[0] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Diag()
                obj.first_name = row[0]
                obj.last_name = row[1]
                obj.date_update = datetime.strptime(row[3], "%m/%d/%Y")
                obj.complete = row[8]
                obj.screen = row[11]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Diag successfully.'))

        # Load data from Sur sheet
        Sur.objects.all().delete()
        sheet3_range = 'Sur!B5:H'
        sheet3_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet3_range).execute()
        sheet3_values = sheet3_result.get('values', [])

        id = 0
        for row in sheet3_values:
            if row == [] or row[0] == '' or row[3] == '-' or row[3] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Sur()
                obj.first_name = row[0]
                obj.last_name = row[1]
                obj.date_update = datetime.strptime(row[3], "%m/%d/%Y")
                obj.tooth_extraction = row[6]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Sur successfully.'))
        
        # Load data from Perio sheet
        Perio.objects.all().delete()
        sheet4_range = 'Perio!B5:CI'
        sheet4_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet4_range).execute()
        sheet4_values = sheet4_result.get('values', [])

        id = 0
        for row in sheet4_values:
            if row == [] or row[0] == '' or row[73] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Perio()
                obj.first_name = row[0]
                obj.last_name = row[1]
                obj.date_update = datetime.strptime(row[3], "%m/%d/%Y")
                obj.S = row[73]
                obj.G = row[74]
                obj.P = row[76]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Perio successfully.'))

        # Load data from Oper sheet
        Oper.objects.all().delete()
        sheet5_range = 'Oper ปี 5!B4:AB'
        sheet5_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet5_range).execute()
        sheet5_values = sheet5_result.get('values', [])

        id = 0
        for row in sheet5_values:
            if row == [] or row[0] == '' or row[17] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Oper()
                obj.first_name = row[0]
                obj.last_name = row[1]
                obj.date_update = datetime.strptime(row[3], "%m/%d/%Y")
                if row[5] == '': obj.class_I = 0
                else: obj.class_I = row[5] 
                if row[11] == '': obj.class_II = 0
                else: obj.class_II = row[11]
                if row[13] == '': obj.class_III = 0
                else: obj.class_III = row[13]
                if row[14] == '': obj.class_VI = 0
                else: obj.class_VI = row[14]
                if row[17] == '': obj.class_V = 0
                else: obj.class_V = row[17]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Oper successfully.'))

        # Load data from Pedo sheet
        Pedo.objects.all().delete()
        sheet6_range = 'Pedo!B4:W'
        sheet6_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet6_range).execute()
        sheet6_values = sheet6_result.get('values', [])

        id = 0
        for row in sheet6_values:
            if row == [] or row[0] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Pedo()
                obj.first_name = row[0]
                obj.last_name = row[2]
                obj.date_update = datetime.strptime(row[4], "%m/%d/%Y")
                if row[7] == '': obj.treatmentPlan_full = 0
                else: obj.treatmentPlan_full = row[7]
                if row[9] == '': obj.treatmentPlan_half = 0
                else: obj.treatmentPlan_half = row[9]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Pedo successfully.'))

        # Load data from Endo sheet
        Endo.objects.all().delete()
        sheet7_range = 'Endo!B4:W'
        sheet7_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet7_range).execute()
        sheet7_values = sheet7_result.get('values', [])

        id = 0
        for row in sheet7_values:
            if row == [] or row[0] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Endo()
                obj.first_name = row[0]
                obj.last_name = row[1]
                obj.date_update = datetime.strptime(row[3], "%m/%d/%Y")
                obj.teeth_sum = row[15]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Endo successfully.'))

        # Load data from Prosth sheet
        Prosth.objects.all().delete()
        sheet8_range = 'Prosth!B4:P'
        sheet8_result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet8_range).execute()
        sheet8_values = sheet8_result.get('values', [])


        import re
        id = 0
        for row in sheet8_values:
            # print(sheet8_values.index(row))

            if row == [] or row[0] == '':
                # print("pass")
                pass
            else:    
                # print(row)
                id += 1
                obj = Prosth()
                obj.first_name = row[0]
                obj.last_name = row[1]
                obj.date_update = datetime.strptime(row[3], "%m/%d/%Y")
                if row[4] == '': obj.fixed_PostCore = 0
                else: obj.fixed_PostCore = row[4]
                if row[5] == '': obj.fixed_PostCore = 0
                else: 
                    cb = re.split(', | ', row[5])
                    # print(cb)
                    if len(cb) == 2 :
                        if cb[0] == 'B': obj.fixed_CB = 1
                        elif  cb[1] == 'B': obj.fixed_CB = int(cb[0]) + 1
                    elif len(cb) > 2: obj.fixed_CB = int(cb[0])
                    elif len(cb) == 1 and cb[0] == 'B': obj.fixed_CB = 1
                    else: obj.fixed_CB = row[5]
                    # print(obj.fixed_CB)
                if row[8] == '': obj.removable_APD = 0
                else: obj.removable_APD = row[8]
                if row[9] == '': obj.removable_RPD = 0
                else: obj.removable_RPD = row[9]
                if row[11] == '': obj.double_CD = 0
                else: obj.double_CD = row[11]
                if row[12] == '': obj.single_CD = 0
                else: obj.single_CD = row[12]
                if row[13] == '': obj.contrast_CD = 0
                else: obj.contrast_CD = row[13]
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data Prosth successfully.'))

        # Format the message with the current date and time
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'Data loaded successfully at {now}!'
        self.stdout.write(self.style.SUCCESS(message))

        # Call function2 after function1 completes
        self.check_case()
