from django.shortcuts import render
from django.views.generic import TemplateView
import io
import pandas as pd
from rest_framework import viewsets
from .models import *
from .serializers import *




# Create your views here.

class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()

class CsvUploader(TemplateView):
    template_name = 'mainApp/csvUploader.html'

    def post(self, request):
        context = {
            "messages":[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            #to convert the file object into a string-like objec
            io.StringIO( 
            csv.read().decode("utf-8") #converts the byte content of the file into a UTF-8 encoded string.
            )
        )
        print(csv_data)

        for record in csv_data.to_dict(orient="records"):
            try:
                Students.objects.create(
                    first_name = record['first_name'],
                    last_name = record['last_name'],
                    grades = record['grades'],
                    roll_number = record['roll_number'],
                    section = record['section']
                )
            except Exception as e:
                print("Exception raised during object creation:", e)
                context['exceptions_raised'] = e

        return render(request, self.template_name, context)    