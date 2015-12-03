from django.db import models


image_type_choices = (
    ('schematic', 'სქემატური'),
    ('render', 'რენდერი'),
    ('photo', 'ფოტო'),
)

flat_commercial_status_choices = (
    ('sold', 'გაყიდულია'),
    ('available', 'იყიდება'),
    ('reserved', 'რეზერვ.'),
)

floor_choices = [(i, i) for i in range(10)]


class Page(models.Model):
    title = models.CharField(max_length=190)
    body = models.TextField()

    def __str__(self):
        return self.title


class Flat(models.Model):
    # title = models.CharField(max_length=190)
    # body = models.TextField()
    floor = models.IntegerField(choices=floor_choices)
    price = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    status = models.CharField(max_length=60, choices=flat_commercial_status_choices, default='available')
    type = models.ForeignKey('FlatType', default=1)
    
    def presented(self):
        return str(self.floor) + ' სართული; ' + str(self.area) + 'კვ.მ.'    

    def __str__(self):
        return str(self.floor) + ' სართული; ' + str(self.area) + 'კვ.მ.; ' + self.get_status_display()


class Image(models.Model):
    title = models.CharField(max_length=190)
    image = models.ImageField(upload_to='images')
    type = models.CharField(max_length=95, choices=image_type_choices, default='photo')
    date_taken = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


flatmeta_choices = (
    ('area', 'ფართობი'),
    ('sqm price', 'კვმ ფასი'),
    ('total price', 'ბინის ფასი'),
    ('conditions', 'ჩაბარების პირობები'),
    ('standard areas', 'სტანდარტული გადატიხრვა'),
)


class FlatMeta(models.Model):
    type = models.CharField(choices=flatmeta_choices, max_length=190)
    value = models.TextField()
    title = models.CharField(max_length=190)

    def __str__(self):
        return self.title


class FlatType(models.Model):
    title = models.CharField(max_length=190)
    descr = models.TextField()
    images = models.ManyToManyField('Image', blank=True)
    meta = models.ManyToManyField('FlatMeta')

    def __str__(self):
        return self.title
