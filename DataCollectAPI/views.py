from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class DataCollectAPI(View):
    template_name='dataCollect/dataCollect.html'

    def get(self, request):
        
        return render(request, self.template_name)

    # def post(self, request):

    #     return render(request, self.template_name)


