import json
from django.http import HttpResponse
from django.views.generic.edit import FormMixin


class JsonResponseFormMixin(FormMixin):
    def form_valid(self, form):
        if self.request.is_ajax():
            return HttpResponse(json.dumps(form.data), content_type='application/json')
        return super(JsonResponseFormMixin, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return HttpResponse(json.dumps(form.errors), content_type='application/json', status_code=400)
        return super(JsonResponseFormMixin, self).form_valid(form)

