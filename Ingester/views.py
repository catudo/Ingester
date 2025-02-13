from rest_framework import status


from .retrieve_from_reddit import retrieve_from_reddit

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer


class IngestView(APIView):
    def post(self, request):
        subreddit = request.GET.get('subreddit')
        subject =request.GET.get('subject')
        user = request.GET.get('user')
        count = int(request.GET.get('count'))
        retrieve_from_reddit(subreddit,subject, user, count)
        return Response({'result': 'done' }, status=status.HTTP_200_OK)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserRegister(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(request.data)  # This will call the create method in the serializer
            return Response(
                {"message": "User created successfully.", "user_id": str(user.id)},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

