from django.contrib import admin
from django.urls import include, path
from explorer import views as explorerViews
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r"operational-units", explorerViews.OperationalUnitViewSet)
router.register(r"oilfields", explorerViews.OilfieldViewSet)
router.register(r"wells", explorerViews.WellViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("challenge1/", explorerViews.challenge1),
    path("challenge2/", explorerViews.challenge2)
]
