import qrcode
import cv2
import image
import PIL
qrText = input("Enter Text or Url for QR code = ")
root = qrcode.make(qrText)
root.save("code.jpg")
qrc = cv2.QRCodeDetector()
code = qrc.detectAndDecode(cv2.imread("code.jpg"))
print(code)