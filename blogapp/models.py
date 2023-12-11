from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        ordering=('title',)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    description=models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('createdAt',)

    def __str__(self):
        return self.title