from rest_framework import serializers
from crudapi.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # roll = serializers.IntegerField(read_only=True)

    '''
    example : Validation using validators
           
            def email_ends_with_@gmail.com(value):
                if not value.endswith('@gmail.com'):
                    raise serializers.ValidationError("Email must end with @gmail.com.")'''
    
    # email = serializers.EmailField(validators=[email_ends_with_@gmail.com])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'email']
        # read_only_fields = ['roll', 'email']  # This will make the roll and email fields read-only

'''for validation we can use the following methods in serializer class
   for field vlalidation use the same as serializer class in drf3

   example : Feild level validation

       def validate_roll(self, value):
           if value < 0:
               raise serializers.ValidationError("Roll number must be a positive integer.")
           return value

    for  validation use the following method in serializer class


    example : Object level validation
    
        def validate(self, data):
            nm = data.get('name')
            em = data.get('email')
            if nm.lower() == 'admin' and em.lower() == 'admin@example.com':
                raise serializers.ValidationError("Admin user is not allowed.")
            return data

    
    
'''