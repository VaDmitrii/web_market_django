import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def index(request):
    return JsonResponse(
        {
            "status": "ok"
        },
        status=200
    )


@method_decorator(csrf_exempt, name="dispatch")
class CatView(View):

    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append(
                {
                    "id": category.id,
                    "name": category.name
                }
            )
        return JsonResponse(response, status=200, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category()
        category.name = category_data.get("name")

        category.save()

        return JsonResponse(
            {
                "id": category.id,
                "name": category.name
            },
            status=200,
            safe=False
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):

    def get(self, request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price
                }
            )
        return JsonResponse(response, status=200, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad(**ad_data)
        ad.save()

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            },
            status=200,
            safe=False
        )


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse(
            {
                "id": category.id,
                "name": category.name

            },
            status=200,
        )


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            },
            status=200,
        )
