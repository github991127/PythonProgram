import os
from PIL import Image
import os
import numpy as np
import time

path = './GrayScaleImage'
file_name = 'Y'
format_name = '.jpg'


# https://zhuanlan.zhihu.com/p/152456981

def replace_color(img, src_clr, dst_clr):
    ''' 通过矩阵操作颜色替换程序
    @paramimg:图像矩阵
    @paramsrc_clr:需要替换的颜色(r,g,b)
    @paramdst_clr:目标颜色(r,g,b)
    @return替换后的图像矩阵
    '''
    img_arr = np.asarray(img, dtype=np.double)
    # 分离通道
    r_img = img_arr[:, :, 0].copy()
    g_img = img_arr[:, :, 1].copy()
    b_img = img_arr[:, :, 2].copy()
    # 编码
    img = r_img * 256 * 256 + g_img * 256 + b_img
    src_color = src_clr[0] * 256 * 256 + src_clr[1] * 256 + src_clr[2]
    # 索引并替换颜色
    r_img[img == src_color] = dst_clr[0]
    g_img[img == src_color] = dst_clr[1]
    b_img[img == src_color] = dst_clr[2]
    # 合并通道
    dst_img = np.array([r_img, g_img, b_img], dtype=np.uint8)
    # 将数据转换为图像数据(h,w,c)
    dst_img = dst_img.transpose(1, 2, 0)
    return dst_img


def replace_color_tran(img, src_clr, dst_clr):
    ''' 通过遍历颜色替换程序
    @paramimg:图像矩阵
    @paramsrc_clr:需要替换的颜色(r,g,b)
    @paramdst_clr:目标颜色(r,g,b)
    @return替换后的图像矩阵
    '''
    img_arr = np.asarray(img, dtype=np.double)
    dst_arr = img_arr.copy()
    for i in range(img_arr.shape[1]):
        for j in range(img_arr.shape[0]):
            for s in src_clr:
                if (img_arr[j][i] == s)[0] == True:
                    dst_arr[j][i] = dst_clr
    return np.asarray(dst_arr, dtype=np.uint8)


def ColorImage():
    img = Image.open(path + '/' + file_name + format_name).convert('RGB')
    res_img = img.copy()
    count = 20
    matrix_time = 0
    trans_time = 0
    for i in range(count):
        print(i)

    dst_img = img
    src_clr = []
    # for a in range(20):
    #     src_clr.append((a, a, a))
    # x = 10
    # for a in range(x):
    #     for b in range(x):
    #         for c in range(x):
    #             src_clr.append((a, b, c))

    src_clr = [(255, 255, 255)]  # 替换前颜色列表
    dst_clr = [(0, 255, 0)]  # 替换后颜色列表
    print(src_clr)

    start = time.time()
    num = 0
    for s in src_clr:
        dst_img = replace_color(dst_img, s, dst_clr[0])
        if s[0] == s[1] == s[2]:
        # if 1:
            res_img = dst_img
            res_img = Image.fromarray(res_img)
            res_img.save(path + '/' + file_name + '-变色图' + str(s[0]) + format_name)

    end = time.time()
    matrix_time += (end - start)
    print('矩阵操作花费时间：', matrix_time / count)

    # start = time.time()
    # dst_img = replace_color_tran(dst_img, src_clr, dst_clr[0])
    # end = time.time()
    # trans_time += (end - start)
    # print('遍历操作花费时间：', trans_time / count)

    # res_img = dst_img
    # res_img = Image.fromarray(res_img)
    # res_img.save(path + '/' + file_name + '-变色图' + format_name)


if __name__ == '__main__':
    ColorImage()
