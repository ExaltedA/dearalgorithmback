from core.models import *
from core.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class PostList(APIView):
    def get(self, request, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
