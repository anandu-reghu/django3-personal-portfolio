from django.db import models

class Blog(models.Model):
    image = models.ImageField(blank = True, upload_to='blog/images/')
    title = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    description = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.id) 
