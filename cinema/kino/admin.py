from django.contrib import admin
from .models import Films, Afisha, Director, Genre

# Register your models here.

admin.site.register(Films)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Afisha)