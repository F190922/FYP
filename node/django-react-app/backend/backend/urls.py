
 
# import views from todo
from todo import views
 
# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
 
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'tasks',views.ArticleViewSet, 'task')
 
from django.urls import path, include

urlpatterns = [
    path('', include(router.urls)),
]
