from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
import io
from django.core.files.storage import default_storage as storage
from django.contrib.auth.models import User

# Create your models here.


class Meme(models.Model):
    caption = models.CharField(max_length=120)
    meme = models.ImageField(upload_to="memes")
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # relationship with User
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Meme: {self.caption}, {self.date_posted}"

    def get_absolute_url(self):
        return reverse("gamebit-meme-full", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_read = storage.open(self.meme.name, 'rb')
        img = Image.open(img_read)

        if img.height > 900 or img.width > 1600:
            output_size = (1600, 900)
            img.thumbnail(output_size)
            in_mem_file = io.BytesIO()
            img.convert('RGB').save(in_mem_file, format='JPEG')
            img_write = storage.open(self.meme.name, 'w+')
            img_write.write(in_mem_file.getvalue())
            img_write.close()
        img_read.close()
