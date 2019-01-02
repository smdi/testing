from django.shortcuts import render , get_object_or_404
from django.core.mail import get_connection , send_mail
from django.http import HttpResponseRedirect

from .models import Page
from .forms import ContactForm


def index(request , pagename):

    pagename = '/' + pagename
    pg = get_object_or_404(Page , permalink=pagename)
    context = {

        'title' : pg.title ,
        'last_updated' : pg.update_date ,
        'content' :  pg.bodytext ,
        'page_list':Page.objects.all()

    }
    # assert False
    return render(request,'pages/page.html', context = context)




def contacts(request):

    submitted = False
    if request.method == 'POST' :
        form  =  ContactForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(

                cd['subject'] ,
                cd['message'] ,
                cd.get('email' ,'noreply@example.com') ,
                ['siteowner@example.com'],
                connection= con
            )
            return HttpResponseRedirect('/contacts?submitted = True')
    else :

        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html',
                      {'form': form, 'page_list': Page.objects.all(),
                       'submitted': submitted})





