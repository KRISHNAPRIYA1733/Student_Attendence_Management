from django.shortcuts import render,get_object_or_404
from Attendence.models import StudentDb,AttendenceDb
from Attendence.serializers import StudentSerializer,AttendenceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class StudentView(APIView):
    def get(self,request):
        qs=StudentDb.objects.all()
        serializer_instance=StudentSerializer(qs,many=True)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance=StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):
    def put(self,request,pk):
        #qs=StudentDb.objects.filter(id=pk).update()
        form_data=request.data
        qs=get_object_or_404(StudentDb,id=pk)
        serializer_instance=StudentSerializer(instance=qs,data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        StudentDb.objects.get(id=pk).delete()
        return Response({"Message":"Deleted"})
      

class AttendenceView(APIView):
    def get(self,request):
        qs=AttendenceDb.objects.all()
        serializer_instance=AttendenceSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=AttendenceSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class AttndenceDetailView(APIView):
    def put(self,request,pk):
        form_data=request.data
        qs=get_object_or_404(AttendenceDb,id=pk)
        serializer_instance=AttendenceSerializer(instance=qs,data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        return Response(data=serializer_instance.data)
    def delete(self,request,pk):
        AttendenceDb.objects.get(id=pk).delete()
        return Response({"Message":"Deleted"})
#TO GET EVERY ATTENDENCE OF A PARTICULAR STUDENT
class StudentAttendanceView(APIView):
    def get(self, request, pk):
        qs = AttendenceDb.objects.filter(student_name_id=pk)
        serializer_instance = AttendenceSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
                
class DateAttendenceView(APIView):
    def get(self,request,date):
        qs=AttendenceDb.objects.filter(date=date)
        serializer_instance=AttendenceSerializer(qs,many=True)
        return Response(data=serializer_instance.data)  
class AttendencePercentageView(APIView):
    def get(self,request,pk):
        total=AttendenceDb.objects.filter(student_name_id=pk).count()
        present=AttendenceDb.objects.filter(student_name_id=pk,status='Present').count()
        student=StudentDb.objects.get(id=pk)
        if total==0:
            return Response({"Message":"Cant calculate percentage"})
        else:
            percentage=(present/total)*100
            return Response({
                            "student Name":student.stud_name,
                            "Total":total,
                             "Present":present,
                             "Attendence Percentage":round(percentage,2)})


