from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView
from .forms import FormName,Create_choice,Create_new_choice
from django.shortcuts import get_object_or_404

# Create your views here.


def formview(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
            form = FormName()


    return render(request,'polls/login_form.html',{'form':form})

class Index(ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

    

class Question_detail(DetailView):
    template_name = 'polls/detail.html'
    model = Question

class Question_create(CreateView):
    model = Question
    fields = ['question_text']

class Question_update(UpdateView):
    model = Question
    fields = ['question_text']

class Question_delete(DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')



    

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"Please select an option"})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        
#HttpResponseRedirect takes a single argument mainly the reverse function which helps avoid hard coding URL
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

class Result_detail(DetailView):
    template_name = "polls/results.html"
    model = Question

def choice_form(request):
    choice = Create_choice()

    if request.method == "POST":
        choice = Create_choice(request.POST)

        if choice.is_valid():
            q=Question(question_text=choice.cleaned_data['question_text'])
            q.save()


    return render(request,'polls/choice_form.html',{'choice':choice})

def create_new_choice(request,pk):
    form = Create_new_choice()

    if request.method == "POST":
        form = Create_new_choice(request.POST)
        if form.is_valid():
            q = get_object_or_404(Question,pk=pk)
            print(q)
            q.choice_set.create(choice_text=form.cleaned_data['choice_text'],votes=0)
            q.save()

            return HttpResponseRedirect(reverse('polls:detail',args=(pk,)))

    return render(request,'polls/create_choice_form.html',{'form':form})


