from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import * 

urlpatterns = [
    path("editar_perfil/", editar_perfil, name='EditarPerfil'), 
    path("accounts/",include("django.contrib.auth.urls")),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(),name="post_delete"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),  # new
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
    path('about/', about, name='about'),
      
    
]

# para iamagenes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
