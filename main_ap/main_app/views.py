from django.views.generic import TemplateView
# from .models import SocialLink
from .models import TopicCategory
from .models import TopicContent
# from .models import SiteOption
from .models import Services
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['topic_category'] = TopicCategory.objects.all().order_by('order')
        for topic in context['topic_category']:
            topic.contents = TopicContent.objects.filter(topic_category=topic.id).order_by('order')
        # print(context['topic_category'])

        return context


def index(request):
    return render(request, 'index.html')


def services(request):
    services_list = Services.objects.values()
    context = {'services_list': services_list}
    return render(request, 'unit.html', context)


def contact(request):
    return render(request, 'contact.html')



def video(request):
    return render(request, 'video.html')



class Home(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['topic_category'] = TopicCategory.objects.all().order_by('order')
        for topic in context['topic_category']:
            topic.contents = TopicContent.objects.filter(topic_category=topic.id).order_by('order')
        # print(context['topic_category'])
        return context
