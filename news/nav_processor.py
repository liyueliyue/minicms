from .models import Column

nav_dispaly_columns = Column.objects.filter(nav_display=True)

def nav_column(request):
    return {'nav_display_columns':nav_dispaly_columns}