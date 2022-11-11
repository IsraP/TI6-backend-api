from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from API import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("mamografias/", views.mamografia_list_or_add),
    path("mamografias/nprocessed", views.get_all_non_processed),
    path("mamografias/<str:pk>/", views.mamografia_detail)
]