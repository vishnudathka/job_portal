from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic as views
from core import models,form
from django.urls import reverse_lazy


class Homeview(views.TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = models.JobCreateModel.objects.all()  # Retrieve all job objects
        return context
    
   


class AboutView(views.TemplateView):
    template_name = "core/about.html"

from django.shortcuts import redirect

class ContactView(views.TemplateView):
    template_name = "core/contact.html"
    model = models.ContactModel
    context_object_name = "contact"

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        instance = self.model(name=name, email=email, subject=subject, message=message)
        instance.save()
        return redirect("core:home")  # Provide the URL or view name to redirect to

class ApplyJobView(views.CreateView):
    model = models.ApplyJobModel
    fields = ['name', 'email', 'portfolio', 'resume', 'cover_letter']
    template_name = 'core/jobs/job_detail.html'

    def form_valid(self, form):
        job_id = self.kwargs['pk']
        job = get_object_or_404(models.JobCreateModel, id=job_id)
        company = job.company
        form.instance.job = job
        form.instance.company = company
        form.instance.jobtitle = job.jobtitle
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('core:jobdetail', kwargs={'pk': pk})
      
 

class JoblistView(views.TemplateView):
    template_name = "core/jobs/job_list.html" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = models.JobCreateModel.objects.all()  # Retrieve all job objects
        return context
       

class JobdetailView(views.View):
   template_name = 'core/jobs/job_detail.html'
   model = models.JobCreateModel

   def get(self, request, pk):
        try:
            job = self.model.objects.get(id=pk)
            print(job.jobtitle)  # Debug statement to check the value of the job title
            context = {'job': job}  # Add the 'job' object to the context
            return render(request, self.template_name, context)
        except self.model.DoesNotExist:
            print("Job does not exist")
            # Handle the case when the job does not exist, e.g., show an error message or redirect to a different page

class ErrorView(views.TemplateView):
    template_name = "core/pages/error.html"   

class CategoryView(views.TemplateView):
    template_name = "core/pages/category.html"   

class TestimonialView(views.TemplateView):
    template_name = "core/pages/testimonial.html"   

class JobCreateView(views.CreateView):
    template_name ="core/jobs/jobcreate.html"
    model = models.JobCreateModel
    form_class = form.JobForm
    success_url = reverse_lazy("core:jobs:job_list.html")

class FindjobView(views.ListView):
    template_name = "core/home.html"
    model = models.JobCreateModel
    context_object_name = "jobs"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')       
        category = self.request.GET.get('category')
        location = self.request.GET.get('location')
        if q:
            qs = qs.filter(jobtitle__icontains=q)
        
        if category:
            qs = qs.filter(category__name__icontains=category)
        if location:
            qs = qs.filter(location__icontains=location)    
        
        return qs

