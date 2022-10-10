from calendar import c
from django.contrib import admin

# Register your models here.
from .models import Company,Profile,Reviews,Social,Skills,Post

admin.site.register(Company)
admin.site.register(Profile)
admin.site.register(Reviews)
admin.site.register(Social)
admin.site.register(Skills)
admin.site.register(Post)
# admin.site.register(Like)