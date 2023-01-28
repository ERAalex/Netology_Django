from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Article, Categories, ScopeDecision
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') and flag:
                raise ValidationError('Oсновным может быть только один Тэг')
            if form.cleaned_data.get('is_main') and not flag:
                flag = True
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ScopeDecision
    extra = 4
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [ScopeInline, ]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('scope',)