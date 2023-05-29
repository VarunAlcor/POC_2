from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import status
from .filters import CommonCustInfo_filter
from django.db.models.functions import Collate
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework import filters
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

# Create your views here.
# Read
@api_view(['GET'])
def home(request):
    Customer_obj=CommonCustInfo.objects.all() #queryset
    serializer=CommonCustInfoSerializer(Customer_obj, many=True)
    return Response(serializer.data)

#create
@api_view(['POST'])
def post_Customer(request):
    #Customer_obj=Customer.objects.all() 
    serializer=CommonCustInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


#update
@api_view(['POST'])
def update_Customer(request,pk):
    Customer_obj=CommonCustInfo.objects.get(pk=pk) #queryset
    serializer=CommonCustInfoSerializer(instance=Customer_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#delete
@api_view(["DELETE"])
def delete_customer(request, pk =None):
    if request.method == 'DELETE':
        pk = pk
        cust = CommonCustInfo.objects.get(pk=pk)
        cust.delete()
    return Response({'msg':'Delete Sucessfully'})

        

#search and filter
@api_view(['GET'])
def search_list(request):
    queryset = CommonCustInfo.objects.all()
    serializer_class = CommonCustInfoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CommonCustInfo_filter

    # Apply filters to the queryset
    filtered_queryset = filterset_class(
        data=request.query_params,
        queryset=queryset,
        request=request
    ).qs

    # Apply search filter to the queryset
    search_term= request.query_params.get('search',None)
    starts_with_letter = request.query_params.get('starts_with', None)
    ends_with_letter = request.query_params.get('ends_with', None)

    if starts_with_letter is not None:
        filtered_queryset = filtered_queryset.filter(first_name_kana__istartswith=starts_with_letter)
    
    elif ends_with_letter is not None:
        filtered_queryset = filtered_queryset.filter(first_name_kana__iendswith=ends_with_letter)
    elif search_term is not None:

        filtered_queryset = filtered_queryset.filter(
            Q(first_name_kanji__icontains=search_term) |
            Q(last_name_kanji__icontains=search_term) |
            Q(first_name_kana__icontains=search_term) |
            Q(last_name_kana__icontains=search_term) |
            Q(gender__icontains=search_term) |
            Q(dob__icontains=search_term) |
            Q(phone_area_code__icontains=search_term) |
            Q(phone_local_area_code__icontains=search_term) |
            Q(phone_no__icontains=search_term) |
            Q(cellphone_no1__icontains=search_term) |
            Q(cellphone_no2__icontains=search_term) |
            Q(cellphone_no3__icontains=search_term) |
            Q(email_pc__icontains=search_term) |
            Q(email_opt_flag__icontains=search_term)
        )

        #filtered_queryset = filtered_queryset.order_by('日本語の苗字')

    # Serialize the filtered queryset
    serializer = serializer_class(filtered_queryset, many=True)
    return Response(serializer.data)


  


 












