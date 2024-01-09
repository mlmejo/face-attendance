from django.urls import include, path

urlpatterns = [
    path('courses/', include('admin.courses.urls')),
]
