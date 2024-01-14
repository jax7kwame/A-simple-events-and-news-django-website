from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import NewsPost, Event
from .forms import EventCommentForm


def home_view(request):
  events = Event.objects.all()
  news = NewsPost.objects.filter(status=NewsPost.ACTIVE)

  context = {
    'events': events,
    'news': news,
    }

  return render(request, 'index.html', context)


def all_events_view(request):
  events = Event.objects.all()
  events_paginator = Paginator(events, 4)

  event_page_number = request.GET.get("page")
  event_page_obj = events_paginator.get_page(event_page_number)

  context = {
  'event_page_obj': event_page_obj
  }

  return render(request, 'events_all.html', context)


def all_news_view(request):
  news = NewsPost.objects.all()
  news_paginator = Paginator(news, 4)

  news_page_number = request.GET.get("page")
  news_page_obj = news_paginator.get_page(news_page_number)

  context = {
  'news_page_obj': news_page_obj
  }

  return render(request, 'news_all.html', context)

def event_detail_view(request, slug):
  event = get_object_or_404(Event, slug=slug)

  if request.method == 'POST':
    form = EventCommentForm(request.POST)

    if form.is_valid():
      comment = form.save(commit=False)
      comment.event = event
      comment.save()

      return redirect('event_detail', slug=slug)
  else:
    form = EventCommentForm()

  context = {
    'event': event,
    'form': form
  }
  return render(request, 'event_details.html', context)


def news_post_view(request, slug):
  news_post = get_object_or_404(NewsPost, slug=slug, status=NewsPost.ACTIVE)
  """
  if request.method == 'POST':
    news_comment_form = NewsPostCommentForm(request.POST)

    if news_comment_form.is_valid():
      comment = news_comment_form.save(commit=False)
      comment.news_post = news_post
      comment.save()

      return redirect('news_post', slug=slug)
  else:
    news_comment_form = NewsPostCommentForm()
  """
  context = {
    'news_post': news_post,
    #'news_comment_form': news_comment_form
  }

  return render(request, 'news-post.html', context)

'''
def category_view(request, category_slug):
  category = get_object_or_404(Category, category_slug=category_slug)
  events = category.events.filter()

  context = {
    'category': category
  }

  return render(request, 'category.html', context)
'''


def search_view(request):
  query = request.GET.get('query', '#')

  events = Event.objects.filter(Q(event_title__icontains=query) | Q(description__icontains=query) | Q(hosting_church_or_group__icontains=query) | Q(description__icontains=query) | Q(event_type__icontains=query))

  context = {
    'events': events,
    'query': query
  }

  return render(request, 'search.html', context)
