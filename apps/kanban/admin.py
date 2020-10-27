from django.contrib import admin
from .models import Kanban, KanbanStyle, Activity, Tag

admin.site.register(Activity)
admin.site.register(Kanban)
admin.site.register(KanbanStyle)
admin.site.register(Tag)
