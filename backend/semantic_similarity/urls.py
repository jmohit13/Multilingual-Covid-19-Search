#from django.urls import path
#from . import views
from semantic_similarity.views import Similarity

from django.conf.urls import url

app_name = 'semantic_similarity'
urlpatterns = [
    url(r"^api/v1.0/similarity$", Similarity.as_view(), name="similarity"),

]
