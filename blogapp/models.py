import uuid
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=100,blank=False)

    class Meta:
        ordering=('title',)

    def __str__(self):
        return str(self.title)
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=250,blank=False)
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE,blank=True)
    description=models.TextField()
    createdAt = models.DateTimeField()

    class Meta:
        ordering=('createdAt',)

    def __str__(self):
        return str(self.title)