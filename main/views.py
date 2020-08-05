import json

import pandas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import MessagesGenerated
from .serializers import FileUploadSerializer


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
        return render(request, 'profiles/gen_sucess.html')


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

