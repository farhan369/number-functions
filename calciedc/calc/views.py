from django.shortcuts import render

# Create your views here.
def calculate(request):
    try:
        num1 = int(request.POST['number1']) 
        num2 = int(request.POST['number2'])


        if 'add' in request.POST :
            r = num1+num2
        elif 'sub' in request.POST :
            r  = num1-num2 
        elif 'mult' in request.POST : 
            r = num1*num2
        elif 'div' in request.POST : 
            r = num1/num2
        return render(request,'result.html',{'value':r} )
    except ValueError:
        return render(request,'result.html',{'value':"WRONG INPUT"} )

def select(request):
    if 'select1' in request.POST:
        return render(request,'binarycalculator.html')
    elif 'select2' in request.POST:
        return render(request,'numberfunctions.html')    

def indexpage(request):
    return render(request,'index.html')
def print(request):
    try:
        num = int(request.POST['number']) 
    except:
        return render(request,'result.html',{'value':"WRONG INPUT"} )    
    if 'print1' in request.POST:
        #prime or not
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
        #factorial
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
        #odd or even
        if (num % 2) == 0:
            return render(request,'result.html',{'value':"even"} )
        else:
            return render(request,'result.html',{'value':"odd"} )    
    
    elif 'print4' in request.POST:
        #Armstrong
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10

# display the result
        if num == sum:
            return render(request,'result.html',{'value':"Armstrong"} )    

            
        else:
            return render(request,'result.html',{'value':"Not Armstrong"} )    
