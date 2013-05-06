from django.db import models

class ShopSettings(models.Model):
    currency_option = models.ForeignKey()
    


class CurrencyOption(models.Model):
    pass