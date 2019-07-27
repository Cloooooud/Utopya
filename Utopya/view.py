from django.shortcuts import render
 
def hello(request):
    context          = {}
    return render(request, 'main.html', context)

def teacher_login(request):
    context         ={}
    return render(request, 'login_page.html',context)

def select_page(request):
    context         ={}
    return render(request, 'split.html',context)

def grades_upload(request):
    context         ={}
    return render(request, 'grades_upload.html',context)

def Home_page_class_profile(request):
    context         ={}
    return render(request, 'Home_page_class_profile.html',context)

def students_profile(request):
    context         ={}
    return render(request, 'students_profile.html',context)