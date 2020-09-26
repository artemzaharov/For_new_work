from django.core.management.base import BaseCommand
import requests
from main.models import ApiArticle
import time
import threading
from random import choice
class Command(BaseCommand):

    help = "collect articles"   

    def handle(self, *args, **options):

        url = ('http://newsapi.org/v2/top-headlines?'
         'country={}&'
         'apiKey={}')
        key = '17ec3ff52d144c22bc61cb8dcac835f9'  
        countryies = ['ru', 'us','fr']
        country = choice(countryies)
  
        for all_articles in range(20):
            
            response = requests.get(url.format(country,key)).json()["articles"][all_articles]
            author = response.get('author', 'Автор Неизвестен') 
            title = response.get('title', 'Заголовок отсутствует')
            description = response.get('description', 'Описание отсутствует')

            try:
                ApiArticle.objects.create(
                    author=author,
                    title=title,
                    description=description)
                print(f'added {title}')
            except:
                print(f'already exists {title}')
            
            
while True:
    time.sleep(12)
    thread = threading.Thread(target=Command.handle, args=("handle", ))
    thread.start()
    time.sleep(500)
