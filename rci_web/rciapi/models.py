from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Unit(models.Model):
    objects = None
    ou = models.CharField(
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\.\d{3}\.\d{3}',
                message='Kod jednostki musi być w formacie XX.XXX.XXX',
                code="Invalid OU"
            ),

        ], max_length=10, error_messages={'blank': "dsdsadsa"})
    abbr = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return '%s' % self.ou


class Employee(models.Model):

    employee_number = models.IntegerField(validators=[MaxValueValidator(999999),
                                                      MinValueValidator(100000)])
    ou = models.ForeignKey(Unit, related_name='ous', on_delete=models.RESTRICT)
    pesel = models.CharField(blank=False,
                             validators=[RegexValidator(regex=r'^[0-9]{11}$', message="Błędny numer PESEL",

                                                        code="Invalid PESEL")],
                             max_length=11
                             )
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mail = models.CharField(blank=False,
                            validators=[
                                RegexValidator(regex=r'^[A-Za-z0-9._%+-]+@uwm.edu.pl$', message="Błędny adres email",
                                               code="Invalid email")],
                            max_length=255)
    phone = models.CharField(blank=False,
                             validators=[
                                 RegexValidator(regex=r'^\d{2}\-\d{3}\-\d{2}-\d{2}|\d{3}\-\d{3}\-\d{3}',
                                                message="Błędny numer telefonu", code="Invalid phone")],
                             max_length=len("XX-XXX-XX-XX"))
    work_length = models.IntegerField(validators=[MaxValueValidator(99),
                                                  MinValueValidator(0)])
    salary = models.DecimalField(blank=False, decimal_places=2, max_digits=9)
