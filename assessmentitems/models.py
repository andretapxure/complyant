from django.db import models
from item.models import Item
from assessment.models import Assessment
# Create your models here.
class ComplianceLevel(models.Model):
    name = models.CharField(db_column='name', max_length=20, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False, null=True)
    class Meta:
        db_table = 'compliancelevel'
        verbose_name = 'Compliance Level'
        verbose_name_plural = 'Compliance Levels'
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class AssessmentItems(models.Model):

    assessment = models.ForeignKey(Assessment, db_column='assessment_id', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, db_column='item_id', on_delete=models.CASCADE)
    compliance_level = models.ForeignKey('ComplianceLevel', db_column='compliance_level_id', on_delete=models.CASCADE)
    measures = models.TextField(db_column='measures', max_length=1000, blank=True, null=True)
    reasonfornotapplicable = models.TextField(db_column='reasonfornotapplicable', max_length=1000, blank=True, null=True)
    class Meta:
        db_table = 'assessmentitems'
        verbose_name = 'Assessment Items'
        verbose_name_plural = 'Assessment Items'
    def __unicode__(self):
        return self.measures if self.measures else ''
    def __str__(self):
        return self.measures if self.measures else ''