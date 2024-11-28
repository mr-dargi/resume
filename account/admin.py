from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("user_name", "email", "is_admin")
    list_filter = ("is_admin",)
    readonly_fields = ("last_login",)

    fieldsets = (
        ("Main", {"fields": ("user_name", "email", "full_name", "phone_number", "password")}),
        ("Permissions", {"fields": ("is_active", "is_admin", "is_superuser", "last_login", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {"fields": ("user_name", "email", "full_name", "phone_number", "password1", "password2")})
    )

    search_fields = ("user_name", "email", "full_name")
    ordering = ("user_name",)
    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields["is_superuser"].disabled = True
        return form


admin.site.register(User, UserAdmin)
