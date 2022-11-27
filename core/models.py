from django.db import models

# Create your models here.
class FileMaker(models.Model):

    NYC_AGENCY_CHOICES = (
        (1, 'VIP'),
        (2, 'Agencyhead'),
        (3, 'Forum Irep'),
        (4, 'Forum Exec Committee'),
        (5, 'CTG Standing Committee'),
    )
    LEGISLATURE = (
        (1, 'Assembly'),
        (2, 'Senate'),
        (3, 'Congress'),
    )

    NON_NYS = (
        (1, 'VIP'),
        (2, 'SCIO'),
    )

    UAI_BANY = (
        (1, 'VIP'),
        (2, 'Information Faculty'),
        (3, 'INF Students'),
        (4, 'University Council'),
        (5, 'SUNY Brd of Trustees'),
        (6, 'UAIbany Foundation'),
        (7, 'CTG Alumni'),
        (8, 'CTG Staff'),
        (9, 'A-list'),
        (10, 'Public Administration'),
        (11, 'Fellows'),
        (12, 'iCEHC'),
        (13, 'Director'),
    )
    NON_UAI_BANY = (
        (1,'VIP'),
        (2,'Public Administration'),
    )

    sal = models.CharField(max_length=80)
    sal1 = models.CharField(max_length=80)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    agencyCompany = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    zip = models.IntegerField()
    zip2 = models.IntegerField()
    url = models.URLField(max_length=200)
    phone = models.IntegerField()
    fax = models.IntegerField()
    cell_phone = models.IntegerField()

    email = models.EmailField(max_length=32)
    skype_name = models.CharField(max_length=200)
    other_contact = models.IntegerField()

    nyc_agency = models.PositiveSmallIntegerField(choices=NYC_AGENCY_CHOICES, null=True)
    legislature = models.PositiveSmallIntegerField(choices=LEGISLATURE, null=True)
    uai_bany = models.PositiveSmallIntegerField(choices=UAI_BANY, null=True)

