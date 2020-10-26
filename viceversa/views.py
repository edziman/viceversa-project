from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    user_text_length = len(user_text.split())
    return render(request, 'reverse.html', {
        'usertext': user_text,
        'reversed_text': reversed_text,
        'user_text_length': user_text_length
    })