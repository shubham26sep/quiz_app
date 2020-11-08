from django.urls import path

from quiz.apps.quizzes import views

urlpatterns = [
    path('quizzes/', views.QuizListView.as_view(), name='quiz-list'),
    path('quizzes/<int:quiz_id>/questions/', views.QuestionListApiView.as_view(), name='question-list'),
    path('quizzes/<int:quiz_id>/submit/', views.QuizSubmitApiView.as_view(), name='quiz-submit'),
]
