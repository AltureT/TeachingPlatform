import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Problem(models.Model):
    class Difficulty(models.TextChoices):
        SIMPLE = 'simple', _('简单')
        NORMAL = 'normal', _('正常')
        HARD = 'hard', _('困难')

    class Types(models.TextChoices):
        CHOOSE = 'choose correct words', _('选择题')
        GAP = 'fill gaps', _('填空题')

    problem_text = RichTextUploadingField(verbose_name='题目内容')
    difficulty = models.CharField(
        '难度',
        choices=Difficulty.choices,
        default=Difficulty.NORMAL,
        max_length=20,
    )
    type = models.CharField(
        '类别',
        choices=Types.choices,
        default=Types.CHOOSE,
        max_length=20,
    )

    class KnowledgePoints(models.TextChoices):
        PANDAS = 'pandas', _('pandas数据分析')
        EXCEL = 'excel', _('Excel表格分析')

    author = models.CharField('上传者', max_length=20, )
    source = models.CharField('所属试卷', max_length=50, blank=True)
    publish_date = models.DateField('发布时间', blank=True)
    knowledge_points = models.CharField(
        '知识点',
        choices=KnowledgePoints.choices,
        default=KnowledgePoints.PANDAS,
        max_length=40,
    )

    def __str__(self):
        return self.problem_text

    def was_published_recently(self):
        # 判断是否最近五天内发布
        return self.publish_date >= \
               timezone.now() - datetime.timedelta(days=5)

    # @admin.display(description='Title')
    # def convert_problem_text_to_html(self):
    #     title = self.problem_text
    #     return
