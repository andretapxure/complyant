from django.db import models
from item.models import Item
from assessmentitems.models import AssessmentItems


class Template(models.Model):
    name = models.CharField(db_column='name', max_length=100, blank=False)
    items = models.ManyToManyField(Item)

    class Meta:
        db_table = 'template'
        verbose_name = 'Templ ates'
        verbose_name_plural = 'Assessment Templates'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

