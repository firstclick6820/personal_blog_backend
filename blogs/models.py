from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    


    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    exerpt = models.CharField(max_length=255)
    author =models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='media/posts')
    
    def __str__(self):
        return self.title
    
    


class Comment(models.Model):
    DRAFT = 'd'
    PUBLISHED = 'p'
    
    STATUS_OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=100, default=DRAFT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    
    def __str__(self):
        return self.name
    