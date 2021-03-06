# import the necessary packages
import argparse
import cv2
import numpy as np
import json
 
mapContours = []
selectedContours = []
selectedContoursSignatures = set()
mapImage = None

def getAreaProportion(contour):
    area = cv2.contourArea(contour)
    return area/(mapImage.shape[1]*mapImage.shape[0])

def on_mouse(event, x, y, flags, param):
    global mapImage
    global mapContours
    global selectedContours

    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        contours = find_contours_containing(mapContours, point)
        if contours:
            toHighlight = min(contours, key=lambda cnt: cv2.contourArea(cnt))

            # this is an awful hack, but it works well enough, lol
            flatlist = [item for sublist in toHighlight.tolist() for item in sublist]
            flatlist = [item for sublist in flatlist for item in sublist]
            thlhash = sum(flatlist)
            if thlhash not in selectedContoursSignatures:
                selectedContours.append(toHighlight)
                selectedContoursSignatures.add(thlhash)
                cv2.drawContours(mapImage, [toHighlight] , -1, (0,0,255), 10)
                cv2.imshow("image", mapImage)

def find_contours_containing(contours, point):
    return list(filter(lambda cnt: cv2.pointPolygonTest(cnt, point, False) == 1, contours))

def get_contours(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,240,255,cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    def filterer(cnt, minArea, maxArea):
        area = getAreaProportion(cnt)
        return area > minArea and area < maxArea

    filtered = filter(lambda cnt: filterer(cnt, 0, 1), contours)
    hulls = map(lambda cnt: cv2.convexHull(cnt), filtered)
    approximated = map(lambda cnt: cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True), hulls)

    return list(approximated)

def jsonify_contours(contours):
    json_object = {}
    i = 0

    def normalize_contour(contour):
        return map(lambda cnt: [round(cnt[0]/mapImage.shape[1], 5),
                                round(cnt[1]/mapImage.shape[0], 5)],
                                contour)

    def normalize_bounding_rect(cnt):
        x = cnt[0]/mapImage.shape[1]
        y = cnt[1]/mapImage.shape[0]
        w = cnt[2]/mapImage.shape[1]
        h = cnt[3]/mapImage.shape[0]

        return {'x': round(x, 5), 'y': round(y, 5),
                'w': round(w, 5), 'h': round(h, 5)}

    for arr in contours:
        inner = map(lambda x: x[0], arr.tolist())
        #contour = list(normalize_contour(inner))
        boundingRect = normalize_bounding_rect(cv2.boundingRect(arr))

        room = {}
        #room['contour'] = contour
        room['bounding_box'] = boundingRect
        json_object['room_' + str(i)] = room
        i += 1
    return json.dumps(json_object, indent=2)

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
