# import json
#
# from django.core.paginator import Paginator
# from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    GenericAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserDetailSerializer, UserListSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserDestroySerializer, LocationSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     self.object_list = self.object_list.order_by('username')
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #
    #     # list(map(lambda x: setattr(x, "first_name", x.first_name), page_obj))
    #     # list(map(lambda x: setattr(x, "last_name", x.last_name), page_obj))
    #
    #
    #     for user in page_obj:
    #         UserListSerializer(page_obj).data['total_ads'] = Ad.objects.filter(
    #             author_id=user.id, is_published="TRUE"
    #         ).all().count()

            # users.append(
            #         {
            #             "id": user.id,
            #             "first_name": user.first_name,
            #             "last_name": user.last_name,
            #             "role": user.role,
            #             "age": user.age,
            #             "locations": user.location.name,
            #             "total_ads": user_ads_qs
            #         }
            #     )
            # return JsonResponse(
            #     {
            #         "items": UserListSerializer(page_obj).data,
            #         "total": paginator.count,
            #         "num_pages": paginator.num_pages,
            #     },
            #     status=200,
            #     safe=False
            # )


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     user = self.get_object()
    #     user_ads_qs = Ad.objects.filter(author_id=user.id, is_published="TRUE").all().count()
    #     UserDetailSerializer(user).data["total_ads"] = user_ads_qs
    #
    #     return JsonResponse(
    #         UserDetailSerializer(user).data,
    #         status=200,
    #     )


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
