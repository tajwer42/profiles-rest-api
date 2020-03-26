from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
            'Uses Http method as function (get,post,put,delete)',
            'It is similar to a traditional django view',
            'Gives us the most control over logic',
            'Is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})