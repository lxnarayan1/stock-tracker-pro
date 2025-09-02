from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import FavouriteStock
from django.http import JsonResponse
from . import functionality
from django.urls import reverse
from django.contrib.auth.models import User

def home(request):
    return render(request, "index.html")

def stock_detail(request):
    symbol = request.GET.get("symbol")

    if not symbol:
        return render(request, "stock_info.html", {"error": "No stock symbol provided"})

    stock = functionality.get_stock_quote(symbol)
    company = functionality.get_company_overview(symbol)

    if not stock:
        return render(request, "stock_info.html", {"error": "Invalid stock symbol"})

    context = {"stock": stock, "company": company}
    return render(request, "stock_info.html", context)

def autocomplete(request):
    query = request.GET.get("q", "")
    if not query:
        return JsonResponse([], safe=False)

    suggestions = functionality.search_symbols(query)
    return JsonResponse(suggestions, safe=False)

@login_required
def add_to_favourites(request, symbol):
    FavouriteStock.objects.get_or_create(
        user=request.user, 
        symbol=symbol.upper()
    )
    
    return redirect(f"{reverse('stock_detail')}?symbol={symbol}")

@login_required
def favourites_list(request):
    favourites = FavouriteStock.objects.filter(user=request.user)
    stocks = []

    for fav in favourites:
        stock = functionality.get_stock_quote(fav.symbol)
        if stock:
            stocks.append(stock)

    return render(request, "favourites.html", {"stocks": stocks})

@login_required
def remove_from_favourites(request, symbol):
    FavouriteStock.objects.filter(user=request.user, symbol=symbol.upper()).delete()
    return redirect(reverse("favourites"))

@login_required
def profile_view(request):
    if request.method == "POST":
       
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")

    return render(request, "profile.html", {"user": request.user})
