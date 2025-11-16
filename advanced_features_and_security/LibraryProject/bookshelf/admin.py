from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, UserProfile

# -----------------------
# Custom User Admin
# -----------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Include extra fields in the admin form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register CustomUser with the custom UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# -----------------------
# UserProfile Admin
# -----------------------
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')

# -----------------------
# Book Admin
# -----------------------
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register Book
admin.site.register(Book, BookAdmin)
