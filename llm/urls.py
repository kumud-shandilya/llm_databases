from django.urls import path
from llm.views import prompt_to_query

app_name= "llm"
urlpatterns = [
    path('prompt_to_query/', prompt_to_query),
]