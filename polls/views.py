from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    # return HttpResponse(latest_question_list)
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse('Usted esta buscando la pregunta %s' % question_id)


def results(request, question_id):
    response = 'Usted está buscando el resultado de la pregunta %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Usted quiere votar la pregunta %s' % question_id)
