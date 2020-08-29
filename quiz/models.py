import random
from collections import OrderedDict
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

User = get_user_model()


class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	quizzes_played = models.IntegerField(default=0)
	total_points = models.IntegerField(default=0)

	def __str__(self):
		return self.user.get_full_name()

	@receiver(post_save, sender=User)
	def create_player(sender, instance, created, **kwargs):
		if created:
			Player.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_player(sender, instance, **kwargs):
		instance.player.save()


class Answer(models.Model):
	text = models.CharField(max_length=200, unique=True)
	questions = models.ManyToManyField('Question', related_name='answers')

	def __str__(self):
		return self.text


class Question(models.Model):
	text = models.TextField(unique=True)
	correct = models.CharField(max_length=200)

	def __str__(self):
		return self.text

	@property
	def answers_list(self):
		al = list(self.answers.values('text')) # answers' list
		random.shuffle(al)
		# alwd = list(OrderedDict.fromkeys(al)) # answers' list without duplicates
		fal_s = al[:3] # final answers' list shortened
		fal = [] # final answers' list
		fal.append(self.correct)
		for a in fal_s:
			fal.append(a['text'])
		random.shuffle(fal)
		return fal
