from django.db import models
from django.contrib.contenttypes.models import ContentType


class GenericType(models.Model):

    concrete_type = models.ForeignKey(ContentType)

    class Meta:
        abstract = True

    def get_concrete_object(self):
        return self.concrete_type.get_object_for_this_type(id=self.id)


def set_concrete_type(sender, instance, *args, **kwargs):
    if isinstance(instance, GenericType):
        # set concrete_type field
        content_type = ContentType.objects.get_for_model(sender)
        instance.concrete_type = content_type
  

from django.db.models.signals import pre_save
pre_save.connect(set_concrete_type)
