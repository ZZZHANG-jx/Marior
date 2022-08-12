import cv2 

crop_im_path = 'the path of crop image in DocUNet dataset'
crop_im = cv2.imread(crop_im_path)
h,w = crop_im.shape[:2]
crop_h = int(h/8)
crop_w = int(w/8)
further_crop_im = crop_im[crop_h:h-crop_h,crop_w:w-crop_w]
