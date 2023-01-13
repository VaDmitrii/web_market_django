import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Ad
from homework_27 import settings
from users.models import User


@method_decorator(csrf_exempt, name="dispatch")
class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('username')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            user_ads_qs = Ad.objects.filter(author_id=user.id, is_published="TRUE").all().count()
            users.append(
                {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "age": user.age,
                    "locations": user.location.name,
                    "total_ads": user_ads_qs
                }
            )
        return JsonResponse(
            {
                "items": users,
                "total": paginator.count,
                "num_pages": paginator.num_pages,
            },
            status=200,
            safe=False
        )


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        user_ads_qs = Ad.objects.filter(author_id=user.id, is_published="TRUE").all().count()

        return JsonResponse(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "location": user.location.name,
                "total_ads": user_ads_qs
            },
            status=200,
        )


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            role=user_data.get("role"),
            age=user_data.get("age"),
            location_id=user_data.get("location_id")
        )

        user.save()

        return JsonResponse(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "locations": user.location.name
            },
            status=200
        )


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.first_name = user_data.get("first_name")
        self.object.last_name = user_data.get("last_name")
        self.object.role = user_data.get("role")
        self.object.age = user_data.get("age")
        self.object.location.id = user_data.get("location_id")

        self.object.save()

        return JsonResponse(
            {
                "id": self.object.id,
                "first_name": self.object.first_name,
                "last_name": self.object.last_name,
                "role": self.object.role,
                "age": self.object.age,
                "locations": self.object.location.name
            },
            status=200
        )


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)
