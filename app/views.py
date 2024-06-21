from django.shortcuts import render
from django.http import HttpResponse

data = {
    "intro": "Homepage",
}

greeting = {
    "greeting": 1,
}

steps = [
        {
            'title': 'Step 1: Inquiry',
            'description': 'Contact us to learn more about Greenfield Academy and schedule a tour of our campus. Our admissions team is here to answer your questions and provide information about our programs.'
        },
        {
            'title': 'Step 2: Application',
            'description': 'Complete the application form and submit the required documents. This includes academic records, recommendation letters, and a personal statement from the student.'
        },
        {
            'title': 'Step 3: Interview',
            'description': 'Attend an interview with our admissions committee. This is an opportunity for us to get to know the student and for the student to learn more about our school community.'
        },
        {
            'title': 'Step 4: Decision',
            'description': 'After reviewing your application and interview, we will notify you of our decision. Successful applicants will receive an acceptance letter and information on the next steps.'
        }
    ]

def home(request):
    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html")

def programs(request):
    return render(request,"programs.html",greeting)

def admissions(request):
    return render(request,"admissions.html",{"data" :steps})

def contact(request):
    return render(request,"contact.html")



# Create your views here.
