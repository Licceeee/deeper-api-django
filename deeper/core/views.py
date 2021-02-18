from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
import random
from card.models import Category, Question


def bad_request(request, exception):
    return render(request, 'core/errors/400.html', status=400)


def permission_denied(request, exception):
    return render(request, 'core/errors/403.html', status=403)


def page_not_found(request, exception):
    return render(request, 'core/errors/404.html', status=404)


def server_error(request):
    return render(request, 'core/errors/500.html', status=500)


class IndexView(TemplateView):
    template_name = 'core/index.html'


class CategoryView(ListView):
    template_name = 'core/categories.html'
    model = Category
    

class QuestionView(TemplateView):
    template_name = 'core/question.html'
    model = Question
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['pk']
        
        questions = Question.objects.filter(categories__id=category_id)
        
        context['category'] = Category.objects.get(id=category_id)
        
        try:
            context['question'] = random.choice(tuple(questions))
            # get random question out of pre-filtered set of questions
        except Exception as e:
            context['question'] = "No questions available for this category"
            print(e)
        

        # context['nr_questions'] = self.object.title
        # context['subtitle'] = format_html(f'<i class="fas fa-map-marker"></i>'
        #                                     f' {self.object.address}')
        # SEO
        # context['page_title'] = context['category']
        # context['page_description'] = _("Real estate manager."
        #                                 "Description and attribute listing of "
        #                                 "a specific object you are "
        #                                 "interested in.")
        return context


