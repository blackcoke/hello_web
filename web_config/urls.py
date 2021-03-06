"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home import views as homev
from board import views as boardv
from maps import views as mapsv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homev.home, name="home_home"),
    path('board/listwithmongo/', boardv.listwithmongo, name="listwithmongo_boardv"),
    path('board/listwithmongowithpaginator/', boardv.listwithmongowithpaginator, name="listwithmongowithpaginator_boardv"),

    path('board/listofworknet/', boardv.listofworknet, name="listofworknet_boardv"),
    path('board/listofjobkorea/', boardv.listofjobkorea, name="listofjobkorea_boardv"),
    path('board/scrapworknet/', boardv.scrapworknet, name="scrapworknet"),
    path('board/scrapjobkorea/', boardv.scrapjobkorea, name="scrapjobkorea"),

    path('maps/showmapwithfolium/', mapsv.showmapwithfolium, name="showmapwithfolium_mapsv"),
    
    path('hello/', homev.hello, name="hello_home"),
    path('hello/responsewithhtml/', homev.responsewithhtml, name="responsewithhtml_home"),
    path('hello/organization/', homev.organization, name="organization_home"),
    path('hello/form/', homev.form, name="form_home"),
    path('hello/template/', homev.template, name="template_home"),
]
