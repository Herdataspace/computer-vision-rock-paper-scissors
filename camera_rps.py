import cv2
from keras.models import load_model
import numpy as np

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        user_choice_prediction = np.argmax(prediction)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(user_choice_prediction)
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    if user_choice_prediction == 0:
        user_choice = 'Rock'
        print('user_choice')
    elif user_choice_prediction == 1:
        user_choice = 'Paper'
        print('user_choice')
    elif user_choice_prediction == 2:
        user_choice = 'Scissors'
        print('user_choice')
    else:
        user_choice = 'Nothing'
        print('user_choice')
    return user_choice

get_prediction()