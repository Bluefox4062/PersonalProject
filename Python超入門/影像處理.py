from PIL import Image

image = Image.open('D:/MyProject/F3768/ch05/5-2節/flower.jpg')

# 轉換顏色
red, green, blue = image.split()
convert_image = Image.merge("RGB", (blue, green, red))
convert_image.show()
convert_image.save('rgb_to_bgr.jpg')

# 黑白圖片
black_and_white = image.convert('1')
black_and_white.show()
black_and_white.save('b_and_w.jpg')

# 灰階圖片
gray_image = image.convert('L')
gray_image.show()
gray_image.save('gray_image.jpg')

# 旋轉圖片
image.transpose(Image.ROTATE_90).show()
image.transpose(Image.ROTATE_90).save('rotate_90.jpg')