from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """Return an list of APIView Features"""
        an_apiview = [
            'Uses Http methods as fuction (get,post,put,patch,delete)',
            'Is similer to traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped mannually to URL',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
