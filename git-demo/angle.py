import cv2
import math

path = 'protractor.png'
img = cv2.imread(path)
pointsList = []


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.arrowedLine(img, tuple(pointsList[0]), (x, y), (255, 0, 0), 1)
        cv2.circle(img, (x, y), 5, (255, 0, 0), cv2.FILLED)
        pointsList.append([x, y])
        print(pointsList)


def gradient(pt1, pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])


def getAngle(ptsLt):
    pt1, pt2, pt3 = ptsLt[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2 - m1) / (1 + (m2 * m1)))
    angD = round(math.degrees(angR))
    if angD < 0:
        angD = 180+angD
    cv2.putText(img, str(angD), (pt1[0] - 40, pt1[1] + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
    print(angD)
    return angD

while True:

    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        pointsList = []
        img = cv2.imread(path)
    if cv2.waitKey(1) & 0xFF == ord('l'):
        break
