from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import name_serializer

class details(APIView):
    def post(self,request):
        serial=name_serializer(data=request.data);
        if(serial.is_valid()):
            serial.save()
            return Response({"message":"suessfully add to database!!","data":serial.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        
        age=request.data.get("age")
        if age>0:
            querys=CustomUser.objects.filter(age=age)
            serial=name_serializer(querys,many=True)
            if serial:
                print(serial.data)
                return Response(serial.data,status=status.HTTP_200_OK)
            else:
                return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST) 
        return Response({"message":"error"},status=404)
######################################################################







