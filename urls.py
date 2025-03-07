from django.urls import path
from .views import index, video_feed, detection_status, capture_photo

urlpatterns = [
    path('', index, name='index'),  # Home Page
    path('video_feed/', video_feed, name='video_feed'),  # ✅ Video Streaming Route
    path('detection_status/', detection_status, name='detection_status'),  # API for Detection
]



urlpatterns = [
    path('', index, name='index'),  
    path('video_feed/', video_feed, name='video_feed'),  
    path('detection_status/', detection_status, name='detection_status'),
    path('capture_photo/', capture_photo, name='capture_photo'),  # ✅ Capture Photo URL
]
