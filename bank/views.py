from django.shortcuts import render,redirect
from .models import Income,Expence,User
from django.contrib.auth.decorators import login_required

@login_required
def Home_view(request):
    incomes = Income.objects.filter(user=request.user)
    expences = Expence.objects.filter(user=request.user)
    return render(request,'home.html',context={'incomes':incomes,'expences':expences})

@login_required
def create_income_view(request):
    if request.method=='POST':
        amount=request.POST.get('amount')
        category=request.POST.get('catergory')
        if amount and category:
            Income.objects.create(
                amount=amount,
                catergory=category,
                user=request.user,
            )
        return redirect('home')
    
    return render(request,'create_income.html')


@login_required
def create_expence_view(request):
    if request.method=='POST':
        amount=request.POST.get('amount')
        category=request.POST.get('catergory')
        if amount and category:
            Expence.objects.create(
                amount=amount,
                catergory=category,
                user=request.user,
            )
        return redirect('home')
    
    return render(request,'create_expence.html')



@login_required
def update_income_view(request,pk):
    income=Income.objects.get(id=pk)
    if request.method=='POST':
        income.amount=request.POST.get('amount')
        income.catergory=request.POST.get('catergory')
        income.save()
        return redirect('home')
    
    return render(request,'update_income.html',context={'income':income})


@login_required
def update_expence_view(request,pk):
    expence=Expence.objects.get(id=pk)
    if request.method=='POST':
        expence.amount=request.POST.get('amount')
        expence.catergory=request.POST.get('catergory')
        expence.save()
        return redirect('home')
    
    return render(request,'update_expence.html',context={'expence':expence})



@login_required
def delete_income_view(request,pk):
    income=Income.objects.get(id=pk)
    if request.method=='POST':
        income.delete()
        return redirect('home')
    return render(request,'delete_income.html',context={'income':income})


@login_required
def delete_expence_view(request,pk):
    expence=Expence.objects.get(id=pk)
    if request.method=='POST':
        expence.delete()
        return redirect('home')
    return render(request,'delete_income.html',context={'expence':expence})