from django.urls import path
from.import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('notes/', views.GetNotes, name="GetNotes"),
    path('notes-details/<slug:slug>', views.NotesDetails, name="NotesDetails"),
    path('category/', views.AllCategory, name='AllCategory'),
    path('category/<slug:catslug>', views.CategoryDetails, name='CategoryDetails'),
    path('author/', views.AllAuthor, name="AllAuthor"),
    path('author/<slug:authslug>', views.AuthorDetails, name="AuthorDetails"),
    path('filtered-results/', views.filtered_results, name='filtered_results'),
]