
from pickle import GET
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRouter(request):
    routes={
        'users':'/api/users',
        'posts/':'/api/posts',

    }
    return Response(routes)