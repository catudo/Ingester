from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .retrieve_from_reddit import retrieve_from_reddit


class IngestView(APIView):
    def post(self, request):
        subreddit = request.GET.get('subreddit')
        subject =request.GET.get('subject')
        user = request.GET.get('user')
        count = int(request.GET.get('count'))
        retrieve_from_reddit(subreddit,subject, user, count)
        return Response({'result': 'done' }, status=status.HTTP_200_OK)
