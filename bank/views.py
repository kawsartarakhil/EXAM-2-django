from django.shortcuts import render,redirect
from .models import Income,Expence,User

def Home_view(request):
    incomes=Income.objects.filter(user=request.user)
    return render(request,'home.html',context={'incomes':incomes})


def create_income_view(request):
    users=User.objects.all()
    if request.method=='POST':
        amount=request.POST.get('amount')
        category=request.POST.get('catergory')
        if amount and category:
            user=User.objects.filter(user=request.user)
            Income.objects.create(
                amount=amount,
                category=category,
                user=user,
            )
        return redirect('home')
    
    return render(request,'create_income.html',context={'users':users})