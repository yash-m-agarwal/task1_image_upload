from django.db import models

class Data(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    image_flagship = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    data = models.ForeignKey(Data, related_name='images', null=True)
