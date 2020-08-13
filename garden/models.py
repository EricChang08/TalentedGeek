from django.db import models
from datetime import date, datetime
from django.urls import reverse

# Create your models here.

############### Data for three main functionalities #################


class profile(models.Model):
    language = models.CharField(max_length=100, blank=True, default="")

    name = models.CharField(max_length=100, blank=True, default="")
    alias = models.CharField(max_length=100, blank=True, default="")
    intro = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.language


class summary(models.Model):
    language = models.CharField(max_length=100, blank=True, default="")

    title = models.CharField(max_length=100000, blank=True, default="")
    description = models.CharField(max_length=100000, blank=True, default="")

    def __str__(self):
        return self.language + ': ' + self.title


class skill(models.Model):
    language = models.CharField(max_length=100, blank=True, default="")

    title = models.CharField(max_length=100, blank=True, default="")
    degree = models.CharField(max_length=100, blank=True, default="")
    description = models.CharField(max_length=100000, blank=True, default="")

    def __str__(self):
        return self.language + ': ' + self.title


class education(models.Model):
    language = models.CharField(max_length=100, blank=True, default="")

    startTime = models.CharField(max_length=100, blank=True, default="")
    endTime = models.CharField(max_length=100, blank=True, default="")
    uni = models.CharField(max_length=100, blank=True, default="")
    major = models.CharField(max_length=100, blank=True, default="")
    perform = models.CharField(max_length=100, blank=True, default="")
    highest = models.BooleanField(default=False)

    #other possible revalent detail
    module = models.CharField(max_length=100000, blank=True, default="")
    reward = models.CharField(max_length=100000, blank=True, default="")
    practice = models.CharField(max_length=100000, blank=True, default="")

    def __str__(self):
        return self.language + ': ' + self.uni


class work(models.Model):
    language = models.CharField(max_length=100, blank=True, default="")

    startTime = models.CharField(max_length=100, blank=True, default="")
    endTime = models.CharField(max_length=100, blank=True, default="")
    comp = models.CharField(max_length=100000, blank=True, default="")
    roleGen = models.CharField(max_length=100000, blank=True, default="")

    def __str__(self):
        return self.language + ': ' + self.comp


class interest(models.Model):
    language = models.CharField(max_length=100, blank=True, default="")

    title = models.CharField(max_length=100000, blank=True, default="")
    description = models.CharField(max_length=100000, blank=True, default="")

    def __str__(self):
        return self.language + ': ' + self.title


class myTag(models.Model):
    tag = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.tag


class myArt(models.Model):
    title = models.CharField(max_length=100000, blank=True, default="")
    abstract = models.CharField(max_length=100000, blank=True, default="")
    content = models.CharField(max_length=1000000, blank=True, default="")
    favor = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    myTag = models.ForeignKey(myTag,
                              on_delete=models.CASCADE,
                              null=True,
                              related_name='article')

    def __str__(self):
        return self.title


class myCom(models.Model):
    content = models.CharField(max_length=100000, blank=True, default="")
    date = models.DateTimeField(auto_now=True)

    myArticle = models.ForeignKey(myArt,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  related_name='comment')

    def __str__(self):
        return self.content


class theProject(models.Model):
    time = models.CharField(max_length=100000, blank=True, default="")
    title = models.CharField(max_length=100000, blank=True, default="")
    description = models.CharField(max_length=100000, blank=True, default="")
    role1 = models.CharField(max_length=100000, blank=True, default="")
    role2 = models.CharField(max_length=100000, blank=True, default="")
    role3 = models.CharField(max_length=100000, blank=True, default="")
    role4 = models.CharField(max_length=100000, blank=True, default="")


############### Data for media #######################################
class images(models.Model):
    title = models.CharField(max_length=100,
                             blank=True,
                             default="",
                             unique=True)
    path = models.ImageField(upload_to="photos", blank=True, unique=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pic_upload:pic_detail', args=[str(self.id)])


class login(models.Model):
    usr = models.CharField(max_length=100000, default="")
    psw = models.CharField(max_length=100000, default="")