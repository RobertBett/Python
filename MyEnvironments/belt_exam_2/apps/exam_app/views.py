from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from .models import *
def index(request):
    return render(request,'exam_app/index.html')
def display(request):
    all_travelers = User.objects.all()
    this_travler = User.objects.get(id=int(request.session['user']['id']))
    all_trips = Trip.objects.all()
    trips = this_travler.trips.all()
    exclude = User.objects.exclude(id=int(request.session['user']['id']))

    print all_travelers[0].name
    # others = exclude.trips.all
    # print trips
    # print others
    print "display method reached"
    return render(request,'exam_app/display.html',{'trips':trips,'exclude':exclude,'all_travelers':all_travelers})
# user = thisauthor.books.all()
# book1authors = book1.authors.all()
# trips = this_travler.trips.all_trips

def create_user(request):
    print "create_user method reached"
    result = User.manager.makeUser(request.POST)
    if result[0] == True:
        request.session['user'] = result[1] # create a login session for the new user
        return redirect('/travels')
    for key, message in result[1].iteritems():
        messages.error(request, message)
        return redirect('/main')

    return redirect('/travels')
def show_users(request):
    return render(request,'/users.html')
def user(request):
    print "user method reached"
    return redirect('/travels')
def login(request):
    result = User.manager.login(request.POST)
    if result[0] == True:
        request.session['user'] = result[1]
        return redirect('/travels')
    for key, message in result[1].iteritems():
        messages.error(request, message)
    return redirect('/main')
def logout(request):
    request.session.clear()
    request.session['user'] = False
    print request.session['user']
    return redirect('/main')
def trip(request,id):
    user = User.objects.exclude(id=int(request.session['user']['id']))
    trip = Trip.objects.get(id=int(id))
    return render(request,'exam_app/profile.html',{'trip':trip,'user':user})
def add_trip(request):
    return render(request,'exam_app/add.html')
def create_trip(request):
    destination = request.POST['destination']
    desc = request.POST['desc']
    start = request.POST['start']
    end = request.POST['end']
    if len(str(destination))<1 or len(str(desc)) < 1 :
        return HttpResponse("No empty fields")
    Trip.objects.create(destination=destination,desc=desc,start=start,end=end)
    last_trip = Trip.objects.last()
    this_user = User.objects.get(id=int(request.session['user']['id']))
    this_user.trips.add(last_trip)
    return redirect('/travels')
def join(request,id):
    this_trip = Trip.objects.get(id=int(id))
    user_id = int(request.session['user']['id'])
    joiner = User.objects.get(id=user_id)
    this_trip.users.add(joiner)
    return redirect('/travels')
def remove(request, id):
    this_trip = Trip.objects.get(id=int(id))
    user_id = int(request.session['user']['id'])
    joiner = User.objects.get(id=user_id)
    this_trip.users.remove(joiner)
    return redirect('/travels')



# Create your views here.
