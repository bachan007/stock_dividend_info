from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def search_result(request):
    symbol = request.POST.get('stock symbol')
    return HttpResponse(symbol)
