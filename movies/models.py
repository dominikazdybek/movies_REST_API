from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='director')
    actors = models.ManyToManyField(Person, related_name='actors', through='Cast')
    year = models.IntegerField()

    def __str__(self):
            return self.title

    @property
    def actors_list(self):
        return ", ".join([str(t) for t in self.actors.all()])

    @property
    def director_name(self):
        return self.director.name


class Cast(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=128, null=True)

    def __str__(self):
            return self.role




