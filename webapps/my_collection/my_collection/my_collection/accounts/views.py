from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.http import HttpResponseRedirect
import smtplib
from django.contrib import messages

from my_collection.accounts.forms import UserProfileForm, RegistrationForm, FriendInviteForm
from my_collection.accounts import profile
from my_collection.accounts.models import Friendship, Invitation

def register(request, template_name="registration/register.html"):
    """ view displaying customer registration form """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RegistrationForm(postdata)
        if form.is_valid():
            #form.save()
            user = form.save(commit=False)  # new
            user.email = postdata.get('email','')  # new
            user.save()  # new
            
            if 'invitation' in request.session:
                # Retrieve the invitation object.
                invitation = Invitation.objects.get(id=request.session['invitation'])
                # Create friendship from user to sender.
                friendship = Friendship(from_friend=user, to_friend=invitation.sender)
                friendship.save()
                
                # Create friendship from sender to user.
                friendship = Friendship (from_friend=invitation.sender, to_friend=user)
                friendship.save()
                
                # Delete the invitation from the database and session.
                invitation.delete()
                del request.session['invitation']
            
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = RegistrationForm()
    page_title = 'User Registration'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def my_account(request, template_name="registration/my_account.html"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'My Account'
    # orders = Order.objects.filter(user=request.user)
    name = request.user.username
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def friends_page(request, username):
    user = get_object_or_404(User, username=username)
    friends = [friendship.to_friend for friendship in user.friend_set.all()]
    variables = RequestContext(request, {
        'friends': friends,
    })
    return render_to_response('friends/friends_page.html', variables)

@login_required
def friend_add(request):
    if 'username' in request.GET:
        friend = get_object_or_404(User, username=request.GET['username'])
        friendship = Friendship(from_friend=request.user, to_friend=friend)
        try:
            friendship.save()
            messages.add_message(request, messages.INFO, 
                                            message=u'%s was added to your friend list.' %
                                            friend.username
                                            )
        except:
            messages.add_message(request, messages.ERROR, 
                                            message=u'%s is already a friend of yours.' %
                                            friend.username
                                            )        
        return HttpResponseRedirect(
                                    '/accounts/friends/%s/' % request.user.username
                                    )
    else:
        raise Http404
    
    
@login_required
def friend_invite(request):
    if request.method == 'POST':
        form = FriendInviteForm(request.POST)
        if form.is_valid():
            invitation = Invitation(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                code=User.objects.make_random_password(20),
                sender=request.user
            )
            invitation.save()
            try:
                invitation.send()
                messages.add_message(request, messages.INFO, 
                                                message=u'An invitation was sent to %s.' %
                                                invitation.email
                                                )
            except smtplib.SMTPException:
                messages.add_message(request, messages.ERROR, 
                                                message=u'An error happened when '
                                                u'sending the invitation to %s.' %
                                                invitation.email 
                )
            return HttpResponseRedirect('/accounts/friend/invite/')
    else:
        form = FriendInviteForm() #GET
            
    variables = RequestContext(request, {
                                             'form': form
                                             })
    return render_to_response('friends/friend_invite.html', variables)

def friend_accept(request, code):
    invitation = get_object_or_404(Invitation, code__exact=code)
    request.session['invitation'] = invitation.id
    return HttpResponseRedirect('/accounts/register/')
