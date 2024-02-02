import cv2
import joblib
import json
import numpy as np
import base64
from wavelet import w2d

__class_name_to_number = {}
__class_number_to_name = {}

__model = None


def get_cv2_image_from_base64_string(b64str):
    '''
    credit: https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
    :param uri:
    :return:
    '''
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def get_cropped_faces_with_two_eyes(img_path, image_base64_data):
    """
    This function takes an image path and returns a cropped face if the image contains two eyes
    """


    face_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_eye.xml')

    if img_path:
        img = cv2.imread(img_path)
    else:
        img = get_cv2_image_from_base64_string(image_base64_data)
    
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    cropped_faces = []
    for (x,y,w,h) in faces:
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_grey)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
            return cropped_faces


def classify_image(image_base64_data, file_path = None):
    imgs = get_cropped_faces_with_two_eyes(file_path, image_base64_data)


    result = []
    for img in imgs:
        scaled_raw_img = cv2.resize(img, (32, 32))
        img_har = w2d(img, 'db1', 5)
        scaled_img_har = cv2.resize(img_har, (32, 32))
        combined_img = np.vstack((scaled_raw_img.reshape(32*32*3,1), scaled_img_har.reshape(32*32,1)))

        len_image_array = 32*32*3 + 32*32

        #the API expects a float datatype. So I am converting it to a float
        # and I am reshaping it because __model.predict expects a 2D array, but I just want to pass in one image
        final = combined_img.reshape(1, len_image_array).astype(float)

    
        result.append({
            #Getting the first result
            'class': result.append(class_number_to_name(__model.predict(final)[0])),
            'class_probability': np.round(__model.predict_proba(final)*100, 2).tolist()[0], #Return the probability that it is the returned driver
            'class_dictionary': __class_name_to_number
        })

        

        
    return result

def load_saved_artifiacts():
    print('loading saved artifacts...')
    global __class_name_to_number
    global __class_number_to_name

    with open('./artifacts/class_dictionary.json', 'r') as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}
    
    global __model
    if __model is None:
        with open('artifacts/saved_model.pkl', 'rb') as f:
            __model = joblib.load(f)
    print('Finished loading saved artifacts')

def get_b64():
    with open('b64.txt') as f:
        return f.read()
    
def class_number_to_name(class_num):
    return __class_number_to_name[class_num]

if __name__ == '__main__':
    load_saved_artifiacts()
    print(classify_image(get_b64(), None)) #works well with base64
    # going to try with image paths
    print(classify_image(None, './test_images/Lewis_test.jpg'))
    print(classify_image(None, './test_images/Seb_test.jpg'))