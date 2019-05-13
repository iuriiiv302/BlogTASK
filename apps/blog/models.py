from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

class Comments(models.Model):
    class Meta:
        db_table = "Comments"
    comments_text = models.TextField()
    comments_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)



    # def __str__(self):
    #     return '%s %s'%(self.title, self.enabled)
