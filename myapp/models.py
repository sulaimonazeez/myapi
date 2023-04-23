from django.db import models
class musicDatabased(models.Model):
  title = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  album = models.ImageField(upload_to='myapp')
  artist = models.CharField(max_length=255)
  song = models.FileField(upload_to='myapp')
  track = models.CharField(max_length=255)
  
  def __str__(self):
    return self.title
    
  class Meta:
    ordering = ('-id',)