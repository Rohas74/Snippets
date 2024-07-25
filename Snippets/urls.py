from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="main_page"),
    path('snippets/add', views.add_snippet_page, name="add_snip_page"),
    path('snippets/view', views.snippets_page, name="view_snip"),
    path('snippets/<int:item_id>', views.view_curr_snippet, name="snip_detail"),
    path('snippets/create', views.create_snippet, name="create_snippet"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
