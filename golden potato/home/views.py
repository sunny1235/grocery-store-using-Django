from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product
from django.contrib.auth.models import  User, auth
from django.contrib import messages as msg

def index(request):
	featured = product.objects.filter(featuredCat = 'yes')
	toprated = product.objects.filter(topRatedPrCat = 'yes')
	latest = product.objects.filter(latestPrCat = 'yes')
	dic = {'featuredPr': featured,'topRatedPr':toprated, 'latestPr':latest}
	return render(request, 'index.html', dic )

def shop(request):
	onOfferPr = product.objects.filter(onOfferCat = 'yes')
	allPr = product.objects.all()
	dic = {'onOfferPr':onOfferPr,'allPr':allPr}
	return render(request, 'shop-grid.html',dic)

def blog(request):
	return render(request, 'blog.html',)

def contact(request):
	return render(request, 'contact.html',)

def details(request,myid):
	viewPr = product.objects.filter(prId = myid)
	relatedPr = product.objects.filter(mainCat = viewPr[0].mainCat)
	dic = {'viewPr':viewPr[0], 'relatedPr':relatedPr}
	return render(request, 'shop-details.html',dic)


def reg(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		password = request.POST.get('password')
		email = request.POST.get('email')
		if User.objects.filter(email = email).exists():
			msg.error(request, 'email Taken !')
			return redirect('/reg')
		elif User.objects.filter(username = username).exists():
			msg.error(request, 'username Taken !')
			return redirect('/reg')
		else:
			newUser = User.objects.create_user(username = username, first_name = fname,last_name = lname, password = password, email = email)
			newUser.save()
			return redirect('/')

	return render(request, 'register.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username =username , password= password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			msg.error(request,'Invalid Credentials')
			return redirect('/login')

	return render(request,'login.html')