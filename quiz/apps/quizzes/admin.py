from django.contrib import admin

from quiz.apps.quizzes.models import Quiz, Question, Option

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
