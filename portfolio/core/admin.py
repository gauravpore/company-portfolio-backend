from django.contrib import admin

from .models import Product, Testimonial, TeamMember, Project, MiscData
from django.contrib.admin import ModelAdmin

# Register your models here.
class ProductAdmin(ModelAdmin):
    search_fields = ("product_name",)
    list_display = ("product_name", "image_url", "url", "created_date", "updated_date")


class TestimonialAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "profile", "comment", "created_date", "updated_date")


class TeamMemberAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = (
        "name",
        "profile",
        "image_url",
        "description",
        "linkedin",
        "email",
        "created_date",
        "updated_date",
    )


class ProjectAdmin(ModelAdmin):
    search_fields = ("project_name",)
    list_display = (
        "project_name",
        "description",
        "image_url",
        "url",
        "created_date",
        "updated_date",
    )


class MiscDataAdmin(ModelAdmin):
    search_fields = ("key",)
    list_display = (
        "key",
        "data",
        "created_date",
        "updated_date",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MiscData, MiscDataAdmin)
