from django.db import models
from django.contrib.auth import get_user_model

class Quiz(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name


class Question(models.Model):
	quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title


class Option(models.Model):
	question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class UserQuiz(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
