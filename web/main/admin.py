from django.contrib import admin
from .models import CustomUser, Product, BlogModel, GymClass
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['user_name', 'full_name', 'rank', 'is_staff']
    fieldsets = (
        (None, {'fields': ('user_name', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'phone', 'address', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Rank Info', {'fields': ('rank',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username',)
    ordering = ('user_name',)

admin.site.register(CustomUser)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('p_id',)

admin.site.register(BlogModel)
admin.site.register(GymClass)