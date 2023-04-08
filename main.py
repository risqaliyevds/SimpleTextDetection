import cv2
import easyocr
import matplotlib.pyplot as plt

# Read image
img_path = 'data/test1.png'
img = cv2.imread(img_path)

# Instance text detector
reader = easyocr.Reader(['en', 'ru'], gpu=False)

# Detect text on image
text_ = reader.readtext(img)

threshold = 0.25

# Drow bbox and text
for i in text_:
    print(i)

    bbox, text, score = i

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 3)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

