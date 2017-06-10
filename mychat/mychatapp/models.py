from django.db import models
from django.utils import timezone


class Messages(models.Model):
    author = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    def __unicode__(self):
        return '[{created_date}] {author}: {message}'.format(**self.as_dict())
    @property
    def formatted_timestamp(self):
        return self.created_date.strftime('%b %-d %-I:%M %p')
    
    def __str__(self):
        return self.title
    def as_dict(self):
        return {'author': self.author, 'text': self.text, 'created_date':  self.formatted_timestamp}
