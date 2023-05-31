from rest_framework import serializers
from .models import Exchange, DateTime, SelectedEx,Central, SelectedCent
from api.serializers import UserSerializer
from .check_ex import check_ex
from .matching import matching
from .setDone import setDone

class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = ('value', 'checked', 'am', 'pm')


class ExchangeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    date_time = DateTimeSerializer(many=True)

    class Meta:
        model = Exchange
        fields = "__all__"

    def create(self, validated_data):
        date_time_data = validated_data.pop('date_time')
        exchange = Exchange.objects.create(**validated_data)
        for dt_data in date_time_data:
            DateTime.objects.create(exchange=exchange, **dt_data)
        # check match case
        check_ex(exchange)

        return exchange

    def update(self, instance, validated_data):
        date_time_data = validated_data.pop('date_time')
        date_time = (instance.date_time).all()
        date_time = list(date_time)
        instance.category = validated_data.get('category', instance.category)
        instance.case_have = validated_data.get('case_have', instance.case_have)
        instance.case_want = validated_data.get('case_want', instance.case_want)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.stop_date = validated_data.get('stop_date', instance.stop_date)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.status = validated_data.get('status', instance.status)
        instance.case_match = validated_data.get('case_match', instance.case_match)
        instance.save()
        for dt_data in date_time_data:
            if date_time:
                dt = date_time.pop(0)
                dt.label = dt_data.get('label', dt.label)
                dt.value = dt_data.get('value', dt.value)
                dt.checked = dt_data.get('checked', dt.checked)
                dt.am = dt_data.get('am', dt.am)
                dt.pm = dt_data.get('pm', dt.pm)
                dt.save()
            else:
                DateTime.objects.create(case=instance, **dt_data)
        # set confirm
        setDone(instance)
        
        return instance


class SelectedExSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    caseEx = ExchangeSerializer(read_only=True)
    caseEx_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = SelectedEx
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user_id']
        caseEx = validated_data['caseEx_id']
        # add match case
        matching(user, caseEx);

        try:
            like = SelectedEx.objects.get(user=user, caseEx=caseEx)
        except SelectedEx.DoesNotExist:
            # If no Like object exists, create a new one
            like = SelectedEx.objects.create(**validated_data)
        else:
            # If a Like object exists, delete it
            like.delete()

        return like


class CentralSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    admin = UserSerializer(read_only=True)
    admin_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Central
        fields = "__all__"


class SelectedCentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    central = CentralSerializer(read_only=True)
    central_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = SelectedCent
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data['user_id']
        central = validated_data['central_id']

        # Check if a Like object already exists for the given user and post
        try:
            like = SelectedCent.objects.get(user=user, central=central)
        except SelectedCent.DoesNotExist:
            # If no Like object exists, create a new one
            like = SelectedCent.objects.create(**validated_data)
        else:
            # If a Like object exists, delete it
            like.delete()

        return like