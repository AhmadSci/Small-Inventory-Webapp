import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Item
from .forms import ItemForm, UpdateItemForm

# Create your views here.


def home_view(request):
    # get all items
    items = Item.objects.all().order_by("-id")
    return render(request, "inventory/home.html", {"items": items})

def add_item_view(request):
    if request.method == "POST":
        print(request.body)
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            name = body["name"]
            quantity = body["quantity"]
            price = body["price"]
            description = body["description"]
            item = Item(name=name, quantity=quantity, price=price, description=description)
            item.save()
            return JsonResponse({"message": "Item added successfully"}, status=201)
        except:
            return JsonResponse({"error": "Invalid data"}, status=400)
            
    else:
        form = ItemForm()
    return render(request, "inventory/add.html", {"form": form})

def update_item_view(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            quantity = body["quantity"]
            price = body["price"]
            item.quantity = quantity
            item.price = price
            item.save()
            print(item.price , item.quantity)
            return JsonResponse({"message": "Item added successfully"}, status=201)
        except:
            return JsonResponse({"error": "Invalid data"}, status=400)

def delete_item_view(request, id):
    pass

def remove_item_view(request):
    pass