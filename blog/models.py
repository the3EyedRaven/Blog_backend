from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.SmallAutoField(auto_created=True, primary_key=True, blank=False, null=False)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.category

# class Author(models.Model):
#     name = models.CharField(max_length=225)
#     biography  = models.TextField()
#     date_of_birth = models.DateField()
#     # blog = models.ManyToManyField(Blog, related_name='author', blank=True)

#     def __str__(self) -> str:
#         return self.name


class Blog(models.Model):
    id = models.SmallAutoField(auto_created=True, primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE, blank=True, null=True)
    # author = models.ManyToManyField(Author, related_name='blogs', blank=True)
    cover = models.ImageField(upload_to='blog', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
