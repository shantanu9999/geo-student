from django.urls import path
from .views import PostView, SinglePostView

app_name = "blog"

urlpatterns = [
    path('user/', PostView.as_view()),
    path('user/<int:pk>', SinglePostView.as_view())
]