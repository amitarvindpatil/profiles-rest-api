from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """Return an list of APIView Features"""
        an_apiview = [
            'Uses Http methods as fuction (get,post,put,patch,delete)',
            'Is similer to traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped mannually to URL',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handdle updateing an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handdle a partial update of an object"""
        return Response({'method','PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method','Delete'})
