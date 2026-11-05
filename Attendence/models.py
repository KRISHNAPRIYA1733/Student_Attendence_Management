from django.db import models

# Create your models here.
class StudentDb(models.Model):
    stud_name=models.CharField(max_length=100)
    roll_no=models.PositiveIntegerField(unique=True)
    class_name=models.CharField(max_length=100)

    def __str__(self):
        return self.stud_name

class AttendenceDb(models.Model):
    student_name=models.ForeignKey(StudentDb,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100,
                            choices=[('Present','Present'),
                                     ('Absent','Absent')])

    def __str__(self):
        return self.student_name.stud_name