from rest_framework import serializers
from .models import Student
from utils import students as utilsStudents

class StudentSerializer(serializers.ModelSerializer):
    date_birth = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'date_birth', 'registration')


class StudentPersistSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    date_birth = serializers.DateField(required=True)

    def create(self):
        self.validated_data['registration'] = utilsStudents.generateRegistration()
        return Student.objects.create(**self.validated_data)
    
    def update(self):
        student = Student.objects.filter(pk=self.validated_data['pk']).update(**self.validated_data)
        return Student.objects.get(pk=student.pk)