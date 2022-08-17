import cv2
import numpy as np


camera=videoCapture(0)

#Weidht ve Height'ını belirledim.

weidth=int(camera.get(CAP_PROP_FRAME_WIDTH))
height=int(camera.get(CAP_PROP_FRAME_HEIGHT))
print(weidth,height)

#kaydedilecek videonun formatını belirledim.

videotipi= cv2.VideoWriter_fourcc(*'MP4V')


#kayıt kodu.
"""
writer=cv2.VideoWriter(kayıdn adı,kayıtın tipi,fps'si(yavaşlık veya hızlılık),(genişliği,yüksekliği))
"""
writer=cv2.VideoWriter('kayit.mp4',videotipi,50,(weidth,height))


"""
frame: görüntü, çerçeve.
"""
while True:
  ret, frame=camera.read()
  #kayıdımızı döngü boyunca yazma işlemi yapıyoruz.
  writer.write(frame)
  cv2.imshow("canlı görüntü",frame)
  
  if cv2.waitKey(25) & 0xFF==ord("q"):
    break

    
    
camera.release()
#kayıdı bitiriyoruz.
writer.release()
cv2.destroyAllWindows()
