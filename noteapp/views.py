from django.shortcuts import render
from .forms import NoteForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from noteapp.models import Note
from noteapp.serializers import NoteSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from noteapp.models import Note
from noteapp.serializers import NoteSerializer
# Create your views here.

# def main(request):
#     return render(request, 'index.html')


def main(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)

    return render(request, 'index.html', {'form': form})


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def note_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # notes = Note.objects.all()
            # serializer = NoteSerializer(notes, many=True)
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def note_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        # print(data, serializer)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        print('not valid serializer')
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)


def note_save(request, pk):

    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        # print(data, serializer)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        print('not valid serializer')
        return JSONResponse(serializer.errors, status=400)



