from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'kanbanboards', views.KanbanBoardViewSet, 'kanbanboard')
router.register(r'columns', views.ColumnViewSet, 'columns')
router.register(r'cards', views.CardViewSet, 'cards')

urlpatterns = router.urls
