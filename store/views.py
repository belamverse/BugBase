from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .serializers import RepositorySerializer, BugSerializer
from .models import Bug, Repository

class ListUserRepos(APIView):

    def get(self, request):
        user = request.user

        access_token = getattr(user, 'github_access_token', None)

        if not access_token:
            return Response({'error':'Missing tokens'}, status=status.HTTP_404_NOT_FOUND)

        url = 'https://api.github.com/user/repos'
        headers = {
            'Authorization': f"Bearer {access_token}",
             'Accept': 'application/vnd.github+json'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Failed to fetch repos",
                "status_code": response.status_code,
                "message": response.text
            }, status=response.status_code)
        
class ImportRepositoryView(APIView):

    def post(self, request):
        name = request.data.get('name')
        owner =request.data.get('owner')
        gihub_url = request.data.get('github_url')

        repo, created = Repository.objects.create(
            name=name,
            owner=owner,
            github_url=gihub_url
        )

        if created:
            return Response({'message': 'Repo successfully '}, status=201)
        else:
            return Response({'message':'Repo already exists'}, status=200)
        

class CreateBugView(APIView):
    def post(self, request):
        serializer = BugSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save(created_by=request.user)  
            return Response({'message': 'Bug successfully created'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
class ListBugs(generics.ListAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer


class ListBugID(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Bug.objects.all()
    serializer_class = BugSerializer 


    
        
        

