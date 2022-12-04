from django.urls import path
from .views import CategoryListView, quiz_view, quizes_view

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<category_pk>/', quizes_view, name='quizes'),
    path('<category_pk>/<quiz_id>/', quiz_view, name='quiz'),

]
