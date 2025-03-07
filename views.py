from django.shortcuts import render

# Create your views here.
import cv2
from cvzone.PoseModule import PoseDetector
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from .utils import sendSms  # ✅ Import SMS function


detector = PoseDetector()
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

human_detected = False  # Tracks human detection status
sms_sent = False  # Ensures SMS is sent only once per detection

# ✅ Function to detect intrusion & send SMS instantly
def detect_intrusion():
    global human_detected, sms_sent
    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.findPose(img)
        imList, bbox = detector.findPosition(img)

        if len(imList) > 0:  # ✅ Human detected
            if not sms_sent:  # ✅ Prevent duplicate SMS spam
                if sendSms():  # ✅ Send SMS only if successful
                    sms_sent = True  
            human_detected = True  
        else:
            human_detected = False
            sms_sent = False  # Reset when no human is detected

        _, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# ✅ API to check detection status
def detection_status(request):
    return JsonResponse({"human_detected": human_detected})

# ✅ Video streaming
def video_feed(request):
    return StreamingHttpResponse(detect_intrusion(), content_type='multipart/x-mixed-replace; boundary=frame')

# ✅ Render UI
def index(request):
    return render(request, 'index.html')


def capture_photo(request):
    success, img = cap.read()
    if success:
        # ✅ Save image to Desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        filename = f"intrusion_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        filepath = os.path.join(desktop_path, filename)
        cv2.imwrite(filepath, img)

        return JsonResponse({"status": "success", "file": filepath})
    else:
        return JsonResponse({"status": "error", "message": "Camera capture failed"})