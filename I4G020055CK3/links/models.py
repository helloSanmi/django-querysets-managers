from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from pytz import timezone
from django.utils import timezone

from I4G020055CK3.links.manage import ActiveLinkManager
from . import utils


class Link(models.Model):

    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(
            get_user_model(), on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()

    def __str__(self):
        return f"{self.identifier}"

    def save(self, *args, **kwargs):
        if not self.identifier:
            # Generate a random ID
            random_id = utils.generate_random_id()
            
            # Make sure there is no other Link with that same ID
            while Link.objects.filter(identifier=random_id).exists():
                random_id = utils.generate_random_id()

            self.identifier = random_id
        
        # Complete the save operation   
        super().save(*args, **kwargs)   
