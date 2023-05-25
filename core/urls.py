from django.urls import path
from core import views
app_name="core"
urlpatterns=[
 path("",views.Homeview.as_view(),name="home"),
 path("about/", views.AboutView.as_view(), name="about"),
 path("contact/", views.ContactView.as_view(), name="contact"),
 path('applyjob/<int:pk>/', views.ApplyJobView.as_view(), name='applyjob'),
 path("joblist/", views.JoblistView.as_view(), name="joblist"),
 path("find/", views.FindjobView.as_view(), name="find_job"),
 path("jobdetail/<int:pk>/", views.JobdetailView.as_view(), name="jobdetail"),
 path("category/", views.CategoryView.as_view(), name="category"),
 path("testimonial/", views.TestimonialView.as_view(), name="testimonial"),
 path("error/", views.ErrorView.as_view(), name="error"),
 path("jobcreate/", views.JobCreateView.as_view(), name="jobcreate"),
]