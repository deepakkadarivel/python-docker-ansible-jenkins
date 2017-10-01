from django.conf.urls import include, url
from todo import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemsViewSet)

# The API urls are now automatically determined by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
]
