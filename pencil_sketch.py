"""
Author: Zeeshan Mumtaz
Date: Aug 20, 2024
Description: This Python script will help you to create professional Pencil Sketches

Two main libraries are used which should be installed first using:

pip install numpy==2.1.0               :    Fundamental package for array computing in Python
pip install opencv-python==4.10.0.84   :    Wrapper package for OpenCV python bindings.
"""





import cv2 
import numpy as np

def pencil_sketch(image_path, output_path):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted_gray_image = cv2.bitwise_not(gray_image)

    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21),0)

    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    cv2.imwrite(output_path, pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_image_path = 'IMG_6068.jpg'
output_image_path = 'Pencil_Sketch_' + input_image_path + '.jpg'
pencil_sketch(input_image_path, output_image_path)





# With more dark shade
# import cv2 
# import numpy as np

# def pencil_sketch(image_path, output_path):
#     image = cv2.imread(image_path)
#     if image is None:
#         print("Error: Could not open or find the image.")
#         return

#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     inverted_gray_image = cv2.bitwise_not(gray_image)
#     blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
#     inverted_blurred_image = cv2.bitwise_not(blurred_image)
    
#     pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
#     # Subtract a constant value to make the sketch darker
#     pencil_sketch_image = cv2.subtract(pencil_sketch_image, np.array([30.0]))

#     cv2.imwrite(output_path, pencil_sketch_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# input_image_path = 'IMG_6068.jpg'
# output_image_path = 'Pencil_Sketch_' + input_image_path + '.jpg'
# pencil_sketch(input_image_path, output_image_path)
