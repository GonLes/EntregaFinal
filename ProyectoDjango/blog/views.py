from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render
from .forms import UserEditForm
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

class BlogCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields= ['titulo','subtitulo','autor','cuerpo','imagen_post']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['titulo', 'subtitulo','cuerpo','imagen_post']

class BlogDeleteView(DeleteView):
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
    
def about(request):
    return render(request, 'about.html')

