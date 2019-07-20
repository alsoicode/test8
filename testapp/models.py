from django.db import models
from adminsortable.models import SortableMixin


class Test(models.Model):
    test = models.CharField(max_length=8)


class SortTest(Test, SortableMixin):
    test2 = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['test2', ]
