from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaultfilters import pprint
from django.urls import reverse

from learning_logs.forms import TopicForm, EntryForm
from learning_logs.models import Topic, Entry


def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """se for get ira criar um form em branco  """
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)

    """verifica se os dados fornecidos sao validos , caso sim grava os dados no banco com o comando save"""
    if form.is_valid():
        form.save()
        """Redireciona para a pagina topics"""
        return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}

    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

    if form.is_valid():
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}

    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    pprint(entry_id)
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}

    return render(request, 'learning_logs/edit_entry.html', context)
