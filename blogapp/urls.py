
from django.urls import path
from .views import \
    (CreateCategory,
    GetAllCategory,
    UpdateCategory,
    GetCategory,
    DeleteCategory,
    PostViewSet
    )

urlpatterns = [
    path('/category/all',GetAllCategory.as_view()),
    path('/category/<str:pk>',GetCategory.as_view()),
    path('/category/create',CreateCategory.as_view()),
    path('/category/<str:pk>/edit',UpdateCategory.as_view()),
    path('/category/<str:pk>/delete',DeleteCategory.as_view()),

    path('/post/all',PostViewSet.as_view({'get':'list'})),
    path('/post/<str:pk>',PostViewSet.as_view({'get':'get'})),
    path('/post/create',PostViewSet.as_view({'post':'create'})),
    path('/post/<str:pk>/edit',PostViewSet.as_view({'put':'update'})),
    path('/post/<str:pk>/delete',PostViewSet.as_view({'delete':'delete'}))
]
