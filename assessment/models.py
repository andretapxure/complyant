from django.db import models
from customer.models import Customer

# Create your models here.


class Assessment(models.Model):
    name = models.CharField(db_column='name', max_length=100, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    template = models.ForeignKey('template.Template', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        db_table = 'assessment'
        verbose_name = 'Assessment'
        verbose_name_plural = 'Assessments'
        unique_together = ("customer", "template")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
