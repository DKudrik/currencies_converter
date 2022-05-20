from django.shortcuts import render
import requests


def hello(request):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')
    if request.method == "GET":
        context = {
            "currencies": currencies,
        }
        return render(request, 'exchange_app/index.html', context)
    if request.method == "POST":
        from_curr = request.POST.get("from-curr")
        to_curr = request.POST.get("to-curr")
        from_amount = request.POST.get("from-amount")
        context = {
            "from_curr": from_curr,
            "to_curr": to_curr,
            "currencies": currencies,
            "error": True,
        }
        if not from_amount:
            return render(request, 'exchange_app/index.html', context)
        from_amount = float(from_amount)
        converted_amount = round(currencies[to_curr]/currencies[from_curr]*from_amount, 2)
        context = {
            "from_curr": from_curr,
            "to_curr": to_curr,
            "currencies": currencies,
            "converted_amount": converted_amount,
        }
        return render(request, 'exchange_app/index.html', context)
