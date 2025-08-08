from django.urls import path
from .views import (
    ListUserRepos,
    ImportRepositoryView,
    CreateBugView,
    ListBugs,
    ListBugID,
)

urlpatterns = [
    path('repos/', ListUserRepos.as_view(), name='list-user-repoz'),
    path('import/repo/', ImportRepositoryView.as_view(), name='import-repo'),
    path('bug/create/', CreateBugView.as_view(), name='bug-create'),
    path('bugs/', ListBugs.as_view(), name='list-bugs'),
    path('bug/<int:pk>/', ListBugID.as_view(), name='bug-id'),
]
