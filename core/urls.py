from django.urls import path
from .views import home_view, event_detail_view, news_post_view, all_news_view, all_events_view, search_view#, category_view

urlpatterns = [
    path('search/', search_view, name="search"),
    path('', home_view, name="home"),
    path('events/all/', all_events_view, name='all_events'),
    path('events/<slug:slug>/', event_detail_view, name="event_detail"),
    path('news/all/', all_news_view, name='all_news'),
    path('news/<slug:slug>/', news_post_view, name="news_post"),
    
    
    #path('<slug:category_slug>/', category_view, name='category-detail')
]
