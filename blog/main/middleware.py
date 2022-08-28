from . import models
import logging

logger = logging.getLogger(__name__)

class HeaderMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        categories = [x.slug for x in models.BlogPostCategory.objects.all()]
        logger.info(f'running the middle ware {categories}')
        request.session['categories'] = categories
        
        return response