from rest_framework import status
from .retrieve_from_reddit import retrieve_from_reddit

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

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

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)