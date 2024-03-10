from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def validate_title(title):
    if len(title) < 2:
        raise ValidationError("invlaid title")
    return title

class Crud(models.Model):
    title = models.CharField(_('title'), blank=True, max_length=50, validators=[validate_title])
