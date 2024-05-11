from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    # Create a members object with all values of the Member model
    mymembers = Member.objects.all().values()
    # Loads the all_members template
    template = loader.get_template("all_members.html")
    
    # Creates an object containing the mymembers object.
    context = {
        "mymembers": mymembers
    }
    # Sends the object to the template.
    # Outputs the HTML that is rendered by the template.
    return HttpResponse(template.render(context, request))


def details(request, id):
    # Gets the id as an argument.
    # Uses the id to locate the correct record in the Member table.
    mymember = Member.objects.get(id=id)

    # Create an object containing the mymember object
    context = {
        "mymember": mymember
    }
    
    # loads the details.html template.
    # Sends the object to the template.
    # Outputs the HTML that is rendered by the template.
    template = loader.get_template("details.html")

    return HttpResponse(template.render(context, request))
    

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


# Add testing view
def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Orange", "Cherry"]
    }

    return HttpResponse(template.render(context, request))

# ***************** Value List *************************

#    mydata = Member.objects.values_list("firstname")

# **************************************** QuerySet Filter ****************************************

# .filter(firstname__startwith="L")  include in the object variable (eg: mydata)
# mydata = Member.objects.filter(firstname__startswith='L').values()

# contains	Contains the phrase
# icontains	Same as contains, but case-insensitive
# date	Matches a date
# day	Matches a date (day of month, 1-31) (for dates)
# endswith	Ends with
# iendswith	Same as endswidth, but case-insensitive
# exact	An exact match
# iexact	Same as exact, but case-insensitive
# in	Matches one of the values
# isnull	Matches NULL values
# gt	Greater than
# gte	Greater than, or equal to
# hour	Matches an hour (for datetimes)
# lt	Less than
# lte	Less than, or equal to
# minute	Matches a minute (for datetimes)
# month	Matches a month (for dates)
# quarter	Matches a quarter of the year (1-4) (for dates)
# range	Match between
# regex	Matches a regular expression
# iregex	Same as regex, but case-insensitive
# second	Matches a second (for datetimes)
# startswith	Starts with
# istartswith	Same as startswith, but case-insensitive
# time	Matches a time (for datetimes)
# week	Matches a week number (1-53) (for dates)
# week_day	Matches a day of week (1-7) 1 is sunday
# iso_week_day	Matches a ISO 8601 day of week (1-7) 1 is monday
# year	Matches a year (for dates)
# iso_year	Matches an ISO 8601 year (for dates)

# **************************** Order By ***********************************************

# mydata = Member.objects.order_by('firstname').values()

# descending order
# mydata = Member.objects.all().order_by('-firstname').values()

# Multiple Order bys
# mydata = Member.objects.all().order_by('lastname', '-id').values()