from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'config/index.html'


class ParticipantsView(TemplateView):
    template_name = 'config/pages/participants.html'


class AllExhibitionsView(TemplateView):
    template_name = 'config/pages/all-exhibitions.html'


class PortfolioView(TemplateView):
    template_name = 'config/pages/portfolio.html'


class PastView(TemplateView):
    template_name = 'config/pages/past.html'
