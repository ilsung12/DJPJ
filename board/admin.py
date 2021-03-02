from django.contrib import admin
from .models import Board

#Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # 여러정보를 알고 싶을때에
admin.site.register(Board, BoardAdmin)    

