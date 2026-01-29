from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    # student_list=Student.objects.all()
    # student_list=Student.objects.filter(marks__gte=35)
    # student_list=Student.objects.filter(marks__lt=35)
    # student_list=Student.objects.filter(marks__range=(60,100))
    # student_list=Student.objects.filter(name__startswith='R')
    # student_list=Student.objects.filter(name__endswith='t')
    # student_list=Student.objects.filter(address__contains='r')
    # student_list=Student.objects.filter(address__icontains='T')
    # student_list=Student.objects.filter(email__iexact='abc@gmail.com')
    # student_list=Student.objects.all().order_by('marks')
    # student_list=Student.objects.all().order_by('-name')
    student_list=Student.objects.all().order_by('name')
    my_dict={'s_list':student_list}
    return render(request,template_name='testapp/stud.html',context=my_dict)