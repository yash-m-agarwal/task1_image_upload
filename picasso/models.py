from django.db import models

class MetaData(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    metadata = models.ForeignKey(MetaData, related_name='images')
