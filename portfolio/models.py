from django.db import models


class Language(models.Model):
	name = models.CharField(max_length=50)
	english_name = models.CharField(max_length=50)
	level = models.CharField(max_length=2)

	def __str__(self):
		return "{} ({})".format(self.name, self.english_name)


class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	birthday = models.DateTimeField()
	email_address = models.EmailField()
	website = models.URLField(null=True, blank=True)
	languages = models.ManyToManyField(Language)

	def __str__(self):
		return self.full_name()

	def full_name(self):
		return "{} {}".format(self.first_name, self.last_name)
