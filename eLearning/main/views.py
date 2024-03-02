from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Category, Question
from .forms import *
from django.contrib import messages



def home(request):
     return render(request,'main/home.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'main/article_detail.html', {'article': article})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('main:article_list')
    else:
        form = ArticleForm()
    return render(request, 'main/article_form.html', {'form': form})

@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('main:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/article_form.html', {'form': form})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('main:article_list')
    return render(request, 'main/article_confirm_delete.html', {'article': article})


@login_required
def question_list(request):
    questions = Question.objects.all()
    print(questions)
    return render(request, 'main/question_list.html', {'questions': questions})


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question  
            answer.save()
            return redirect('main:question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'main/question_detail.html', {'question': question, 'answers': answers, 'form': form})


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:question_list')
    else:
        form = QuestionForm()
    print(form)
    return render(request, 'main/question_form.html', {'form': form})
@login_required
def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('main:question_list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'main/question_form.html', {'form': form})
@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('main:question_list')
    return render(request, 'main/question_confirm_delete.html', {'question': question})





@login_required
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = QuizQuestion.objects.filter(quiz=quiz)

    if request.method == 'POST':
        total_marks = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            correct_answer = question.correct_answer
            if user_answer == correct_answer:
                total_marks += 1
            QuizAnswer.objects.create(quiz=quiz, user=request.user, question=question, selected_option=user_answer)
        
        messages.success(request, f'You scored {total_marks} out of {len(questions)}')
        return redirect('main:quiz_list')

    return render(request, 'main/take_quiz.html', {'quiz': quiz, 'questions': questions})
@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'main/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            return redirect('main:my_quiz')
    else:
        form = QuizForm()
    return render(request, 'main/quiz_form.html', {'form': form})
@login_required
def my_quiz(request):
    quiz = Quiz.objects.filter(author=request.user)
    return render(request, 'main/my_quiz.html', {'quiz': quiz})


@login_required
def quiz_question_create(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)

    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz  
            question.save()
            return redirect('main:my_quiz')  
    else:
        form = QuizQuestionForm()
    
    return render(request, 'main/quiz_question_form.html', {'form': form, 'quiz': quiz})
