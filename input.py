#!/usr/bin/env python 

import cv2

def inputVideo( vidFile=None ):
    
    assert vidFile is not None

    vidFile = vidFile 
    vid = cv2.VideoCapture( 'videos/' + vidFile )

    while ( vid.isOpened() ):

        ret, frame = vid.read()
        if ret == True:

            cv2.imshow( 'SLAM', frame )

            if cv2.waitKey( 25 ) & 0xFF == ord( 'q' ):
                break
        else:
            break

    vid.release() # release vid vidCapture object

    cv2.destroyAllWindows()


def process_input( img, W, H ):

    img = cv2.resize( img, ( W, H ) )
    


inputVideo( 'test_nyc.mp4' )
