from stupidArtnet import StupidArtnet
import numpy as np
import cv2 as cv
from time import sleep

# MATRIX
target_size = (36, 108)
target_ratio = target_size[0] / target_size[1]
screen_offset = (0, 0)

# ARTNET
a = StupidArtnet("192.168.1.12")


def waitVid():
    nextDueTime = last_frame_time + frame_interval * cv.getTickFrequency()
    remainingTime = int( (nextDueTime - cv.getTickCount()) * 1000 / cv.getTickFrequency() )
    
    # sleep for the remaining time
    if remainingTime > 3:
        # print(f"Sleeping for {remainingTime-3} ms")
        cv.waitKey(remainingTime-3)

    # busyloop for the remaining time
    # remainingTime = int( (nextDueTime - cv.getTickCount()) * 1000 / cv.getTickFrequency() )
    # print (f"Busylooping for {remainingTime} ms")
    while cv.getTickCount() < nextDueTime:
        continue

    # Late ?
    late_by = (cv.getTickCount() - nextDueTime) / cv.getTickFrequency()
    if late_by > 0.001 and last_frame_time > 0:
        print(f"WARNING: Late by { int(late_by*1000) } ms")


def resizeFrame(frame):
    h, w, _ = frame.shape
    frame_ratio = w / h

    if frame_ratio > target_ratio:
        # crop horizontally
        new_w = int(h * target_ratio)
        offset = (w - new_w) // 2   
        frame = frame[:, offset:offset+new_w]
    else:
        # crop vertically
        new_h = int(w / target_ratio)
        offset = (h - new_h) // 2
        frame = frame[offset:offset+new_h, :]

    return cv.resize(frame, target_size, interpolation=cv.INTER_AREA)


while True:

    # MEDIA
    media = 'small.mp4'

    # OPEN VIDEO
    cap = cv.VideoCapture(media)
    fps = cap.get(cv.CAP_PROP_FPS)
    frame_interval = 1/fps
    last_frame_time = 0

    print(f"PLAY {media} - FPS: {fps}")
    # print(f"Frame interval: { int(frame_interval*1000) } ms")

    # READ VIDEO
    while cap.isOpened():
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("END OF VIDEO.")
            break

        # Crop and resize frame
        matrix = resizeFrame(frame)

        # flip vertically even columns (ZigZag pattern)
        for i in range(1, matrix.shape[1], 2):
            matrix[:, i] = np.flip(matrix[:, i], axis=0)

        # reshape (flatten) matrix to 1D array 
        artnet = np.reshape(matrix, (1, target_size[0]*target_size[1]*3))[0]

        # split artnet into 512 byte universe
        artnet = [artnet[i:i+512] for i in range(0, len(artnet), 512)]

        # fill up the last universe with zeros
        artnet[-1] = np.pad(artnet[-1], (0, 512 - len(artnet[-1])))

        # send artnet
        for i in range(len(artnet)):
            a.set_universe(i)
            a.set(artnet[i])
            a.show()

        # wait for next frame
        waitVid()

        # PUSH frame to artnet
        cv.imshow('frame', matrix)

        last_frame_time = cv.getTickCount()

        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()


cv.destroyAllWindows()