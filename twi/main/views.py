from django.shortcuts import render
import requests
from .models import *
from itertools import chain
from django.db.models import Q


def index(request):
   search_query = request.GET.get('search','')
   if search_query:
      search_query = search_query.upper()
      query_sets = []
      query_sets.append(ApiArticle.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(author__icontains=search_query)))
      query_sets.append(MyArticle.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(author__icontains=search_query)))

      articles = list(chain(*query_sets))
   else:
      articles = LatestArticles.objects.get_articles_for_main_page('myarticle', 'apiarticle',with_respect_to='myarticle')
     
   print(f'query:{search_query}')

   context = {'articles':articles}
   return render(request, 'twits/base.html',context) 



def sort(request):
   sort_query = request.GET.get('sort','')
   if sort_query == 'newsort':
      
      query_sets = []
      query_sets.append(ApiArticle.objects.order_by('date_pub'))
      query_sets.append(MyArticle.objects.order_by('date_pub'))

      articles = list(chain(*query_sets))
   else:
      articles = LatestArticles.objects.get_articles_for_main_page('myarticle', 'apiarticle',with_respect_to='myarticle')
   print(f'sort-query:{sort_query}')

   context = {'articles':articles}
   return render(request, 'twits/base.html',context) 



