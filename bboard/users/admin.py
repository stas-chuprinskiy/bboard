import datetime

from django.contrib import admin
from django.contrib.auth import get_user_model
from main.utils import send_activation_notification

User = get_user_model()


def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письма с требованиями отправлены')


send_activation_notifications.short_description = (
    'Отправка писем с требованиями активации'
)


class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Прошли активацию?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3 дней'),
            ('week', 'Не прошли более недели'),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        if val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(
                is_active=False, is_activated=False, date_joined__date__lt=d
            )
        if val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(
                is_active=False, is_activated=False, date_joined__date__lt=d
            )


class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (
        ('username', 'email'), ('first_name', 'last_name'),
        ('is_active', 'is_activated'), ('is_staff', 'is_superuser'),
        'groups', 'user_permissions', ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)


admin.site.register(User, UserAdmin)
