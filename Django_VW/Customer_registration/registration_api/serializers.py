from rest_framework import serializers
from .models import *
from django import forms
from datetime import datetime


class CommonCustInfoSerializer(serializers.ModelSerializer):
    #dob=serializers.CharField(validators=[validate_dob])

    class YourSerializer(serializers.ModelSerializer):
        dob = serializers.DateField(input_formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.000Z"])

    def validate_dob(self, dob):
        try:
            date_obj = datetime.strptime(str(dob), '%Y-%m-%d')
        except ValueError:
            try:
                date_obj = datetime.strptime(str(dob), '%Y-%m-%dT%H:%M:%S.000Z')
            except ValueError:
                raise serializers.ValidationError("Invalid date format. Use one of these formats instead: YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS.000Z")
        
        return date_obj.strftime('%Y-%m-%d')








    
    """ class YourSerializer(serializers.ModelSerializer):
    # assuming you have a field named `date_field` in your model
        dob = serializers.DateField(input_formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.000Z"])


    def validate(self, data):
        # validate date format
        try:
            datetime.strptime(data['date_field'], '%Y-%m-%dT%H:%M:%S.000Z')
        except ValueError:
            raise serializers.ValidationError("Invalid date format")

        # change date format to %y-%m-%d and update data dict
        date_obj = datetime.strptime(data['date_field'], '%Y-%m-%dT%H:%M:%S.000Z')
        data['date_field'] = date_obj.strftime('%y-%m-%d')
        return data """
    
    class Meta:
        model=CommonCustInfo
        fields='__all__'

        
    
    """ def validate_dob(self, value):
            print (value.date())
            try:
                print(value, "Hello")
                datetime.strptime(str(value), '%Y-%m-%dT%H:%M:%S.000Z')
            except ValueError:
                raise serializers.ValidationError('Invalid date format')
            print (value.date())    

            return value.date() """




    


