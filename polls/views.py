from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
#from django.template import RequestContext,loader
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


def index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]#从数据库中取出最新的5个question
   #这里用到了数据库，其实Django给我们封装了数据库的读写操作，
   # 我们不需要用SQL语句去查询、更新数据库等，我们要做的是用python的方式定义数据库结构(在model.py里面定义数据库)，然后用python的方式去读写内容。

   #The context is a dictionary mapping template variable names to Python objects.
   context = {'latest_question_list':latest_question_list}
   return render(request,'polls/index.html',context)




def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
         #redisplay the question voting form.
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #you should always return an HttpResponseRedirect, after successfully dealing with POST data.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


































