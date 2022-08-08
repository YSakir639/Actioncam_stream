import cv2
cap = cv2.VideoCapture("rtsp://192.168.1.1/MJPG")
width = 980
height = 520
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width,height))
    cv2.imshow('Video Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

