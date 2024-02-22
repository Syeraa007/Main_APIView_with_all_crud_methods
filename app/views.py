from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class ProductCrud(APIView):
    def get(self, request, pid):
        PQS = Product.objects.filter(product_id = pid)
        # PQS = Product.objects.all()
        serializer = ProductSerializer(PQS, many = True)
        return Response(serializer.data)

    def post(self, request, pid):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success' : 'Data saved successfully'}, status = status.HTTP_201_CREATED)
        return Response({'Failure' : 'Invalid data'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pid):
        PQO = Product.objects.get(product_id = pid)
        serializer = ProductSerializer(PQO, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Success' : 'Product data "{}" updated successfully.'.format(PQO.product_name)}, status = status.HTTP_202_ACCEPTED)
        return Response({'Failure' : 'Invalid data'}, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pid):
        data = request.data
        PQO = Product.objects.get(product_id = pid)
        PQO.product_name = data['product_name']
        PQO.save()
        return Response({'Success' : 'Product data "{}" partially updated successfully.'.format(PQO.product_name)}, status = status.HTTP_202_ACCEPTED)

    def delete(self, request, pid):
        PQO = Product.objects.get(product_id = pid)
        PQO.delete()
        return Response({'Success' : 'Product data "{}" deleted successfully.'.format(PQO.product_name)}, status = status.HTTP_200_OK)