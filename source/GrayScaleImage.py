import os
from PIL import Image

path = './GrayScaleImage'
file_name = '4'
format_name = '.png'


def fun():
    input_image = Image.open(path + '/' + file_name + format_name)

    # 二值图
    output_image1 = input_image.convert('1')
    output_image1.save(path + '/' + file_name + '-二值图' + format_name)

    # 8bit灰度图
    output_image2 = input_image.convert('L')  # 灰度值计算公式L = R * 0.299 + G * 0.587+ B * 0.114
    output_image2.save(path + '/' + file_name + '-灰度图' + format_name)

    # 滤波图
    Lim = input_image.convert('L')
    threshold = 185  # 设置滤波大小
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    output_image3 = Lim.point(table, '1')
    output_image3.save(path + '/' + file_name + '-滤波图' + format_name)


def GrayScaleImage():
    if not os.path.exists(path):  # 如果文件夹不存在就创建
        os.mkdir(path)
    fun()


if __name__ == '__main__':
    GrayScaleImage()
