import random
# from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Answer, Question


def index(request, *args, **kwargs):
	qn = Question.objects.count() # question number
	aq = Question.objects.all() # all questions
	q = random.choice(aq) # question
	qa = q.answers_list # question answers
	answers = "<ul style='list-style-type: none;'>"
	for a in qa:
		answers += "<li><button>" + a + "</button></li>"
	answers += "</ul>"
	return HttpResponse("<h3>{}</h3>{}".format(q.text, answers))
