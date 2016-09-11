#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# C:\Documents and Settings\dmuley\Collectibles\my_collection\manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add friendship'
    auth_permission_1.content_type = ContentType.objects.get(app_label="accounts", model="friendship")
    auth_permission_1.codename = u'add_friendship'
    auth_permission_1.save()

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change friendship'
    auth_permission_2.content_type = ContentType.objects.get(app_label="accounts", model="friendship")
    auth_permission_2.codename = u'change_friendship'
    auth_permission_2.save()

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete friendship'
    auth_permission_3.content_type = ContentType.objects.get(app_label="accounts", model="friendship")
    auth_permission_3.codename = u'delete_friendship'
    auth_permission_3.save()

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add invitation'
    auth_permission_4.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    auth_permission_4.codename = u'add_invitation'
    auth_permission_4.save()

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change invitation'
    auth_permission_5.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    auth_permission_5.codename = u'change_invitation'
    auth_permission_5.save()

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete invitation'
    auth_permission_6.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    auth_permission_6.codename = u'delete_invitation'
    auth_permission_6.save()

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add user profile'
    auth_permission_7.content_type = ContentType.objects.get(app_label="accounts", model="userprofile")
    auth_permission_7.codename = u'add_userprofile'
    auth_permission_7.save()

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change user profile'
    auth_permission_8.content_type = ContentType.objects.get(app_label="accounts", model="userprofile")
    auth_permission_8.codename = u'change_userprofile'
    auth_permission_8.save()

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete user profile'
    auth_permission_9.content_type = ContentType.objects.get(app_label="accounts", model="userprofile")
    auth_permission_9.codename = u'delete_userprofile'
    auth_permission_9.save()

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add log entry'
    auth_permission_10.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_10.codename = u'add_logentry'
    auth_permission_10.save()

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change log entry'
    auth_permission_11.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_11.codename = u'change_logentry'
    auth_permission_11.save()

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete log entry'
    auth_permission_12.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_12.codename = u'delete_logentry'
    auth_permission_12.save()

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add group'
    auth_permission_13.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_13.codename = u'add_group'
    auth_permission_13.save()

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change group'
    auth_permission_14.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_14.codename = u'change_group'
    auth_permission_14.save()

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete group'
    auth_permission_15.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_15.codename = u'delete_group'
    auth_permission_15.save()

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add message'
    auth_permission_16.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_16.codename = u'add_message'
    auth_permission_16.save()

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change message'
    auth_permission_17.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_17.codename = u'change_message'
    auth_permission_17.save()

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete message'
    auth_permission_18.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_18.codename = u'delete_message'
    auth_permission_18.save()

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add permission'
    auth_permission_19.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_19.codename = u'add_permission'
    auth_permission_19.save()

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change permission'
    auth_permission_20.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_20.codename = u'change_permission'
    auth_permission_20.save()

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete permission'
    auth_permission_21.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_21.codename = u'delete_permission'
    auth_permission_21.save()

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add user'
    auth_permission_22.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_22.codename = u'add_user'
    auth_permission_22.save()

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change user'
    auth_permission_23.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_23.codename = u'change_user'
    auth_permission_23.save()

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete user'
    auth_permission_24.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_24.codename = u'delete_user'
    auth_permission_24.save()

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can add bank'
    auth_permission_25.content_type = ContentType.objects.get(app_label="banknotes", model="bank")
    auth_permission_25.codename = u'add_bank'
    auth_permission_25.save()

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can change bank'
    auth_permission_26.content_type = ContentType.objects.get(app_label="banknotes", model="bank")
    auth_permission_26.codename = u'change_bank'
    auth_permission_26.save()

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete bank'
    auth_permission_27.content_type = ContentType.objects.get(app_label="banknotes", model="bank")
    auth_permission_27.codename = u'delete_bank'
    auth_permission_27.save()

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can add bank note'
    auth_permission_28.content_type = ContentType.objects.get(app_label="banknotes", model="banknote")
    auth_permission_28.codename = u'add_banknote'
    auth_permission_28.save()

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can change bank note'
    auth_permission_29.content_type = ContentType.objects.get(app_label="banknotes", model="banknote")
    auth_permission_29.codename = u'change_banknote'
    auth_permission_29.save()

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete bank note'
    auth_permission_30.content_type = ContentType.objects.get(app_label="banknotes", model="banknote")
    auth_permission_30.codename = u'delete_banknote'
    auth_permission_30.save()

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add country'
    auth_permission_31.content_type = ContentType.objects.get(app_label="banknotes", model="country")
    auth_permission_31.codename = u'add_country'
    auth_permission_31.save()

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change country'
    auth_permission_32.content_type = ContentType.objects.get(app_label="banknotes", model="country")
    auth_permission_32.codename = u'change_country'
    auth_permission_32.save()

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete country'
    auth_permission_33.content_type = ContentType.objects.get(app_label="banknotes", model="country")
    auth_permission_33.codename = u'delete_country'
    auth_permission_33.save()

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add currency unit'
    auth_permission_34.content_type = ContentType.objects.get(app_label="banknotes", model="currencyunit")
    auth_permission_34.codename = u'add_currencyunit'
    auth_permission_34.save()

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change currency unit'
    auth_permission_35.content_type = ContentType.objects.get(app_label="banknotes", model="currencyunit")
    auth_permission_35.codename = u'change_currencyunit'
    auth_permission_35.save()

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete currency unit'
    auth_permission_36.content_type = ContentType.objects.get(app_label="banknotes", model="currencyunit")
    auth_permission_36.codename = u'delete_currencyunit'
    auth_permission_36.save()

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can add mint'
    auth_permission_37.content_type = ContentType.objects.get(app_label="banknotes", model="mint")
    auth_permission_37.codename = u'add_mint'
    auth_permission_37.save()

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can change mint'
    auth_permission_38.content_type = ContentType.objects.get(app_label="banknotes", model="mint")
    auth_permission_38.codename = u'change_mint'
    auth_permission_38.save()

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can delete mint'
    auth_permission_39.content_type = ContentType.objects.get(app_label="banknotes", model="mint")
    auth_permission_39.codename = u'delete_mint'
    auth_permission_39.save()

    auth_permission_40 = Permission()
    auth_permission_40.name = u'Can add comment'
    auth_permission_40.content_type = ContentType.objects.get(app_label="comments", model="comment")
    auth_permission_40.codename = u'add_comment'
    auth_permission_40.save()

    auth_permission_41 = Permission()
    auth_permission_41.name = u'Can moderate comments'
    auth_permission_41.content_type = ContentType.objects.get(app_label="comments", model="comment")
    auth_permission_41.codename = u'can_moderate'
    auth_permission_41.save()

    auth_permission_42 = Permission()
    auth_permission_42.name = u'Can change comment'
    auth_permission_42.content_type = ContentType.objects.get(app_label="comments", model="comment")
    auth_permission_42.codename = u'change_comment'
    auth_permission_42.save()

    auth_permission_43 = Permission()
    auth_permission_43.name = u'Can delete comment'
    auth_permission_43.content_type = ContentType.objects.get(app_label="comments", model="comment")
    auth_permission_43.codename = u'delete_comment'
    auth_permission_43.save()

    auth_permission_44 = Permission()
    auth_permission_44.name = u'Can add comment flag'
    auth_permission_44.content_type = ContentType.objects.get(app_label="comments", model="commentflag")
    auth_permission_44.codename = u'add_commentflag'
    auth_permission_44.save()

    auth_permission_45 = Permission()
    auth_permission_45.name = u'Can change comment flag'
    auth_permission_45.content_type = ContentType.objects.get(app_label="comments", model="commentflag")
    auth_permission_45.codename = u'change_commentflag'
    auth_permission_45.save()

    auth_permission_46 = Permission()
    auth_permission_46.name = u'Can delete comment flag'
    auth_permission_46.content_type = ContentType.objects.get(app_label="comments", model="commentflag")
    auth_permission_46.codename = u'delete_commentflag'
    auth_permission_46.save()

    auth_permission_47 = Permission()
    auth_permission_47.name = u'Can add content type'
    auth_permission_47.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_47.codename = u'add_contenttype'
    auth_permission_47.save()

    auth_permission_48 = Permission()
    auth_permission_48.name = u'Can change content type'
    auth_permission_48.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_48.codename = u'change_contenttype'
    auth_permission_48.save()

    auth_permission_49 = Permission()
    auth_permission_49.name = u'Can delete content type'
    auth_permission_49.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_49.codename = u'delete_contenttype'
    auth_permission_49.save()

    auth_permission_50 = Permission()
    auth_permission_50.name = u'Can add flat page'
    auth_permission_50.content_type = ContentType.objects.get(app_label="flatpages", model="flatpage")
    auth_permission_50.codename = u'add_flatpage'
    auth_permission_50.save()

    auth_permission_51 = Permission()
    auth_permission_51.name = u'Can change flat page'
    auth_permission_51.content_type = ContentType.objects.get(app_label="flatpages", model="flatpage")
    auth_permission_51.codename = u'change_flatpage'
    auth_permission_51.save()

    auth_permission_52 = Permission()
    auth_permission_52.name = u'Can delete flat page'
    auth_permission_52.content_type = ContentType.objects.get(app_label="flatpages", model="flatpage")
    auth_permission_52.codename = u'delete_flatpage'
    auth_permission_52.save()

    auth_permission_53 = Permission()
    auth_permission_53.name = u'Can add session'
    auth_permission_53.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_53.codename = u'add_session'
    auth_permission_53.save()

    auth_permission_54 = Permission()
    auth_permission_54.name = u'Can change session'
    auth_permission_54.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_54.codename = u'change_session'
    auth_permission_54.save()

    auth_permission_55 = Permission()
    auth_permission_55.name = u'Can delete session'
    auth_permission_55.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_55.codename = u'delete_session'
    auth_permission_55.save()

    auth_permission_56 = Permission()
    auth_permission_56.name = u'Can add site'
    auth_permission_56.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_56.codename = u'add_site'
    auth_permission_56.save()

    auth_permission_57 = Permission()
    auth_permission_57.name = u'Can change site'
    auth_permission_57.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_57.codename = u'change_site'
    auth_permission_57.save()

    auth_permission_58 = Permission()
    auth_permission_58.name = u'Can delete site'
    auth_permission_58.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_58.codename = u'delete_site'
    auth_permission_58.save()

    auth_permission_59 = Permission()
    auth_permission_59.name = u'Can add tag'
    auth_permission_59.content_type = ContentType.objects.get(app_label="tagging", model="tag")
    auth_permission_59.codename = u'add_tag'
    auth_permission_59.save()

    auth_permission_60 = Permission()
    auth_permission_60.name = u'Can change tag'
    auth_permission_60.content_type = ContentType.objects.get(app_label="tagging", model="tag")
    auth_permission_60.codename = u'change_tag'
    auth_permission_60.save()

    auth_permission_61 = Permission()
    auth_permission_61.name = u'Can delete tag'
    auth_permission_61.content_type = ContentType.objects.get(app_label="tagging", model="tag")
    auth_permission_61.codename = u'delete_tag'
    auth_permission_61.save()

    auth_permission_62 = Permission()
    auth_permission_62.name = u'Can add tagged item'
    auth_permission_62.content_type = ContentType.objects.get(app_label="tagging", model="taggeditem")
    auth_permission_62.codename = u'add_taggeditem'
    auth_permission_62.save()

    auth_permission_63 = Permission()
    auth_permission_63.name = u'Can change tagged item'
    auth_permission_63.content_type = ContentType.objects.get(app_label="tagging", model="taggeditem")
    auth_permission_63.codename = u'change_taggeditem'
    auth_permission_63.save()

    auth_permission_64 = Permission()
    auth_permission_64.name = u'Can delete tagged item'
    auth_permission_64.content_type = ContentType.objects.get(app_label="tagging", model="taggeditem")
    auth_permission_64.codename = u'delete_taggeditem'
    auth_permission_64.save()

    from django.contrib.auth.models import Group


    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'dmuley'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'd@d.com'
    auth_user_1.password = u'sha1$f6af1$e87d4a235b92014ff2b0e8ca2d082ed66df78486'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2012, 5, 7, 10, 47, 12, 359000)
    auth_user_1.date_joined = datetime.datetime(2012, 4, 14, 23, 44, 32, 31000)
    auth_user_1.save()

    auth_user_2 = User()
    auth_user_2.username = u't1'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.password = u'sha1$93b98$86699aae0e91b2b885523e7ebe4bb1b9874322e3'
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.is_superuser = False
    auth_user_2.last_login = datetime.datetime(2012, 4, 15, 12, 14, 11, 578000)
    auth_user_2.date_joined = datetime.datetime(2012, 4, 14, 23, 48, 19, 781000)
    auth_user_2.save()

    auth_user_3 = User()
    auth_user_3.username = u't2'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.password = u'sha1$ab452$edd92a1af86d4acf2483e9f2db72f6c8df34fbfb'
    auth_user_3.is_staff = False
    auth_user_3.is_active = True
    auth_user_3.is_superuser = False
    auth_user_3.last_login = datetime.datetime(2012, 4, 15, 12, 12, 11, 437000)
    auth_user_3.date_joined = datetime.datetime(2012, 4, 15, 12, 12, 11, 437000)
    auth_user_3.save()

    from django.contrib.auth.models import Message


    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'254a38161d2128f8042d775e6c7134b4'
    django_session_1.session_data = u'NTQ1ZjBjMmI4YjUzYTMwZTI5NTc5MGJjYzA3OTA4ZWE4ZGVmYmFlYjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSVteV9jb2xsZWN0aW9uLmVtYWlsLWF1dGguRW1haWxCYWNrZW5kcQNVDV9h\ndXRoX3VzZXJfaWRxBEsBdS4=\n'
    django_session_1.expire_date = datetime.datetime(2012, 5, 4, 17, 14, 43, 435000)
    django_session_1.save()

    django_session_2 = Session()
    django_session_2.session_key = u'28ff8d81d3239977437a099463dc3584'
    django_session_2.session_data = u'NWQ2ZjkwYzg5YTkwNGI4ZGM3MGUwNTkyNmJlMDYzZGRlNDgwNDkyNDqAAn1xAS4=\n'
    django_session_2.expire_date = datetime.datetime(2012, 5, 21, 11, 2, 33, 125000)
    django_session_2.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'example.com'
    django_site_1.name = u'example.com'
    django_site_1.save()

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="banknotes", model="banknote")
    django_admin_log_1.object_id = u'1'
    django_admin_log_1.object_repr = u'dmuley, bb, bb'
    django_admin_log_1.action_flag = 1
    django_admin_log_1.change_message = u''
    django_admin_log_1.save()

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="banknotes", model="currencyunit")
    django_admin_log_2.object_id = u'1'
    django_admin_log_2.object_repr = u'rr - ttt(rrr)'
    django_admin_log_2.action_flag = 1
    django_admin_log_2.change_message = u''
    django_admin_log_2.save()

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
    django_admin_log_3.user = auth_user_1
    django_admin_log_3.content_type = ContentType.objects.get(app_label="banknotes", model="mint")
    django_admin_log_3.object_id = u'1'
    django_admin_log_3.object_repr = u'nn'
    django_admin_log_3.action_flag = 1
    django_admin_log_3.change_message = u''
    django_admin_log_3.save()

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2012, 5, 7, 10, 53, 29, 609000)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="banknotes", model="bank")
    django_admin_log_4.object_id = u'1'
    django_admin_log_4.object_repr = u'bb'
    django_admin_log_4.action_flag = 1
    django_admin_log_4.change_message = u''
    django_admin_log_4.save()

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2012, 5, 7, 10, 53, 26, 765000)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="banknotes", model="country")
    django_admin_log_5.object_id = u'1'
    django_admin_log_5.object_repr = u'bb'
    django_admin_log_5.action_flag = 1
    django_admin_log_5.change_message = u''
    django_admin_log_5.save()

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 718000)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_6.object_id = u'1'
    django_admin_log_6.object_repr = u'dmuley, d@d.com'
    django_admin_log_6.action_flag = 3
    django_admin_log_6.change_message = u''
    django_admin_log_6.save()

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 703000)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_7.object_id = u'2'
    django_admin_log_7.object_repr = u'dmuley, d@d.com'
    django_admin_log_7.action_flag = 3
    django_admin_log_7.change_message = u''
    django_admin_log_7.save()

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 687000)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_8.object_id = u'4'
    django_admin_log_8.object_repr = u'dmuley, d@d.com'
    django_admin_log_8.action_flag = 3
    django_admin_log_8.change_message = u''
    django_admin_log_8.save()

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 687000)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_9.object_id = u'3'
    django_admin_log_9.object_repr = u'dmuley, d@d.com'
    django_admin_log_9.action_flag = 3
    django_admin_log_9.change_message = u''
    django_admin_log_9.save()

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 671000)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_10.object_id = u'6'
    django_admin_log_10.object_repr = u'dmuley, d@d.com'
    django_admin_log_10.action_flag = 3
    django_admin_log_10.change_message = u''
    django_admin_log_10.save()

    django_admin_log_11 = LogEntry()
    django_admin_log_11.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 671000)
    django_admin_log_11.user = auth_user_1
    django_admin_log_11.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_11.object_id = u'5'
    django_admin_log_11.object_repr = u'dmuley, d@d.com'
    django_admin_log_11.action_flag = 3
    django_admin_log_11.change_message = u''
    django_admin_log_11.save()

    django_admin_log_12 = LogEntry()
    django_admin_log_12.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 656000)
    django_admin_log_12.user = auth_user_1
    django_admin_log_12.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_12.object_id = u'7'
    django_admin_log_12.object_repr = u'dmuley, d@d.com'
    django_admin_log_12.action_flag = 3
    django_admin_log_12.change_message = u''
    django_admin_log_12.save()

    django_admin_log_13 = LogEntry()
    django_admin_log_13.action_time = datetime.datetime(2012, 5, 7, 10, 53, 1, 640000)
    django_admin_log_13.user = auth_user_1
    django_admin_log_13.content_type = ContentType.objects.get(app_label="accounts", model="invitation")
    django_admin_log_13.object_id = u'8'
    django_admin_log_13.object_repr = u'dmuley, d@d.com'
    django_admin_log_13.action_flag = 3
    django_admin_log_13.change_message = u''
    django_admin_log_13.save()

    django_admin_log_14 = LogEntry()
    django_admin_log_14.action_time = datetime.datetime(2012, 4, 15, 12, 14, 53, 921000)
    django_admin_log_14.user = auth_user_1
    django_admin_log_14.content_type = ContentType.objects.get(app_label="accounts", model="friendship")
    django_admin_log_14.object_id = u'2'
    django_admin_log_14.object_repr = u't1, t2'
    django_admin_log_14.action_flag = 1
    django_admin_log_14.change_message = u''
    django_admin_log_14.save()

    django_admin_log_15 = LogEntry()
    django_admin_log_15.action_time = datetime.datetime(2012, 4, 15, 12, 12, 11, 437000)
    django_admin_log_15.user = auth_user_1
    django_admin_log_15.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_15.object_id = u'3'
    django_admin_log_15.object_repr = u't2'
    django_admin_log_15.action_flag = 1
    django_admin_log_15.change_message = u''
    django_admin_log_15.save()

    django_admin_log_16 = LogEntry()
    django_admin_log_16.action_time = datetime.datetime(2012, 4, 14, 23, 48, 22, 406000)
    django_admin_log_16.user = auth_user_1
    django_admin_log_16.content_type = ContentType.objects.get(app_label="accounts", model="friendship")
    django_admin_log_16.object_id = u'1'
    django_admin_log_16.object_repr = u'dmuley, t1'
    django_admin_log_16.action_flag = 1
    django_admin_log_16.change_message = u''
    django_admin_log_16.save()

    django_admin_log_17 = LogEntry()
    django_admin_log_17.action_time = datetime.datetime(2012, 4, 14, 23, 48, 19, 796000)
    django_admin_log_17.user = auth_user_1
    django_admin_log_17.content_type = ContentType.objects.get(app_label="auth", model="user")
    django_admin_log_17.object_id = u'2'
    django_admin_log_17.object_repr = u't1'
    django_admin_log_17.action_flag = 1
    django_admin_log_17.change_message = u''
    django_admin_log_17.save()

    from django.contrib.flatpages.models import FlatPage


    from django.contrib.comments.models import Comment


    from django.contrib.comments.models import CommentFlag


    from tagging.models import Tag


    from tagging.models import TaggedItem


    from my_collection.banknotes.models import Country

    Country_1 = Country()
    Country_1.name = u'bb'
    Country_1.url = u''
    Country_1.is_active = True
    Country_1.description = u''
    Country_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
    Country_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
    Country_1.save()

    from my_collection.banknotes.models import CurrencyUnit

    CurrencyInfo_1 = CurrencyUnit()
    CurrencyInfo_1.country = Country_1
    CurrencyInfo_1.code = u'rr'
    CurrencyInfo_1.symbol = u'rrr'
    CurrencyInfo_1.unit = u'ttt'
    CurrencyInfo_1.is_subunit = False
    CurrencyInfo_1.url = u''
    CurrencyInfo_1.is_active = True
    CurrencyInfo_1.description = u''
    CurrencyInfo_1.created_at = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
    CurrencyInfo_1.updated_at = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
    CurrencyInfo_1.save()

    from my_collection.banknotes.models import Mint

    Mint_1 = Mint()
    Mint_1.name = u'nn'
    Mint_1.country = Country_1
    Mint_1.url = u''
    Mint_1.is_active = True
    Mint_1.description = u''
    Mint_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
    Mint_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
    Mint_1.save()

    from my_collection.banknotes.models import Bank

    Bank_1 = Bank()
    Bank_1.name = u'bb'
    Bank_1.country = Country_1
    Bank_1.url = u''
    Bank_1.is_active = True
    Bank_1.description = u''
    Bank_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 29, 593000)
    Bank_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 29, 593000)
    Bank_1.save()

    from my_collection.banknotes.models import BankNote

    BankNote_1 = BankNote()
    BankNote_1.user = auth_user_1
    BankNote_1.bank = Bank_1
    BankNote_1.mint = Mint_1
    BankNote_1.unit = CurrencyInfo_1
    BankNote_1.value = 4
    BankNote_1.signed_by = u''
    BankNote_1.series = u''
    BankNote_1.serial_number = u''
    BankNote_1.material = u'Paper'
    BankNote_1.obverse_img = u'photos/2012/05/07/Newzeland-10-shillings-back.jpg'
    BankNote_1.obverse_desc = u''
    BankNote_1.reverse_img = u'photos/2012/05/07/Newzeland-10-shillings-front.jpg'
    BankNote_1.reverse_desc = u''
    BankNote_1.grade = u'UNC'
    BankNote_1.status = u'In-circulation'
    BankNote_1.main_color = u''
    BankNote_1.issue_date = datetime.date(2012, 5, 7)
    BankNote_1.dimensions = u''
    BankNote_1.url = u''
    BankNote_1.tags_input = u''
    BankNote_1.is_active = True
    BankNote_1.description = u''
    BankNote_1.created_at = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
    BankNote_1.updated_at = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
    BankNote_1.save()

    from my_collection.accounts.models import UserProfile


    from my_collection.accounts.models import Friendship

    Friendship_1 = Friendship()
    Friendship_1.from_friend = auth_user_1
    Friendship_1.to_friend = auth_user_2
    Friendship_1.save()

    Friendship_2 = Friendship()
    Friendship_2.from_friend = auth_user_2
    Friendship_2.to_friend = auth_user_3
    Friendship_2.save()

    Friendship_3 = Friendship()
    Friendship_3.from_friend = auth_user_1
    Friendship_3.to_friend = auth_user_3
    Friendship_3.save()

    from my_collection.accounts.models import Invitation


