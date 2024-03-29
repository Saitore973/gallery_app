from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from . models import Image

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def photos(request):
    
     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    
    photos = Image.objects.all()
    return render(request, 'all-photos/current-photos.html', { "photos":photos})

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def past_days_photos(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(photos_of_day)
#     #     # Converts data from the string Url
#     # date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     # day = convert_dates(date)
#     # html = f'''
#     #     <html>
#     #         <body>
#     #             <h1>Uploads for {day} {date.day}-{date.month}-{date.year}</h1>
#     #         </body>
#     #     </html>
#     #         '''
#     photos = Image.days_photos(date)
#     return render(request, 'all-photos/past-photos.html', {"date": date, "photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


def filter_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.filter_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/filter.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/filter.html',{"message":message})
