from django.shortcuts import render

# Create your views here.

def HomePageView(request):
    var = """This is the first View, \
             that returns the variable on Home Page\
             try to figure out how it works.\
                 Django is MVT framework, which means you first define\
                     your models then your views and templates respectively\
                         Model are used to create database tables while views\
                             are generally used for logic, and templates are used\
                                 to display the content using html css javascript\
                                     """
    return render(request,'home.html',{"data_to_template":var})