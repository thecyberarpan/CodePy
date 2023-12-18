from django.urls import path
from.import views


urlpatterns = [
    path('', views.BlogIndex, name="BlogIndex"),
    path('blog-detail/<slug:BlogSlug>/', views.BlogDetail, name="BlogDetail"),
]