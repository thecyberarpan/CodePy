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


    # path('category/', views.AllCategory, name = 'AllCategory'),
    # path('category/<slug:category_slug>/', views.CategoryPosts, name='category_posts'),
    # path('instructors-list/', views.InstructorsList, name="InstructorsList"),
    # path('instructors-single/', views.InstructorsSingle, name="InstructorsSingle"),
]