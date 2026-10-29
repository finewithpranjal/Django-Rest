from rest_framework import serializers
from crudapi.models import Student

# Validators

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with "R"')
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self, value):  # This method is autometically invoked when is_valid() method is called.
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value


    # Object Level Validation <-- use this on post data
    def validate(self, data):
        nm = data.get('name')
        em = data.get('email')
        if nm.lower() == 'aarav' and em.lower() != 'aarav@gmail.com':
            raise serializers.ValidationError('Email must be aarav@gmail.com')
        return data


    # Validators  syantax def funname(value):
    '''example 
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with "R"')

    class StudentSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=100, validators=[start_with_r]) see the syntax of validators. It is a list of functions. You can add multiple validators in the list.
    
    '''