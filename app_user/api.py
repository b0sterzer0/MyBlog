from rest_framework import status
from .models import ProfileModel
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class APIGetProfileData(APIView):
    serializer_class = ProfileSerializer
    model = ProfileModel

    def get(self, request):
        # Извлекаем набор всех записей из таблицы Writer
        # Создаём сериалайзер для извлечённого наборa записей
        serializer_for_reading = self.serializer_class(
            instance=self.model.objects.all(),  # Передаём набор записей
            many=True  # На вход подается именно набор, а не одна запись
        )
        return Response(serializer_for_reading.data)

    def post(self, request):
        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(
            data=serializer_for_writing.data,
            status=status.HTTP_201_CREATED
        )
