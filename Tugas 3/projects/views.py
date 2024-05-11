from django.shortcuts import render

def home_screen_view(request):
  print(request.headers)

  return render(request, "base.html", {})