from my_collection.accounts.models import Friendship, Invitation
from django.contrib import admin

class FriendshipInline(admin.TabularInline):
    model = Friendship

class FriendshipAdmin(admin.ModelAdmin):
   pass

admin.site.register(Friendship, FriendshipAdmin)

class InvitationAdmin(admin.ModelAdmin):
   pass


admin.site.register(Invitation, InvitationAdmin)
