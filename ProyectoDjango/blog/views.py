from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render
from .forms import UserEditForm

# Create your views here.
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name="post_detail.html"

class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name="post_new.html"
    fields= ['titulo','subtitulo','autor','cuerpo']


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['titulo', 'subtitulo','cuerpo']

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


def editar_perfil(request):
    usuario=request.user
    if request.method == "POST":
        
        formularioEditorPerfil=UserEditForm(request.POST, instance=request.user)

        if formularioEditorPerfil.is_valid():
            
            data = formularioEditorPerfil.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(request, "home.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(request, "editar_perfil.html", {"formularioEditorPerfil": formularioEditorPerfil})

    else:
        formularioEditorPerfil = UserEditForm(instance=usuario)
        return render(request, "editar_perfil.html", {"formularioEditorPerfil": formularioEditorPerfil})
