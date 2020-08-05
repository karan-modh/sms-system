import json

import pandas
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import MessagesGenerated
from .serializers import FileUploadSerializer, MessageSerializer


@login_required()
def FormDisplayView(request):
    if request.method == 'GET':
        serializer = FileUploadSerializer()
        return render(request, 'profiles/gen_sms.html', {'serializer': serializer})


@login_required()
def FileUploadView(request):
    if request.method == 'POST':
        if len(request.FILES) == 0:
            tempSerializer = FileUploadSerializer()
            return render(request, 'profiles/gen_sms.html', { 'serializer': tempSerializer})
        data = request.POST['message']
        print(data)
        uploaded_file = request.FILES['file']
        data_frame = pandas.read_excel(uploaded_file, header=None)
        json_str = data_frame.to_json()
        obj = json.loads(json_str)['0']
        contacts = [str(obj[key]) for key in obj]
        contacts = ' '.join(contacts)
        print(contacts)
        messageObject = MessagesGenerated.objects.create_message(data, contacts, request.user)
        messageObject.save()
        return render(request, 'profiles/gen_success.html')


@api_view(('GET', ))
@permission_classes((IsAuthenticated, )) 
def GenMessageView(request):
    auth_token = request.META['HTTP_AUTHORIZATION']
    auth_token = auth_token.split(' ')[-1]
    temp = Token.objects.get(key=auth_token)
    user = temp.user
    print(user)
    try:
        messageObj = MessagesGenerated.objects.get(author=user)
    except MessagesGenerated.DoesNotExist:
        print("I'm here")
        return Response({'Error': "Message for that object not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # serializer = MessageSerializer(messageObj)
        directory = []
        contacts = messageObj.contacts.split(' ')
        for num in contacts:
            temp = {'message': messageObj.message, 'to': str(num)}
            directory.append(temp)
        messageObj.delete()
        return Response({'directory': directory})


def index(request):
    return render(request, 'main/index.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def about(request):
    return render(request, 'main/about.html')


@login_required
def dash(request):
    context = {'user': request.user}
    return render(request, 'profiles/dashboard.html', context)

