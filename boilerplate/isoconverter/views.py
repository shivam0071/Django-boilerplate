from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Index(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        return Response({"API": "SUCCESS"}, status=status.HTTP_200_OK)
