from django.urls import path

from .views import (SubjectCreateView, SubjectDeleteView,
                                  SubjectListView, SubjectUpdateView)

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject-list'),
    path('create/', SubjectCreateView.as_view(), name='subject-new'),
    path('<pk>/edit', SubjectUpdateView.as_view(), name='subject-edit'),
    path('<pk>/delete', SubjectDeleteView.as_view(), name='subject-delete'),
]
