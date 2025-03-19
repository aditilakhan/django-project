from django.shortcuts import render, HttpResponse

def index(req):
    home = f"<a href='/'>Home</a>"
    library = f"<a href='/library/'>Library</a>"
    exam = f"<a href='/exam/'>Exam</a>"
    events = f"<a href='/events/'>Events</a>"
    return HttpResponse(f"<center><h1>Welcome to exam app <hr>{home}\t{library}\t{exam}\t{events}</h1></center>")

