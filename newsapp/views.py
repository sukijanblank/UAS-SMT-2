from email.mime import image
from turtle import title
from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?country=id&apiKey=3a50d26e71e94b17872b8e74bb030921')
    res = r.json()
    articles = res['articles']
    title = []
    description = []
    urlToImage = []
    url = []
    for i in articles:
        title.append(i['title'])
        description.append(i['description'])
        urlToImage.append(i['urlToImage'])
        url.append(i['url'])
    news = zip(title, description, urlToImage, url)
    return render(request, 'newsapp/index.html', {'news' :news})