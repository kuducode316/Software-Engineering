from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page(request):
    context=[
    {
        "FirstName" : "أحمد",
        "LastName" : "الهاشمي",
        "Age" : 21,
        "Gender" : "ذكر",
        "Level" : "السنة الثالثة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "محمد",
        "LastName" : "الحضرمي",
        "Age" : 22,
        "Gender" : "ذكر",
        "Level" : "السنة الرابعة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "ليلى",
        "LastName" : "الشريف",
        "Age" : 19,
        "Gender" : "أنثى",
        "Level" : "السنة الأولى",
        "Status" : "نعم"
    },
    {
        "FirstName" : "فهد",
        "LastName" : "القاسمي",
        "Age" : 23,
        "Gender" : "ذكر",
        "Level" : "السنة الخامسة",
        "Status" : "لا"
    },
    {
        "FirstName" : "سارة",
        "LastName" : "الزهري",
        "Age" : 20,
        "Gender" : "أنثى",
        "Level" : "السنة الثانية",
        "Status" : "نعم"
    },
    {
        "FirstName" : "عبدالله",
        "LastName" : "النعيمي",
        "Age" : 24,
        "Gender" : "ذكر",
        "Level" : "السنة الخامسة",
        "Status" : "لا"
    },
    {
        "FirstName" : "مريم",
        "LastName" : "العسيري",
        "Age" : 18,
        "Gender" : "أنثى",
        "Level" : "السنة الأولى",
        "Status" : "نعم"
    },
    {
        "FirstName" : "خالد",
        "LastName" : "المري",
        "Age" : 22,
        "Gender" : "ذكر",
        "Level" : "السنة الرابعة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "هدى",
        "LastName" : "القرشي",
        "Age" : 21,
        "Gender" : "أنثى",
        "Level" : "السنة الثالثة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "بدر",
        "LastName" : "التميمي",
        "Age" : 23,
        "Gender" : "ذكر",
        "Level" : "السنة الخامسة",
        "Status" : "لا"
    }
]
    return render(request,'webPage.html',{"students":context})

def home(request):
    name='Abdulrahman'
    return render(request,'home.html',{"yourName":name})

def read(request):
    # return HttpResponse('<h1 style="color:blue;">All Students ')
    return render(request,'allStudent.html')



def read_one(request):
    # return HttpResponse('<h1 style="color:blue;">One Student')
    context={
        "name":"Abdulrahman",
        "marks":[90,93,92],
        "subjects":{
            "SW":99,
            "CS":96,
            "CO":85,
            "CG":96

        },
        "age":24,
        "GPA":95
    }
    return render(request,'student_one.html',context)


def create(request):
    return HttpResponse('<h1 style="color:blue;">Student Created')

def update(request):
    return HttpResponse('<h1 style="color:blue;">Student updated')
def delete(request):
    return HttpResponse('<h1 style="color:blue;">Student deleted')