import sys
import argparse
import cv2
import os
from matplotlib import pyplot as plt
from Libraries.ExtractKeypoints.ExtractKeypoints import extractKeypoints


def main(id, visual = False, thres = 20):
    target1 = 'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/signature_recognition/registered/'+str(id)+'.jpg'
    target2 = 'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/signature_recognition/sample/'+str(id)+'.jpg'
    
    if(not os.path.exists(target1)):
        return "Invalid ID. Can't find fingerprint. Please Register"
    img1 = cv2.imread(target1, cv2.IMREAD_GRAYSCALE)
    kp1, des1 = extractKeypoints(img1)

    if(not os.path.exists(target2)):
        return "Signature image not properly uploaded"
    img2 = cv2.imread(target2, cv2.IMREAD_GRAYSCALE)
    kp2, des2 = extractKeypoints(img2)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = sorted(bf.match(des1, des2), key=lambda match: match.distance)

    img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
    img5 = cv2.drawKeypoints(img2, kp2, outImage=None)

    if visual:
        f, axarr = plt.subplots(1, 2)
        axarr[0].imshow(img4)
        axarr[1].imshow(img5)
        plt.show()

        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
        plt.imshow(img3)
        plt.show()

    score = 0
    for match in matches:
        score += match.distance
    if score / len(matches) < thres:
        print("Signature matches with score = {:.2f}".format(100-(score / len(matches))))
        return "Signature matches with score = {:.2f}".format(100-(score / len(matches)))
    else:
        print("Signature does not match")
        return "Signature does not match"
    # print('----|| MODULE ENDED ||----')


# def setup(argv):
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--image', help='Provide signature image path needs to be verified', type=str, default='Data/signature.jpg')
#     parser.add_argument('--ref_image', help='Provide reference signature image path needs to be verified', type=str, default='Data/ref-signature.jpg')
#     parser.add_argument('--thres', help='Signature matching threshold', type=int, default=20)
#     parser.add_argument('--visual', help='Visulisation of result', type=bool, default=True)
#     return parser.parse_args(argv)


# main(101, True)
