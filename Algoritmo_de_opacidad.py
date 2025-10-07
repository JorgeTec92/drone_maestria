from PIL import Image, ImageEnhance

factor = 0.4


for i in range(1,2089):
    if i < 10:
        img = Image.open("D:/Maestria/Imagenes para dataset/data3/images/entrenar/"f'DJI_000{i}.jpg').convert("RGB") # Imágenes del 1 al 9
        img_enhancer = ImageEnhance.Brightness(img)
        enhanced_output = img_enhancer.enhance(factor)
        enhanced_output.save("D:/Maestria/Imagenes para dataset/Imagenes-oscurecidas/"f'DJI_000{i}.jpg')
    elif i < 100:
        img = Image.open("D:/Maestria/Imagenes para dataset/data3/images/entrenar/"f'DJI_00{i}.jpg').convert("RGB") # Imágenes del 10 al 99
        img_enhancer = ImageEnhance.Brightness(img)
        enhanced_output = img_enhancer.enhance(factor)
        enhanced_output.save("D:/Maestria/Imagenes para dataset/Imagenes-oscurecidas/"f'DJI_00{i}.jpg')
    elif i < 1000:
        img = Image.open("D:/Maestria/Imagenes para dataset/data3/images/entrenar/"f'DJI_0{i}.jpg').convert("RGB") # Imágenes del 100 al 999
        img_enhancer = ImageEnhance.Brightness(img)
        enhanced_output = img_enhancer.enhance(factor)
        enhanced_output.save("D:/Maestria/Imagenes para dataset/Imagenes-oscurecidas/"f'DJI_0{i}.jpg')
    elif i >= 1000:
        img = Image.open("D:/Maestria/Imagenes para dataset/data3/images/entrenar/"f'DJI_{i}.jpg').convert("RGB") # Imágenes del 1000 al 1879
        img_enhancer = ImageEnhance.Brightness(img)
        enhanced_output = img_enhancer.enhance(factor)
        enhanced_output.save("D:/Maestria/Imagenes para dataset/Imagenes-oscurecidas/"f'DJI_{i}.jpg')

print("El proceso termino satisfactoriamente")