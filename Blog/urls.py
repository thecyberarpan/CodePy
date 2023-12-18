from django.urls import path
from.import views

urlpatterns = [
    path('', views.BlogIndex, name="BlogIndex"),
    path('blog-details/<slug:blogslug>/', views.BlogDetails, name = "BlogDetails"),
]