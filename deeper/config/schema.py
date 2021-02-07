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
    category_by_id = graphene.Field(CategoryNode, id=graphene.Int())
    
    questions = graphene.List(QuestionNode)
    question_by_id = graphene.Field(QuestionNode, id=graphene.Int())


    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()
    
    def resolve_category_by_id(self, info, id):
        # Querying a single Category
        return Category.objects.get(pk=id)


    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()
    
    def resolve_question_by_id(self, info, id):
        # Querying a single question
        return Question.objects.get(pk=id)



schema = graphene.Schema(query=Query)