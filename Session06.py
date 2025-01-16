from ultralytics import YOLO
from ultralytics.solutions import heatmap
import cv2 as cv
import imutils
import time

def track_createHeatmap():
    exportPath=f"export/{time.strftime('%Y%m%d%H%M%S')}.mp4"
    path=f"Video/Iran 001.mp4"
    writer = None
    (W, H) = (None, None)
    vs = cv.VideoCapture(path)
    filterItems=[2]
    model = YOLO("yolo11n.pt",filterItems)
    (grabbed, frame) = vs.read()
    h, w, c = frame.shape
    heatmap_obj = heatmap.Heatmap(colormap=cv.COLORMAP_PARULA,
                         imw=w,
                         imh=h,
                         view_img=False,
                         shape="circle",
                         names=model.names)
    while True:
        (grabbed, frame) = vs.read()
        if not grabbed:
            break
        results = model.track(frame)
        frame = heatmap_obj.generate_heatmap(frame)
        # ---------------------------------------------------
    
        # -------------------------------------------------------
        if writer is None:
            fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
            writer = cv.VideoWriter(exportPath, fourcc, 24,
                                    (frame.shape[1], frame.shape[0]), True)
        writer.write(frame)
        # --------------------------------------------------------------
    
        cv.imshow('image', frame)
    
        cv.waitKey(24)


track_createHeatmap()