# from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
#
# from ads.models import Category
# from category.serializers import CategoryDetailSerializer, CategoryCreateSerializer, CategoryUpdateSerializer, \
#     CategoryDestroySerializer, CategoryListSerializer
#
#
# class CatListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryListSerializer
#
#
# class CatDetailView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailSerializer
#
#
# class CatCreateView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateSerializer
#
#
# class CatUpdateView(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryUpdateSerializer
#
#
# class CatDeleteView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDestroySerializer
