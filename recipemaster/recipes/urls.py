from django.conf.urls import patterns, url

from recipemaster.recipes import views
from recipemaster.recipes.feeds import LatestRecipes

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^feed/$', LatestRecipes()),
    url(r'^collections/add/$', views.edit_collection, name='add_collection'),
    url(
        r'^collections/(?P<collection_id>\d+)/delete/$',
        views.delete_collection,
        name='delete_collection'
    ),
    url(
        r'^collections/(?P<collection_id>\d+)/by-tag/(?P<slug>[\w-]+)/$',
        views.tag_filter,
        name='tag_filter'
    ),
    url(
        r'^collections/(?P<collection_id>\d+)/edit/$',
        views.edit_collection,
        name='edit_collection'
    ),
    url(r'^collections/(?P<collection_id>\d+)/$', views.view_collection, name='view_collection'),
    url(
        r'^collections/(?P<collection_id>\d+)/remove/(?P<recipe_id>\d+)/$',
        views.remove_recipe_from_collection,
        name='remove_recipe_from_collection'
    ),
    url(
        r'^collections/(?P<collection_id>\d+)/edit/(?P<recipe_id>\d+)/$',
        views.edit_recipe_in_collection,
        name='edit_recipe_in_collection'
    ),
    url(
        r'^collections/(?P<collection_id>\d+)/add/$',
        views.edit_recipe_in_collection,
        name='add_recipe_to_collection'
    ),
    url(
        r'^collections/(?P<collection_id>\d+)/add_user/$',
        views.add_user_to_collection,
        name='add_user_to_collection'
    ),
)
