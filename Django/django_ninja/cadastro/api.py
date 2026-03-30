from ninja import ModelSchema, NinjaAPI
from .models import Livro
from django.shortcuts import get_object_or_404
import orjson
from ninja.parser import Parser
from django.http import HttpRequest

class ORJSONParser(Parser):
    def parse_body(self, request: HttpRequest):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORJSONParser())

class LivroSchema(ModelSchema):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'descricao', 'autor']

@api.get('livro/', response=list[LivroSchema])
def listar(request):
    return Livro.objects.all()

@api.get('livro/{id}', response=LivroSchema)
def obter_livro(request, id: int):
    return get_object_or_404(Livro, id=id)

@api.post('livro', response=LivroSchema)
def livro_criar(request, livro: LivroSchema):
    obj = Livro(**livro.model_dump())
    obj.save()
    return obj