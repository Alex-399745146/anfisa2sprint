from django.contrib import admin

from .models import Category, IceCream, Topping, Wrapper

# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline):  # admin.StackedInline and admin.TabularInline
    model = IceCream
    extra = 0 # необязательный


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )


#  Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category', 'is_on_main', 'wrapper')
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)  # Указываем, для каких связанных моделей нужно включить такой интерфейс:


# Регистрируем класс с настройками админки для моделей IceCream и Category:
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
# Регистрируем модели Topping и Wrapper,
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):
admin.site.register(Topping)
admin.site.register(Wrapper)
