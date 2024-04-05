from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

article_pages = {
    'sports': "Sports",
    'finance': "Finance Page", 
    'politics': "Politics Page",
}
# Create your views here.
def news_view(request, topic):
    try:
        result = article_pages[topic]
        return HttpResponse (result)
    except:
        raise Http404("Generic 404") #Linked to custom 404 later
    
def num_page_view(request, num_page):
    topics_list = list(article_pages.keys())
    topic = topics_list[num_page]

    try: 
        return HttpResponseRedirect(reverse('topic-page', args=[topic]))
    except:
        raise Http404("GENERIC 404 PAGE NOT FOUND")

