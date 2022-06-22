from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(db_column='name', max_length=100, blank=False)
    companyName = models.CharField(db_column='company_name', max_length=100, blank=False, null=True)
    email = models.CharField(db_column='email', max_length=100, blank=False, null=True)
    active = models.BooleanField(default=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False, null=True)
    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Clientes'
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name