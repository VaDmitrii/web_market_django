import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad
from homework_27 import settings


def index(request):
    return JsonResponse(
        {
            "status": "ok"
        },
        status=200
    )


@method_decorator(csrf_exempt, name="dispatch")
class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, *kwargs)

        self.object_list = self.object_list.order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author_id": ad.author.id,
                    'author': ad.author.first_name,
                    "price": ad.price,
                    "description": ad.description,
                    "is_published": ad.is_published,
                    "category_id": ad.category.id,
                    "image": ad.image.url if ad.image else None,
                }
            )
        return JsonResponse(
            {
                "items": ads,
                "total": paginator.count,
                "num_pages": paginator.num_pages
            },
            status=200,
            safe=False
        )


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author.id,
                'author': ad.author.first_name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category.id,
                "image": ad.image.url if ad.image else None,
            },
            status=200,
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data.get("name"),
            author_id=ad_data.get("author_id"),
            price=ad_data.get("price"),
            description=ad_data.get("description"),
            is_published=ad_data.get("is_published"),
            image=request.FILES.get("image"),
            category_id=ad_data.get("category_id"),
        )
        ad.save()

        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author.id,
                'author': ad.author.first_name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category.id,
                "image": ad.image.url if ad.image else None,
            },
            status=200,
            safe=False
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdImageView(UpdateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.object.name,
                "author_id": self.object.author.id,
                'author': self.object.author.first_name,
                "price": self.object.price,
                "description": self.object.description,
                "is_published": self.object.is_published,
                "category_id": self.object.category.id,
                "image": self.object.image.url if self.object.image else None,
            },
            status=200,
            safe=False
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        self.object.name = ad_data.get("name")
        self.object.author_id = self.object.author_id
        self.object.price = ad_data.get("price")
        self.object.description = ad_data.get("description")
        self.object.is_published = ad_data.get("is_published")
        self.object.image = self.object.image
        self.object.category_id = ad_data.get("category_id")

        self.object.save()


        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.object.name,
                "author_id": self.object.author.id,
                'author': self.object.author.first_name,
                "price": self.object.price,
                "description": self.object.description,
                "is_published": self.object.is_published,
                "category_id": self.object.category.id,
                "image": self.object.image.url if self.object.image else None,
            },
            status=200,
            safe=False
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)
