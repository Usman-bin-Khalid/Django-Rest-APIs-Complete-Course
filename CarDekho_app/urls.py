from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('showroom' , views.Showroom_Viewset , basename = 'showroom')
urlpatterns = [
     path ('list' , views.car_list_view ,  name='car_list'),
     path('<int:pk>' , views.car_detail_view , name= 'car_detail'),
     path('' , include(router.urls)),
     # path('showroom' , views.Showroom_view.as_view(), name='showroom_view'),
     # path('showroom/<int:pk>' , views.Showroom_Details.as_view(), name = 'showroom_details'),
     # path('review' , views.ReviewList.as_view(), name='review_list' ),
     # path('review/<int:pk>' , views.ReviewDetails.as_view() , name='review_detail'),
     path('showroom/<int:pk>/review-create' , views.ReviewCreate.as_view() , name = 'review-create'),
     path('showroom/<int:pk>/review' , views.ReviewList.as_view() , name = 'review_list'),
     path('showroom/review/<int:pk>' , views.ReviewDetail.as_view() , name='review_detail')
]

