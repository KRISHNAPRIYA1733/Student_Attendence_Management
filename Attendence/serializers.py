from rest_framework import serializers
from Attendence.models import StudentDb,AttendenceDb

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDb
        fields="__all__"
        read_only_fields=["id"]
    def validate_stud_name(self,value):
        if not value.strip():
            raise serializers.ValidationError("Name should be proper")
        return value

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AttendenceDb
        fields="__all__"
        read_only_fields=["id"]
    def validate(self,data):
        student=data.get('student_name')
        date=data.get('date')
        if AttendenceDb.objects.filter(
             student_name=student,
             date=date
        ).exists():
            raise serializers.ValidationError("Not valid")
        return data