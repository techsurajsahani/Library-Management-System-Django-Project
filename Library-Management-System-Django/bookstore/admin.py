from django.contrib import admin
from .models import User,Book,Chat,DeleteRequest,Feedback
# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Chat)
admin.site.register(DeleteRequest)
admin.site.register(Feedback)
