from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
