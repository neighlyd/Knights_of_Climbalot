from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html', {})

def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
