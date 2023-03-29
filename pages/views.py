from django.shortcuts import render,HttpResponse

# Create your views here.
def HomepageView(request):
    return HttpResponse("Hello Word!")