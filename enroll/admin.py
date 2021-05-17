from django.contrib import admin
from .models import User_table
from .forms import StudentRegistration

# Register your models here.
@admin.register(User_table)
class UserAdmin(admin.ModelAdmin):
    form = StudentRegistration
    model = User_table
    list_display = ('id', 'brand', 'invamt', 'invdate', 'cltnamt', 'cltndate', 'customer', 'customercode', 'collectedby', 'paymentmode', 'cheque', 'bank', 'duedate', 'status', 'doptdate', 'utrno', 'bksc')