from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
# IsAuthenticatedOrReadOnly
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return Hello message"""

        as_viewset = [
            'user action (list,create,retrive,update,partial_update,destroy)',
            'Automatically maps to URLs using Routers',
            'Provide more functionality with less code',
        ]
        return Response({'message':'Hello!','as_viewset':as_viewset})

    def create(self,request):
        """Create new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handdle getting object by id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handdle updating object """
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handdle updating Part an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handdle Removing object"""
        return Response({'http_method':'DELETE'})


# class UserProfileViewSet(viewsets.ModelViewSet):
#     """Handdle creating and updating profiles"""
#     print("helo")
#     serializer_class = serializers.UserProfileSerializer
#     queryset = models.UserProfile.objects.all()

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields  = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle Creating User authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handdle creating reading and updating profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,IsAuthenticated
        # IsAuthenticatedOrReadOnly
    )

    def perform_create(self,serializer):
        """sets the user profile to logged in user """
        serializer.save(user_profile=self.request.user)
