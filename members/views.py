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
        "fruits":["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))
