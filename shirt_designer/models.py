from django.db import models
from shop.models import FabricModel
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete



def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)
    return file_path

class CollarType(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.type

class Collar(models.Model):
    fabric = models.ForeignKey(FabricModel,
                              related_name='+', blank=True, null=True,
                              on_delete=models.CASCADE)
    type = models.ForeignKey(CollarType,
                               related_name='+', blank=True, null=True,
                               on_delete=models.CASCADE)
    # type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.fabric} {self.type}'


#
# @receiver(post_delete, sender=Collar)
# def submission_delete(sender, instance, **kwargs):
#     instance.image.delete(False)