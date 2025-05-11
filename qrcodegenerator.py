# pip install qrcode[pil]


import cv2


import qrcode

source = "https://github.com/ohatra/beeeee" # 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,   
)

qr.add_data(source) #adding the source content to the qrcode
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("image_qr.png")

cv2.imshow("QRCODE",cv2.imread("image_qr.png"))
cv2.waitKey(0)
cv2.destroyAllWindows()
