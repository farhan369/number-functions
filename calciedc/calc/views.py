from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,'index.html')
def print(request):
    num = int(request.POST['number']) 
    if 'print1' in request.POST:
        flag = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
        if flag:
            return render(request,'result.html',{'value':"not prime"} )
        else:
            return render(request,'result.html',{'value':"prime "} )
    elif 'print2' in request.POST:
        factorial = 1
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num + 1):
                factorial = factorial*i
            return render(request,'result.html',{'value':factorial} )
    elif 'print3' in request.POST:
        if (num % 2) == 0:
            return render(request,'result.html',{'value':"even"} )
        else:
            return render(request,'result.html',{'value':"odd"} )    