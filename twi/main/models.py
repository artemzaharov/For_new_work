from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class LatestArticlesManager:

    @staticmethod
    def get_articles_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        articles = []
        ct_models = ContentType.objects.filter(model__in=args)    
        for ct_models in ct_models:
            model_articles = ct_models.model_class()._base_manager.all().order_by('-id')[:30]
            articles.extend(model_articles)
        if with_respect_to:
            ct_models = ContentType.objects.filter(model=with_respect_to)
            if ct_models.exists():
                if with_respect_to in args:
                    return sorted(articles, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True)
        return articles


class LatestArticles:

    objects = LatestArticlesManager()


class MyArticle(models.Model):

    title = models.CharField(max_length=500, verbose_name='Заголовок')
    author = models.CharField(max_length=300, verbose_name='Автор',)
    description = models.TextField(verbose_name='Описание', )
    date_pub = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = ("MyArticle")
        verbose_name_plural = ("MyArticles")

    def __str__(self):
        return self.title


class ApiArticle(models.Model):

    title = models.CharField(max_length=500, verbose_name='Заголовок',unique=True)
    author = models.CharField(max_length=300, verbose_name='Автор',)
    description = models.TextField(verbose_name='Описание',)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("ApiArticle")
        verbose_name_plural = ("ApiArticles")

    def __str__(self):
        return self.title
   

class AllArticles(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "Статьи: {}".format(self.content_object.title)