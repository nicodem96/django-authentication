from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, \
MaxValueValidator
# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)],
                                            help_text='Inserisci un valore compreso tra 1 e 10')

    def __str__(self) -> str:
        return self.title