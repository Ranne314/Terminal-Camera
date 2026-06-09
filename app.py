import cv2
ESC = "\033["
RESET = f"{ESC}0m"

def convert_to_ascii(frame):
    chars = " .:-=+*#%@"
    size = cv2.resize(frame, (150, 100))
    result :str = ""

    for i, row in enumerate(size):
        for i2, pixel in enumerate(row):
            r, g, b = pixel
            brightness = int(r) + int(g) + int(b)
            char = chars[brightness // 96]
            result += f"{ESC}38;2;{r};{g};{b}m{char}{RESET}"
        result += "\n"
    return result


cap = cv2.VideoCapture(0)

while __name__ == "__main__":
    ret, frame = cap.read()
    if not ret:
        break
    print(f"{ESC}[H{ESC}[J" + convert_to_ascii(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
