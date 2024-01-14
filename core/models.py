from django.db import models

'''
class Category(models.Model):
  category_title = models.CharField(max_length=255)
  category_slug = models.SlugField()

  def __str__(self):
     return self.category_title

  class Meta:
    ordering = ('-category_title',)
    verbose_name_plural = 'Categories'
'''


class Event(models.Model):
  #event_category = models.ForeignKey(Category,related_name='posts', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  event_title = models.CharField(max_length=255)
  event_photo = models.ImageField(upload_to='uploads/events')
  slug = models.SlugField()
  description = models.TextField()
  event_type = models.CharField(max_length=100)
  event_date = models.DateField()
  event_time = models.TimeField()
  hosting_church_or_group = models.CharField(max_length=255)
  church_location = models.CharField(max_length=255)
  church_district = models.CharField(max_length=255)
  church_conference = models.CharField(max_length=255)
  website_link = models.CharField(max_length=255, blank=True)
  facebook_link = models.CharField(max_length=255, blank=True)
  instagram_link = models.CharField(max_length=255, blank=True)
  twitter_link = models.CharField(max_length=255, blank=True)
  speaker_name = models.CharField(max_length=50)
  speaker_title = models.CharField(max_length=50)
  speaker_image =models.ImageField(upload_to='uploads/speakers', blank=True)
  #sessions_activities = models.FileField(blank=True)
  on_site = models.BooleanField()
  virtual_link = models.CharField(max_length=255, blank=True)
  sponsor_title = models.CharField(max_length=50, blank=True)
  sponsor_logo = models.ImageField(upload_to='uploads/logos', blank=True)

  def __str__(self):
      return self.event_title
  
  class Meta:
     ordering: ('-created_at',)
     verbose_name_plural = 'Events'
  

class EventComment(models.Model):
  event = models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ('-created_at',)
    verbose_name_plural = 'Event Comments'


class NewsPost(models.Model):
  ACTIVE = 'active'
  DRAFT = 'draft'

  CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft')
  )
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  image = models.ImageField(upload_to='uploads/news', blank=True)
  author = models.CharField(max_length=50, default="Unknown")
  intro = models.TextField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)

  def __str__(self):
      return self.title
  
  class Meta:
     ordering = ('-created_at',)
     verbose_name_plural = 'News'

"""

class NewsPostComment(models.Model):
  event = models.ForeignKey(NewsPost, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ('-created_at',)
    verbose_name_plural = 'News Post Comments'
"""


   