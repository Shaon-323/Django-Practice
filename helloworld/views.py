from django.http import HttpResponse
from django.shortcuts import render

todo = [
    {"todo":"Test todo 1"},
    {"todo":"Test todo 2"},
    {"todo":"Test todo 3"},
    {"todo":"Test todo 4"},
    {"todo":"Test todo 5"}
]
def HomePage(request):
    data = 'I love you Mona'
    return render(request, 'index.html',{'data':todo})

def ResultPage(request):
    if request.method == 'POST':
        num1 = request.POST['Number 1']
        num2 = request.POST['Number 2']
        
        data = {
            'num1' : num1,
            'num2' : num2,
        }
        return render(request, 'index.html', {'result': data})