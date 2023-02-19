from django.shortcuts import render
from django.http import HttpResponse
from .scripts.symbol_info import get_company_info

# Create your views here.
def homepage(request):
    print("Calling homepage \n")
    return render(request,'index.html')

def search_result(request):
    # print('calling search result \n')
    symbol = request.GET.get("stock symbol")
    print(f"symbol : {symbol}")
    if request.method=='GET':
        symbol = request.GET.get('stock symbol')
        company_dividend_info = get_company_info(symbol.upper())
        print(type(company_dividend_info))
        if type(company_dividend_info) is dict:
            return render(request, 'search_result.html',{"symbol":symbol,"company":company_dividend_info})
        else:
            print(f"error : {company_dividend_info}")
            return HttpResponse(f"{company_dividend_info}")
