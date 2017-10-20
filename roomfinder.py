# import the necessary packages
import argparse
import cv2
import numpy as np
import json
 
mapContours = []
selectedContours = []
mapImage = None
 
def on_mouse(event, x, y, flags, param):
    global mapImage
    global mapContours
    global selectedContours

    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        contours = find_contours_containing(mapContours, point)
        if contours:
            toHighlight = min(contours, key=lambda cnt: cv2.contourArea(cnt))
            selectedContours.append(toHighlight)
            cv2.drawContours(mapImage, [toHighlight] , -1, (0,255,0), 2)
            cv2.imshow("image", mapImage)

def find_contours_containing(contours, point):
    return list(filter(lambda cnt: cv2.pointPolygonTest(cnt, point, False) == 1, contours))

def get_contours(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,240,255,cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    #global mapImage
    #mapImage = thresh
    im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    def filterer(cnt, minArea, maxArea):
        area = cv2.contourArea(cnt)
        return area < maxArea and area > minArea

    filtered = filter(lambda cnt: filterer(cnt, 500, 20000), contours)
    hulls = map(lambda cnt: cv2.convexHull(cnt), filtered)
    approximated = map(lambda cnt: cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True), hulls)

    return list(approximated)

def jsonify_contours(contours):
    json_object = {}
    i = 0
    for arr in contours:
        contour = map(lambda x: x[0], arr.tolist())
        contour = map(lambda cnt: [round(cnt[0]/mapImage.shape[1], 5),
                                   round(cnt[1]/mapImage.shape[0], 5)],
                                   contour)
        json_object['room_' + str(i)] = list(contour)
        i += 1
    return json.dumps(json_object, indent=2)

    #contours = list(map(lambda arr: list(map(lambda x: x[0], arr.tolist())), contours))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = ap.parse_args()

    mapImage = cv2.imread(args.image)
    mapContours = get_contours(mapImage)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("image", 1280, 800)
    cv2.setMouseCallback("image", on_mouse)
     
    while True:
        cv2.imshow("image", mapImage)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    #contours = list(map(lambda arr: list(map(lambda x: x[0], arr.tolist())), selectedContours))
    print(jsonify_contours(selectedContours))
     
    # close all open windows
    cv2.destroyAllWindows()
