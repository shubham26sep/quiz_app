from rest_framework import serializers

from quiz.apps.quizzes.models import Quiz, Question, Option

class QuizSerializer(serializers.ModelSerializer):

	class Meta:
		model = Quiz
		fields = ('id', 'name')


class OptionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Option
		fields = ('id', 'title')


class QuestionSerializer(serializers.ModelSerializer):
	
	options = OptionSerializer(many=True)

	class Meta:
		model = Question
		fields = ('id', 'title', 'options')


class QuizSubmitSerializer(serializers.Serializer):

	question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
	option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())
