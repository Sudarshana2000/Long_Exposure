import cv2
import numpy as np

def smoothening(video):
    (bAvg,gAvg,rAvg)=(None,None,None)
    total=0
    cap=cv2.VideoCapture(video)
    while(True):
        res,frame=cap.read()
        if not res:
            break
        (B,G,R)=cv2.split(frame.astype("float"))
        if bAvg is None:
            bAvg=R
            gAvg=G
            rAvg=B
        else:
            bAvg=(bAvg*total + B)/(total+1)
            gAvg=(gAvg*total + G)/(total+1)
            rAvg=(rAvg*total + R)/(total+1)
        total+=1
    avg=cv2.merge([bAvg,gAvg,rAvg]).astype("uint8")
    cap.release()
    return avg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input video path')
    parser.add_argument('output', help='output image path')
    args = parser.parse_args()
    res = smoothening(args.input)
    cv2.imwrite(args.output, res)
    print("Successful!")