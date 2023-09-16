from .models import Task
from rest_framework import ( 
    viewsets, 
    authentication, 
    permissions,
    filters
)
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    #queryset = Todolist.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        request_user = self.request.user  # El usuario que ha iniciado sesión
        return Task.objects.filter(user=request_user)
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends =[filters.SearchFilter]
    search_fields = ['description', 'created_at']