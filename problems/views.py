from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Problem, ProblemInformation


# Create your views here.

def index(request):
    latest_problem_list = \
        Problem.objects.order_by(
            '-info_of__publish_date'
        )[:10]

    context = {
        'latest_problem_list': latest_problem_list,
    }

    return render(request, 'problems/index.html', context)


def detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    problem_info = problem.info_of
    return render(request, 'problems/detail.html', {
        'problem': problem,
        'problem_info': problem_info,
    })
