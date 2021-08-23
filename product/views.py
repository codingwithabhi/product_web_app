from django.db.models.query_utils import Q
from django.shortcuts import render
from.models import Product
import json
# Create your views here.
def product_list(request):
    sort_by = request.GET.get("sort_by")
    max_price = request.GET.get("max_price")
    min_price = request.GET.get("min_price")
    rating = request.GET.get("rating")
    qs = Product.objects.all()
    sort_order = ""
    if sort_by:
        sort_order = "" if "-" in sort_by else "-"
        qs = qs.order_by(sort_by)
    if max_price:
        qs = qs.filter(price__lte=max_price)
    if min_price:
        qs = qs.filter(price__gte=min_price)
    try:
        rating = int(rating)
        qs = qs.filter(rating=rating)
    except TypeError:
        pass
    ctx = {"product_list": qs,"sort_order":sort_order}
    return render(request, "list.html", ctx)