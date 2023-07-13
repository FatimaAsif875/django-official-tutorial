from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404,render
from django.utils import timezone
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/choice.html", {"question": question})


def newchoice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        new_choice=request.POST["choice"]
        if not new_choice:
            raise KeyError
            
    except (KeyError):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"choice cannot be added"
            }
        )
    else:
        n_choice= Choice(
            question=question,
            choice_text=new_choice,
        )
        n_choice.save()
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    
def resetVote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        for choice in question.choice_set.all():
            choice.votes=0
            choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
def newQs(request):
    if request.method == 'GET':
        return render(request, "polls/newQs.html", {})
    elif request.method == 'POST':
        user_submitted_question = request.POST["question"]
        if not user_submitted_question:
            return render(request, "polls/newQs.html", {
                "error_message":"please enter a valid qs"
            })

        new_question = Question(
            question_text=user_submitted_question,
            pub_date=timezone.now(),
        )
        new_question.save()
    return HttpResponseRedirect(reverse("polls:index",))
