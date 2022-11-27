from django.db import models

# Create your models here.
from django.urls import reverse


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
        (1, 'VIP'),
        (2, 'Public Administration'),
    )

    PRIVATE_SECTOR = (
        (1, 'VIP'),
        (2, 'Corporate Partner'),
    )

    OTHER = (
        (1, 'VIP'),
    )

    SPECIAL_INTREST = (
        (1, 'Annual Report'),
        (2, 'Cooperation with China'),
        (3, 'Digt Society'),
        (4, 'ICEGOV'),
    )

    SPECIAL_CATEGORIES = (
        (1, 'ITEG Project 2008'),
        (2, 'DGI Institute'),
        (3, 'Grand Challenges Workshop'),
        (4, 'Hard Copy AR'),
        (5, 'Personalized Letter AR'),
    )

    PROJECT_PARTNERS = (
        (1, 'apa'),
        (2, 'awt'),
        (3, 'beth'),
        (4, 'dgi'),
        (5, 'dg_inst'),
        (6, 'diggov'),
        (7, 'dj2'),
        (8, 'dmv'),
        (9, 'docs'),
        (10, 'doj'),
        (11, 'egov'),
        (12, 'eot'),
        (13, 'gaof'),
        (14, 'gateways'),
        (15, 'gen'),
        (16, 'gis'),
        (17, 'grpware'),
        (18, 'hims'),
        (19, 'inetsys'),
        (20, 'inettb'),
        (21, 'itgov'),
        (22, 'journal'),
        (23, 'kdi'),
        (24, 'kwic'),
        (25, 'lc'),
        (26, 'lg1'),
        (27, 'lg2'), (28, 'mfa'), (29, 'miii'), (30, 'mobile'), (31, 'nadgwg'),
        (32, 'newmodels'), (33, 'nysit'), (34, 'omh'), (35, 'orma'), (36, 'orps'),
        (37, 'proi'), (38, 'rm2020'), (39, 'tmf'), (40, 'transnational'), (41, 'uig'), (42, 'un'),
        (43, 'usdafs'), (44, 'utw'), (45, 'writing'), (46, 'wtc1'), (47, 'xmltb'), (48, 'open govt'),
        (49, 'rich context'), (50, 'vpoc'), (51, 'arra'), (52, 'ifmr'), (53, 'epa'), (54, 'ocs'),
        (55, 'cpath'), (56, 'smartCities'), (57, 'iChoose'), (58, 'nytd'), (59, 'BOE'),
        (60, 'City of Albany Code Enforcement'), (61, 'ICEGOV 2012'), (62, 'Executive Leadership'),
        (63, 'IT Transformation'),
        (64, 'World Bank'), (65, 'Open Data'), (66, 'ISCC Workshop'), (67, 'IMLS'), (68, 'Kenya-CID'),
        (69, 'Urban Bilight'), (70, 'Digital Towpath'), (71, 'Health Research'), (72, 'Water Quality'),
        (73, 'DOH Visualization'), (74, 'GAB'), (75, '25th CTG Anniv'), (76, 'DEC Water Quality'), (77, 'SCC'),
        (78, 'NYS ITS Data Strategy'), (79, 'AHI'), (80, 'FEMA'),

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
    non_nys = models.PositiveSmallIntegerField(choices=NON_NYS, null=True)
    uai_bany = models.PositiveSmallIntegerField(choices=UAI_BANY, null=True)
    non_uai_bany = models.PositiveSmallIntegerField(choices=NON_UAI_BANY, null=True)
    private_sector = models.PositiveSmallIntegerField(choices=PRIVATE_SECTOR, null=True)
    other = models.PositiveSmallIntegerField(choices=OTHER, null=True)
    special_intrest = models.PositiveSmallIntegerField(choices=SPECIAL_INTREST, null=True)
    special_categories = models.PositiveSmallIntegerField(choices=SPECIAL_CATEGORIES, null=True)
    project_partners = models.PositiveSmallIntegerField(choices=PROJECT_PARTNERS, null=True)

    def get_absolute_url(self):
        return reverse('file_maker_detail', kwargs={"pk": self.pk})
