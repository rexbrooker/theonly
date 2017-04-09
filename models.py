from django.db import models
# from django.urls import reverse


class Brewery_Graphic(models.Model):
    brewery_graphic = models.ImageField("brewery graphic", upload_to='theonly/brewery_graphic/')  # , default='media/None/no-img.jpg' upload_to=None, height_field=None, width_field=None, max_length=100, **options

    def __str__(self):
        return "%s" % (self.brewery_graphic)

    def __unicode__(self):
        return self.__str__()


class Brewery(models.Model):
    brewery_name = models.CharField("brewery name", max_length=2048, unique=True)                      # Combo, Add Type
    brewery_graphic = models.ForeignKey(Brewery_Graphic, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.brewery_name)

    def __unicode__(self):
        return self.__str__()


class Beverage_Style(models.Model):
    beverage_style = models.CharField("beverage style", max_length=256, unique=True)                          # Combo, Add Type

    def __str__(self):
        return "%s" % (self.beverage_style)

    def __unicode__(self):
        return self.__str__()


class Beverage_Serving_Size(models.Model):
    beverage_serving_size = models.CharField("serving size", max_length=256, unique=True)

    def __str__(self):
        return "%s" % (self.beverage_serving_size)

    def __unicode__(self):
        return self.__str__()


class Beverage_Serving_Graphic(models.Model):
    beverage_serving_graphic = models.ImageField("serving graphic", upload_to='theonly/beverage_serving_graphic/')  # upload_to=None, height_field=None, width_field=None, max_length=100, **options

    def __str__(self):
        return "%s" % (self.beverage_serving_graphic)

    def __unicode__(self):
        return self.__str__()


class Beverage(models.Model):
    beverage_color = models.CharField("Hash of beverage color", max_length=6)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, verbose_name="beverage brewery")  # Combo, Add Type
    beverage_name = models.CharField("beverage name", max_length=2048)                       # Combo, Add Type
    beverage_style = models.ForeignKey(Beverage_Style, on_delete=models.CASCADE)  # Combo, Add Type
    beverage_abv = models.FloatField("alcohol by volume")                              # Float, 1DP

    def __str__(self):
        return "%s" % (self.beverage_name)

    def __unicode__(self):
        return self.__str__()


class MenuModel(models.Model):
    tap_number = models.IntegerField(unique=True)
    tap_number_subtext = models.CharField("text under tap number", max_length=6)
    brewery_name = models.CharField(max_length=255)
    beverage_name = models.CharField(max_length=255)
    beverage_type = models.CharField(max_length=255)
    beverage_price_1 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    beverage_serving_size_1 = models.CharField(max_length=255)
    beverage_price_2 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    beverage_serving_size_2 = models.CharField(max_length=255)
    beverage_serving_graphic_1 = models.ForeignKey(Beverage_Serving_Graphic, on_delete=models.CASCADE, related_name="serving_size_one")  # Combo, Add Type
    beverage_serving_graphic_2 = models.ForeignKey(Beverage_Serving_Graphic, on_delete=models.CASCADE, related_name="serving_size_two")  # Combo, Add Type
    two_serving_sizes = models.BooleanField()
    menu_row = models.IntegerField()
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)  # Combo, Add Type
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)                       # Combo, Add Type
    beverage_serving_size = models.ForeignKey(Beverage_Serving_Size, on_delete=models.CASCADE, verbose_name="menu serving size")  # Combo, Add Type
    beverage_serving_graphic = models.ForeignKey(Beverage_Serving_Graphic, on_delete=models.CASCADE)  # Combo, Add Type

    def __str__(self):
        return "Tap Number:%s" % (self.tap_number)

    def __unicode__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if self.tap_number >= 13:
            self.menu_row = self.tap_number - 12
        else:
            self.menu_row = self.tap_number

        if self.beverage_price_2:
            self.two_serving_sizes = True
        else:
            self.two_serving_sizes = False
        # self.s = slugify(self.q)
        super(MenuModel, self).save(*args, **kwargs)
