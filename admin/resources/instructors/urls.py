from django.urls import path

from .views import (InstructorCreateView, InstructorDeleteView,
                    InstructorListView, InstructorUpdateView)

urlpatterns = [
    path('', InstructorListView.as_view(), name='instructor-list'),
    path('create/', InstructorCreateView.as_view(), name='instructor-new'),
    path('<pk>/edit/', InstructorUpdateView.as_view(), name='instructor-edit'),
    path('<pk>/delete/', InstructorDeleteView.as_view(), name='instructor-delete'),
]
