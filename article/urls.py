from django.urls import path
from article.views import CategoryView, HomeView, NewsView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("category/<str:slug>/", CategoryView.as_view(), name="category"),
    path("<str:slug>/", NewsView.as_view(), name="news"),
]
