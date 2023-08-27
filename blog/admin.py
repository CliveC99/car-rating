from django.contrib import admin
from .models import Post, Category, Comments, Contact

# Logs the model into the admin panel
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Contact)
