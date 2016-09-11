from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
#from django.conf import settings
from my_collection import settings

class UserProfile(models.Model):
    """ stores customer order information used with the last order placed; can be attached to the checkout order form
    as a convenience to registered customers who have placed an order in the past.
    
    """
    url = models.URLField()
    home_address = models.TextField()
    # phone_number = models.PhoneNumberField()    
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return 'User Profile for: ' + self.user.username
    
class Friendship(models.Model):
    from_friend = models.ForeignKey(User, related_name='friend_set')
    to_friend = models.ForeignKey(User, related_name='to_friend_set')
    
    def __unicode__(self):
        return u'%s, %s' % (
                            self.from_friend.username,
                            self.to_friend.username
                            )

    class Meta:
        db_table = 'Friendship'
        verbose_name_plural = 'Friendships'
        unique_together = (('to_friend', 'from_friend'), )

class Invitation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    sender = models.ForeignKey(User)
    
    def __unicode__(self):
        return u'%s, %s' % (self.sender.username, self.email)
    
    def send(self):
        subject = u'Invitation to join Deepak Collection network'
        link = 'http://%s/accounts/friend/accept/%s/' % (settings.SITE_HOST, self.code)
        template = get_template('friends/invitation_email.txt')
        context = Context({
            'name': self.name,
            'link': link,
            'sender': self.sender.username,
        })
        message = template.render(context)
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])
            
    class Meta:
        db_table = 'Invitation'
        verbose_name_plural = 'Invitations'
