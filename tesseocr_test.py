from PIL import Image
from tesserocr import PyTessBaseAPI, RIL

image = Image.open('/Users/ankit2204/Downloads/Invoice-a4.jpeg')
with PyTessBaseAPI() as api:
    api.SetImage(image)

    api.SetRectangle(39, 286, 202, 16)
    ocrResult = api.GetUTF8Text()
    conf = api.MeanTextConf()
    print(ocrResult)
    
