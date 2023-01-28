from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import IsAuthorOrStaff
from ads.serializers import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroySerializer


def index(request):
    return JsonResponse(
        {
            "status": "ok"
        },
        status=200
    )


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Added lookups to filter ads by category_id,
        keyword in ad name, location_id, and price range
        """

        ad_category = request.GET.get('cat', None)
        if ad_category:
            self.queryset = self.queryset.filter(
                category__id__exact=ad_category
            )

        name_text = request.GET.get('text', None)
        if name_text:
            self.queryset = self.queryset.filter(
                name__icontains=name_text
            )
        location_name = request.GET.get('location', None)
        if location_name:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=location_name
            )

        start_price = request.GET.get('price_from', None)
        end_price = request.GET.get('price_to', None)
        if start_price and end_price:
            self.queryset = self.queryset.filter(
                price__range=(start_price, end_price)
            )

        self.queryset = self.queryset.order_by("-price")

        return super().get(request, *args, *kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthorOrStaff]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [IsAuthorOrStaff]


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
