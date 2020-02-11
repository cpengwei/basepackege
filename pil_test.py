# encoding:utf-8

import os
import math
from PIL import Image
from wxpy import Bot


# 获取保存图片路径
def creat_dir(dirname='picture'):
    base_dir = r'/Users/caopengfei/Documents/python/'
    act_dir = base_dir + '{}/'.format(dirname)
    if not os.path.exists(act_dir):
        os.mkdir(act_dir)
    return act_dir


# 获取微信头像并保存到指定目录
def save_picture(path):
    bot = Bot()
    freinds = bot.friends(update=True)  #:rtype: :class:`wxpy.Chats`
    for freind in freinds:
        freind_name = freind.name
        # 获取每个好友的头像,以名称命名的话，同名的情况下会替换
        freind.get_avatar(path + '{}.jpg'.format(freind_name))
    print('微信头像获取完成！')


# 头像拼接
def join_picture(path):
    # 获取头像数量
    num = len(os.listdir(path))
    # 设置拼图大小
    image_size = 2560
    # 获取每个头像应该设置的大小
    each_picture = math.ceil(2560 / math.floor(math.sqrt(num)))
    # 拼图中每行每列的头像个数
    x_num = math.ceil(math.floor(math.sqrt(num)))
    y_num = math.ceil(math.floor(math.sqrt(num)))
    # 创建一个新的拼图
    image = Image.new('RGB', (each_picture * x_num, each_picture * y_num))
    # 设置两个值，用例每行每列每个头像顺序排列
    x = 0
    y = 0
    # 遍历目录头像
    for root, dirs, files in os.walk(path):
        for file in files:
            # 处理头像无法读取的异常
            try:
                with Image.open(root + file) as img:
                    # 修改每个头像的大小
                    img = img.resize((each_picture, each_picture))
                    # 黏贴每个头像到拼图中
                    image.paste(img, (x * each_picture, y * each_picture))
                    x += 1
                    # 如果每行头像满了，则换行再黏贴
                    if x == x_num:
                        x = 0
                        y += 1
            except Exception as e:
                print('打开头像:{} 失败！'.format(file))
    # 保存最终的拼图
    image.save(os.getcwd() + '/微信头像拼图.png')
    print('微信好友拼图完成！')


if __name__ == '__main__':
    act_path = creat_dir()
    # save_picture(act_path)
    # join_picture(act_path)
