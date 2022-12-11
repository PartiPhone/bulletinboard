from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import bbs, BbDetailView, comments, BbListViewSet

from .views import BbListViewSet

urlpatterns = [
    path('bbs/<int:pk>/comments', comments),
    path('bbs/<int:pk>/', BbDetailView.as_view()),
    path('bbs/', bbs)
]

# router = DefaultRouter()
# router.register(r'comments', BbListViewSet, basename="comment")
# router.register(r'bbs', BbListViewSet, basename="bbs")


# urlpatterns = [
    # path('', include(router.urls)),
# ]
