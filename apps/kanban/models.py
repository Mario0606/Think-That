from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, help_text='activity name')
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"
        verbose_name = "tag"
        verbose_name_plural = "tags"


class KanbanStyle(models.Model):
    name = models.CharField(max_length=100, help_text='Kanban table name')
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "kanban_styles"
        verbose_name = "kanban_style"
        verbose_name_plural = "kanban_styles"


class Kanban(models.Model):
    name = models.CharField(max_length=100, help_text="Kanban table name")
    kanban_style = models.ForeignKey(KanbanStyle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "kanbans"
        verbose_name = "kanban"
        verbose_name_plural = "kanbans"


class Activity(models.Model):
    name = models.CharField(max_length=100, help_text="activity name")
    tags = models.ManyToManyField(Tag, blank=True)
    kanban = models.ForeignKey(
        Kanban, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "activities"
        verbose_name = "activity"
        verbose_name_plural = "activities"
