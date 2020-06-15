from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.person.models import Person
from api.person.serializers import PersonSerializer


class LatestBorderCrossersView(APIView):

    def get(self, request):
        # limit wasn't discuss in tech task so it's only mine initiative
        queryset = Person.objects.all().order_by('-border_crosses__date_of_border_cross')[:10]
        serialized = PersonSerializer(queryset, many=True)
        return Response(serialized.data)


class CreatePersonView(APIView):
    serializer_class = PersonSerializer

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
