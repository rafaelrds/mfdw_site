from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>The Meandco Homepage</h1>")
