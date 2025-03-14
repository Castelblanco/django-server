from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {
            "title": "hola",
            "list": [
                {
                    "name": "a",
                    "price": "$"
                },
                {
                    "name": "b",
                    "price": "$$"
                },
                {
                    "name": "c",
                    "price": "$$$"
                },
                {
                    "name": "d",
                    "price": "$$$$$"
                },
            ]
        }
