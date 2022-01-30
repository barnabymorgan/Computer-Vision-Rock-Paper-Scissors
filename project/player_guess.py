import cv2
from keras.models import load_model
import numpy as np
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600.0) 
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300.0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


while True: #loops forever  
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    
    cv2.putText(frame, "TEST", (10, 50),  cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

    cv2.imshow('frame', frame)

    # Press q to close the window
    #print(prediction)

    if prediction[0][0] > .7:
        print("Rock")

    elif prediction[0][1] > .7:
        print("Paper")

    elif prediction[0][2] > .7: 
        print("Scissors")

    else:
        print("Nothing")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

def countdown(t):
    while t:
        if t == 3:
            print("ROCK")
        if t == 2:
            print("PAPER")
        if t == 1:
            print("SCISSORS")
        time.sleep(1)
        t -= 1
    print('SHOOT')


def get_player_selection():
    selection = random.randint(0, 2)
    return selection 
