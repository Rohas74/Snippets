from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="main_page"),
    path('add_snippet', views.add_snippet_page, name="add_snip_page"),
    path('view_snippets', views.snippets_page, name="view_snip"),
    path('view_snipp/<int:item_id>', views.view_curr_snippet, name="snip_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
