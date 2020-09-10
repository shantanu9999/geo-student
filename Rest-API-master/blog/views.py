from rest_framework.generics import (
	ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
	)

from .models import User
from .serializers import  UserSerializer


class PostView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer