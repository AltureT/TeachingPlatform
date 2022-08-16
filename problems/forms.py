
from django.forms import ModelForm, CharField, DateField
from .models import Problem


class AddProblemForm(ModelForm):
    author = CharField(
        label='上传者',
        required=False,
    )
    source = CharField(
        label='所属试卷',
        required=False,
    )
    publish_date = DateField(
        label='发布时间',
        required=False,
    )
    class Meta:
        model = Problem
        fields = '__all__'


