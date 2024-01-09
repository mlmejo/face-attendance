from django.urls import include, path

app_name = 'admin'
urlpatterns = [
    path('courses/', include('admin.courses.urls')),
    path('subjects/', include('admin.subjects.urls')),
]
