from django.urls import path
from .views import IndexView, CategoryView, QuestionView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question'),
]
