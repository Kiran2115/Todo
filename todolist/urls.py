from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from todolist import views
from todolist.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todolist', views.TodoViewSet)

todo_list = TodoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
todo_detail = TodoViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = (
    path('', include(router.urls)),
    # path('', views.Todo_List.as_view(), name='todo-list'),
    # path('<int:pk>/', views.Todo_Detail.as_view(), name='todo-detail'),
    path('<int:pk>/start', views.change_status),
)
