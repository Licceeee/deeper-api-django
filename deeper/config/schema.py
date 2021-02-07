import graphene
from graphene_django.types import DjangoObjectType

from card.models import Category, Question


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryNode)
    questions = graphene.List(QuestionNode)


    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()


schema = graphene.Schema(query=Query)