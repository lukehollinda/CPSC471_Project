"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from api import views #REMOVE WEBAPP
#from WebApp.pages.views import home_view

router = routers.DefaultRouter()
#router.register(r'api', views.LandViewSet, 'land')
router.register(r'city', views.CityViewSet, 'City')
router.register(r'neighborhood', views.NeighborhoodViewSet, "Neighborhood")
router.register(r'land', views.LandViewSet, 'Land')
router.register(r'developer', views.DeveloperViewSet, 'Developer')
router.register(r'owner', views.OwnerViewSet, 'Owner')
router.register(r'personOwner', views.PersonOwnerViewSet, 'PersonOwner')
router.register(r'companyOwner', views.CompanyOwnerViewSet, 'CompanyOwner')
router.register(r'bankOwner', views.BankOwnerViewSet, 'BankOwner')
router.register(r'ownsRelation', views.OwnsRelationViewSet, 'OwnsRelation')
router.register(r'building', views.BuildingViewSet, 'Building')
router.register(r'commercialBuilding', views.CommecialBuildingViewSet, 'CommercialBuilding')
router.register(r'residentialBuilding', views.ResidentialBuildingViewSet, 'ResidentialBuilding')
router.register(r'renter', views.RenterViewSet, 'Renter')

urlpatterns = [
   # path('', home_view, name = 'home'),
    path('admin/', admin.site.urls),
    #path('', include('api.urls')),
    path('', include(router.urls))

]
