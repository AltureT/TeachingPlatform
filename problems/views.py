from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Problem
from .forms import AddProblemForm


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'problems/index.html'
    context_object_name = 'latest_problem_list'

    def get_queryset(self):
        return Problem.objects.order_by(
            'publish_date'
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
    return render(request, 'problems/detail.html', {
        'problem': problem,
    })


def add(request):
    problem = AddProblemForm
    context = {
        'problem': problem,
    }
    return render(request, 'problems/add.html', context=context)


def save_problem_to_db(new_problem):
    pass


def add_to_db(request):
    context = {
        'success': False,
    }
    if request.method == 'POST':
        form = AddProblemForm(request.POST)
        if form.is_valid():
            save_problem_to_db(form)
            context = {
                'success': True,
            }

    return render(request, 'problems/add.html', context=context)
