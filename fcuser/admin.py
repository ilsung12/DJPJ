from django.contrib import admin
from .models import Fcuser

#Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    # 여러정보를 알고 싶을때에
admin.site.register(Fcuser, FcuserAdmin)    

