from django.db import models


class Category(models.Model):
    name = models.CharField(db_column='name', max_length=100, blank=False)
    description = models.TextField(
        db_column='description', max_length=1000, blank=False)

    class Meta:
        db_table = 'category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.name if self.name else ''

    def __str__(self):
        return self.name if self.name else ''


class RiskType(models.Model):
    name = models.CharField(db_column='name', max_length=100, blank=False)
    description = models.TextField(
        db_column='description', max_length=1000, blank=False, null=True)

    class Meta:
        db_table = 'risktype'
        verbose_name = 'Tipo de risco'
        verbose_name_plural = 'Tipos de risco'


class Item(models.Model):
    name = models.CharField(db_column='name', max_length=1000, blank=False)
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    risk = models.TextField(db_column='risk', blank=False, null=True)
    how_to_assess = models.TextField(
        db_column='how_to_assess', blank=False, null=True)
    how_to_correct = models.TextField(
        db_column='how_to_correct', blank=False, null=True)

    class Meta:
        db_table = 'item'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
