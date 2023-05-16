import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', include('grados.app.teachers.urls')),
    path('accounts/', include('grados.app.accounts.urls')),
    path('students/', include('grados.app.students.urls')),
    path('parents/', include('grados.app.parents.urls')),
    path("__debug__", include(debug_toolbar.urls)),  # Debug purposes
]
