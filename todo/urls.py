from django.urls import path
from .views import TodoModelGetView,TodoModelCreateView

urlpatterns= [
    path("get/",TodoModelGetView.as_view()), 
    path('create/',TodoModelCreateView.as_view()),
    path("get/<int:pk>/",TodoModelGetView.as_view()), 
]