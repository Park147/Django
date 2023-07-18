from django.contrib import admin
from board.models import Board

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display=("title", "writer", "hit", "post_date")
    

#admin.site.register(Board, BoardAdmin)