from django.contrib import admin
from django.urls import path, include
from livro.views import CategoriasViewSet, LivrosViewSet, EmprestimosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorias', CategoriasViewSet)
router.register(r'livros', LivrosViewSet)
router.register(r'emprestimos', EmprestimosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    path('', include(router.urls))
]
