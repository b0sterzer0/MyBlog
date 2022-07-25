from rest_framework import status
from .models import PostModel, CommentModel
from .serializers import PostModelSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect


class APIGetPostData(APIView):
    serializer_class = PostModelSerializer
    model = PostModel

    def post(self, request):
        serialized_data_for_writing = self.serializer_class(data=request.data)
        serialized_data_for_writing.is_valid()
        try:
            serialized_data_for_writing.save()
        except:
            return HttpResponseRedirect('/blog/api/posts/')
        return Response(
            data=serialized_data_for_writing.data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        queryset = PostModel.objects.select_related('author').all()
        post_serialize_data = PostModelSerializer(instance=queryset, many=True)
        return Response(post_serialize_data.data)


class APIGetCommentData(APIView):
    serializer_class = CommentSerializer
    model = CommentModel

    def post(self, request):
        serialized_data_for_writing = self.serializer_class(data=request.data)
        serialized_data_for_writing.is_valid()
        if not serialized_data_for_writing.errors():
            serialized_data_for_writing.save()
        return Response(
            data=serialized_data_for_writing.data,
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        queryset = CommentModel.objects.select_related('author', 'post').all()
        comment_serialize_data = CommentSerializer(instance=queryset, many=True)
        return Response(comment_serialize_data.data)
