from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tagent_leave_app.urls'), name='tagent_leave_app')
]
