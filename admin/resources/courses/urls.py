from django.urls import path

from .views import (CourseCreateView, CourseDeleteView,
                                 CourseListView, CourseUpdateView)

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-new'),
    path('<pk>/edit', CourseUpdateView.as_view(), name='course-edit'),
    path('<pk>/delete', CourseDeleteView.as_view(), name='course-delete'),
]
