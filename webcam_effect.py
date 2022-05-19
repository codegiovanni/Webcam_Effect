import cv2
import numpy as np

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

WIDTH, HEIGHT = 800, 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

cell_width, cell_height = 12, 12
new_width, new_height = int(WIDTH / cell_width), int(HEIGHT / cell_height)

font = cv2.FONT_HERSHEY_SIMPLEX


def effect(image):
    global black_window

    black_window = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    small_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

    for i in range(new_height):
        for j in range(new_width):
            color = small_image[i, j]
            B = int(color[0])
            G = int(color[1])
            R = int(color[2])

            coord = (j * cell_width + cell_width, i * cell_height)

            cv2.circle(black_window, coord, 5, (B, G, R), 2)
            # cv2.circle(black_window, coord, 5, (0, G, 0), 2)
            # cv2.circle(black_window, coord, 5, (0, G, 0), -1)
            # cv2.circle(black_window, coord, 5, (B, G, R), -1)

            # cv2.line(black_window, coord, (coord[0] + 8, coord[1]), (0, G, 0), 1)
            # cv2.line(black_window, (coord[0] + 4, coord[1] - 4), (coord[0] + 4, coord[1] + 4), (0, G, 0), 1)

            # cv2.putText(black_window, 'X', coord, font, 0.4, (B, G, R), 1, cv2.LINE_AA)

while True:

    _, frame = cap.read()

    effect(frame)

    cv2.imshow('result', black_window)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
