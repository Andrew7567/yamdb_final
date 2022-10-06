from .models import Category, Genre, Title, GenreTitle, Review, Comment

from django.contrib import admin

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
admin.site.register(Review)
admin.site.register(Comment)
