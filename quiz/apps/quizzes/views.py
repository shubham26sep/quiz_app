from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from quiz.apps.quizzes.models import Quiz, UserQuiz
from quiz.apps.quizzes.serializers import (QuizSerializer, QuestionSerializer,
    QuizSubmitSerializer)

class QuizListView(ListAPIView):
    '''
    Api for listing all quizzes
    '''
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListApiView(APIView):
    '''
    Api for listing questions and respective options
    '''
    serializer_class = QuestionSerializer

    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = quiz.questions.prefetch_related('options')
        serializer = self.serializer_class(questions, many=True)
        return Response(serializer.data)


class QuizSubmitApiView(APIView):
    '''
    API for submitting quiz questions
    '''

    serializer_class = QuizSubmitSerializer

    def post(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for data in serializer.validated_data:
            question, option = data['question'], data['option']
            if question.quiz != quiz:
                return Response({'detail': 'Invalid Question'}, status=status.HTTP_400_BAD_REQUEST)
            if option.question != question:
                return Response({'detail': 'Invalid Option'}, status=status.HTTP_400_BAD_REQUEST)

        user_quiz_objects = []
        right_answers = 0
        for data in serializer.validated_data:
            question = data['question']
            option = data['option']
            if option.is_correct:
                right_answers += 1
            user_quiz_objects.append(UserQuiz(user=request.user, 
                                              question=question,
                                              selected_option=option))
        UserQuiz.objects.bulk_create(user_quiz_objects)

        total_questions = quiz.questions.count()
        wrong_answers = total_questions - right_answers
        return Response({'right_answers': right_answers, 'wrong_answers': wrong_answers})
