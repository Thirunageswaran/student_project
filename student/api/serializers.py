from rest_framework import serializers
from .models import Student, Subject

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class subject_serializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = Subject
        fields = '__all__'

    def create(self, validated_data):
        students = validated_data.pop('students')
        subject = Subject.objects.create(**validated_data)
        subject.students.set(students)
        return subject

    def update(self, instance, validated_data):
        students = validated_data.pop('students')
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        instance.students.set(students)
        return instance