from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import Inventory, MasterInventory, RemainingInventory
from .serializers import InventorySerializer, MasterInventorySerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


@login_required(login_url='/login/')
def inventory_add(request):
    if request.method == 'POST':
        crop_type_pk = request.POST.get('crop_type')
        crop_price_per_kg = request.POST.get('crop_price_per_kg')
        crop_quantity = request.POST.get('crop_quantity')
                
        crop_type = MasterInventory.objects.get(pk=crop_type_pk)


        last_inventory_record = Inventory.objects.filter(crop_type=crop_type).last()
        print(last_inventory_record)
# If the last inventory record is not None, then store the crop_quantity value in the total_crops variable.
        if last_inventory_record:
             total_crops = last_inventory_record.crop_quantity
             total_crops = int(total_crops)
             print("||||||||||||||||||||||||||||||||||")
             print(total_crops)
             crop_quantity = int(crop_quantity)
             total_crops += crop_quantity
             print(total_crops)
        else:
            total_crops = int(crop_quantity)

        inventory = Inventory()
        inventory.crop_type = crop_type
        inventory.crop_price_per_kg = crop_price_per_kg
        inventory.crop_quantity = crop_quantity
        inventory.add_or_remove = "Add"
        inventory.total_crops = total_crops
    
        inventory.save()
        remaining_inventory = RemainingInventory.objects.filter(inventory_item_id=inventory.crop_type).first()
        print(99999999999999999999999999999999)
        print(remaining_inventory)
        # If the existing remaining inventory is not None, then add the new crop quantity to the existing remaining inventory and update the database.
        if remaining_inventory:
            remaining_inventory.total_quantity += int(crop_quantity)
            remaining_inventory.save()

            # Save the inventory object again to update the crop_quantity field.
            inventory.save()
        else:
            # Create a new remaining inventory object and save it to the database.
            remaining_inventory = RemainingInventory()
            remaining_inventory.inventory_item = crop_type
            remaining_inventory.total_quantity = crop_quantity
            remaining_inventory.save()

        return redirect('inventory_list')
    else:
        crop_types = MasterInventory.objects.all()
        return render(request, 'inventory_add.html', {'crop_types': crop_types})


def inventory_update(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    if request.method == 'POST':
        crop_type = request.POST.get('crop_type')
        crop_price_per_kg = request.POST.get('crop_price_per_kg')
        crop_quantity = request.POST.get('crop_quantity')

        inventory.crop_type = crop_type
        inventory.crop_price_per_kg = crop_price_per_kg
        inventory.crop_quantity = crop_quantity
        inventory.save()

        # Update RemainingInventory total_quantity
        remaining_inventory = RemainingInventory.objects.get(inventory_item=inventory)
        remaining_inventory.total_quantity = crop_quantity
        remaining_inventory.save()

        return redirect('inventory_list')
    else:
        crop_types = MasterInventory.objects.all()
        return render(request, 'inventory/inventory_update.html', {'inventory': inventory, 'crop_types': crop_types})

def inventory_delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()

    # Delete RemainingInventory
    remaining_inventory = RemainingInventory.objects.get(inventory_item=inventory)
    remaining_inventory.delete()

    return redirect('inventory_list')

def remaining_inventory_list(request):
    remaining_inventories = RemainingInventory.objects.all()

    # Create a dictionary to store the total quantity for each crop type.
    total_quantities = {}

    # Iterate over the remaining inventories and calculate the total quantity for each crop type.
    for remaining_inventory in remaining_inventories:
        crop_type = remaining_inventory.inventory_item.crop_type
        total_quantity = total_quantities.get(crop_type, 0)
        total_quantity += remaining_inventory.total_quantity
        total_quantities[crop_type] = total_quantity

    # Pass the total quantities dictionary to the template.
    return render(request, 'remaining_inventory_list.html', {'total_quantities': total_quantities})


def allAddInventory(request):
    inventoryList = Inventory.objects.filter(add_or_remove="Add") 
    serializer = InventorySerializer(inventoryList, many = True)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


    
class Crop(APIView):
    def get(self, request):
        try:
            crops = MasterInventory.objects.all()
            serializer = MasterInventorySerializer(crops, many=True)
            # crop_names = [crop_data['name'] for crop_data in serializer.data]
            # print(crop_names)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Handle any unexpected exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except MasterInventory.DoesNotExist:
            # Handle specific exception for MasterInventory objects not found
            return Response({'message': 'No crop types found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle any remaining exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request):
        print(request.data["crop_type"]);
        print(request.data["quantity"]);
        
        try:
            print(request.data)
            # serializer = MasterInventorySerializer(data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            return Response({"message": "Post Successfully"}, status=status.HTTP_201_CREATED)
            # else:
            #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Insert Valid Data"}, status=status.HTTP_400_BAD_REQUEST)
     