
from django.urls import path

from blog.views import blog_add, blog_comment, blog_delete, blog_details, blog_list, blog_post_like, blog_update, blog_comment

urlpatterns = [
   path('', blog_list, name='list'),
   path('add/', blog_add, name='add'),
   path('list/', blog_list, name='list'),
   path('update/<int:id>/', blog_update, name='update'),
   path('delete/<int:id>/', blog_delete, name='delete'),
   path('details/<int:id>/', blog_details, name='details'),
   path('details/<int:id>/like', blog_post_like, name='like'),
   path('details/<int:id>/comment/', blog_comment, name='comment'),
 

]
