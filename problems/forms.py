from django.forms import ModelForm
from .models import Problem, ProblemInformation


class AddProblem(ModelForm):
    class Meta:
        model = Problem
        fields = '__all__'


class AddProblemInfo(ModelForm):
    class Meta:
        model = ProblemInformation
        fields = ('author', 'source', 'publish_date', 'knowledge_points')
