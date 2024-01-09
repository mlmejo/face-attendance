from django.urls import path

from .views import (StudentCreateView, StudentDeleteView, StudentListView,
                    StudentUpdateView)

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-new'),
    path('<pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]
