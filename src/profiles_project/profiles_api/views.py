from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses Http method as function (get,post,put,delete)',
            'It is similar to a traditional django view',
            'Gives us the most control over logic',
            'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """crearte a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ deletes an object"""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Test api viewset """

    def list(self, request):
        """ Returns a hello message """

        a_viewset = [
            'Uses actions(list,create,retrieve,update,partial_update)',
            'automatically maps to urls using routers',
            'provides more functionality with less code'
        ]

        return Response({'message': 'hello!!!!', 'a_viewset': a_viewset})