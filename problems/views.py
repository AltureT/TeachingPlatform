from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Problem, ProblemInformation


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'problems/index.html'
    context_object_name = 'latest_problem_list'

    def get_queryset(self):
        return Problem.objects.order_by(
            '-info_of__publish_date'
        )[:10]


class DetailView(generic.DetailView):
    model = Problem
    template_name = 'problems/detail.html'


# class ProblemDetailView(DetailView):
#     model = Problem
#     problem_info = model.info_of
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['problem'] = self.model
#         context['problem_info'] = self.problem_info
#
#         return context
def detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    problem_info = problem.info_of.get(problem_id=problem.id)
    return render(request, 'problems/detail.html', {
        'problem': problem,
        'problem_info': problem_info,
    })
