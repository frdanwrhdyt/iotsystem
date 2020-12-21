from django.contrib import admin

# Register your models here.
from accounts.models import *
from django.contrib.auth.admin import UserAdmin
# account = get_user_model(Account)
admin.site.register(MyUser)
