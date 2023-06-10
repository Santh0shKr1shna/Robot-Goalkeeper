import numpy as np
import cv2


url = 'http://192.168.1.15:8080/video'

def detectBall():
    cap = cv2.VideoCapture(url)

    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frame rate: ", int(fps), "FPS")

    prevCircle = None

    while True:
        print('New Calculations: ')
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Detecting White Circle
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 30, 255])
        mask_white = cv2.inRange(hsv, lower_white, upper_white)
        res_white = cv2.bitwise_and(frame, frame, mask=mask_white)
        gray_white = cv2.cvtColor(res_white, cv2.COLOR_BGR2GRAY)
        blur_white = cv2.GaussianBlur(gray_white, (5, 5), 0)
        circles_white = cv2.HoughCircles(blur_white, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0,
                                         maxRadius=0)
        # print('Finished white')

        # Detecting Green Circle
        lower_green = np.array([50, 50, 50])
        upper_green = np.array([70, 255, 255])
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
        gray_green = cv2.cvtColor(res_green, cv2.COLOR_BGR2GRAY)
        blur_green = cv2.GaussianBlur(gray_green, (5, 5), 0)
        circles_green = cv2.HoughCircles(blur_green, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

        print("Finished Circles")

        if circles_white is None:
            # print('White: ',circles_white)
            print("Unable to find white")
            return 0

        if circles_green is None:
            # print('Green: ',circles_green)
            print("Unable to find green")
            return 0

        if circles_white is not None and circles_green is not None:
            circles_white = np.uint16(np.around(circles_white))
            circles_green = np.uint16(np.around(circles_green))
            for j in circles_white[0, :]:
                for k in circles_green[0, :]:
                    dist2 = np.sqrt((j[0] - k[0]) ** 2 + (j[1] - k[1]) ** 2)
                    print('White: ', dist2)
                    if (dist2 < 400):
                        # rotate_forward()
                        # time.sleep(10)
                        # rotate_backward()
                        print('Forward Back\n\n')
                        return 1
                    else:
                        # rotate_backward()
                        # time.sleep(10)
                        # rotate_forward()
                        print('Back Forward\n\n')
                        return -1