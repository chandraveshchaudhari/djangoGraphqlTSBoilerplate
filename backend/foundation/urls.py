from django.urls import path

from . import views

urlpatterns = [

    # ex: /polls/
    path('homepage/', views.index, name='index'),
    # ex: /polls/5/
    path('homepage/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('homepage/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('homepage/<int:question_id>/vote/', views.vote, name='vote'),
]
