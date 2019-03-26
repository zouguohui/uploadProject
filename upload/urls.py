from upload import views
from django.urls import path, re_path

urlpatterns = [
    path('upload/', views.upload_file),
    path('index/', views.app_list),
    re_path('list/(?P<par>\S*)', views.download_file),
]