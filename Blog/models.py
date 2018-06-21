from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """
    This is the model of the article
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # ForeignKey is linked to another model,
# auth.User = this is a user field
    title = models.CharField(max_length=200)  # Text with limited character
    text = models.TextField()  # Text with Unlimited character
    created_date = models.DateTimeField(default=timezone.now)  # DateTimeField is for date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        #  This function/method will publish the post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        string representation of the model, useful in ORM
        :return: title by author
        """
        return self.title + " by "+ str(self.author)
