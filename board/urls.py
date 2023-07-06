from django.urls import path
from . import views
from .views import BoardList, BoardDetail, CommentList, SameUniversity, BoardDetailUpdate, BoardDetailDestroy

app_name = 'board'

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/update/', BoardDetailUpdate.as_view()),
    path('<int:pk>/destroy/', BoardDetailDestroy.as_view()),
    path('<int:pk>/comments/', CommentList.as_view()),
    path('sameuniv/', SameUniversity.as_view())
]