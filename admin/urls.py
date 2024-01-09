from django.urls import include, path

app_name = 'admin'
urlpatterns = [
    path('courses/', include('admin.resources.courses.urls')),
    path('subjects/', include('admin.resources.subjects.urls')),
    path('instructors/', include('admin.resources.instructors.urls')),
    path('students/', include('admin.resources.students.urls')),
]
