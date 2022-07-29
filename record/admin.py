from django.contrib import admin

from .models import Details
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DetailsResource(resources.ModelResource):
   class Meta:
      model = Details
class DetailsAdmin(ImportExportModelAdmin):
   resource_class = DetailsResource

# Register your models here.
admin.site.register(Details, DetailsAdmin)

