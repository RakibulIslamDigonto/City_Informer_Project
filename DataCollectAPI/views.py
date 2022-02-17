from django.shortcuts import render
from django.views.generic import View
import requests

# Create your views here.
class DataCollectAPI(View):
    template_name='dataCollect/dataCollect.html'

    def get(self, request):
        url = 'https://jsonplaceholder.typicode.com/posts'
        respo = requests.get(url)
        converted_data = respo.json()
        print('check data: ',converted_data)
        context={
            'data':converted_data,
        }
        return render(request, self.template_name, context)

    # def post(self, request):

    #     return render(request, self.template_name)


