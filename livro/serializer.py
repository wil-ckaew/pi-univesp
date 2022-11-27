from dataclasses import fields
from rest_framework import serializers
from livro.models import Categoria, Livros, Emprestimos

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome','descricao','usuario']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['nome','autor','co_autor','data_cadastro','emprestado','categoria']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = ['nome_emprestado','nome_emprestado_anonimo','data_emprestimo','data_devolucao','livro','avaliacao']

