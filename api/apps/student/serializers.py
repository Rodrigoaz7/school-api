from rest_framework import serializers
from .models import Student
from utils import students as utilsStudents
from schoolClass.models import Class

class StudentSerializer(serializers.ModelSerializer):
    date_birth = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'date_birth', 'registration', 'school_class')


class StudentPersistSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    date_birth = serializers.DateField(required=True)
    school_class = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), required=False)

    # custom validation
    def validate(self, data):
        if Student.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already Exists'})
        return data

    def create(self):
        self.validated_data['registration'] = utilsStudents.generateRegistration()
        return Student.objects.create(**self.validated_data)