from django.shortcuts import render
 
def home(request):
    return render(request,'test1/index.html')

def second(request):
    return render(request,"test1/test_app_view2.html")