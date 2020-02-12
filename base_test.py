#encoding:utf-8

import requests
import base64

#获取access_token
def getToken(apikey,secretkey):
    api_url = r'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
              '&client_id={}&client_secret={}'.format(apikey,secretkey)
    res = requests.get(api_url)
    r = res.json()
    if 'access_token' in r:
        return r['access_token']
    else:
        print('未能获取到access_token!')

#用base64编码img-学习蓝队的时候保存了微信图片
def en2base64(img):
    with open(img,'rb') as f:
        pic_base64 = base64.b64encode(f.read())
    return pic_base64

#调用接口进行人脸评分
def testface(img64,token):
    headers = {'content-type': 'application/json'}
    #headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    url = r'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token={}'.format(token)
    data = {
        'image':img64,
        'image_type':'BASE64',
        'face_field':'age,beauty,gender,face_shape,face_type,expression'
    }
    r = requests.post(url,data=data,headers=headers).json()
    if r['error_msg'] == 'SUCCESS':
        face_value = r['result']['face_list'][0]
        age = face_value['age']
        beauty = face_value['beauty']
        gender = face_value['gender']['type']
        face_shape = face_value['face_shape']['type']
        face_type = face_value['face_type']['type']
        expression = face_value['expression']['type']
        fs = {
            'square':'方形脸',
            'triangle':'瓜子脸',
            'oval':'圆形脸',
            'heart':'瓜子脸',
            'round':'圆形脸'
        }
        ft = {
            'human':'真实人物',
            'cartoon':'卡通人物'
        }
        exp = {
            'none':'不笑',
            'smile':'微笑',
            'laugh':'大笑'
        }
        print('图片信息-年龄:{}; 颜值:{}; 性别:{}; 脸型:{}; 人物类型:{}; 表情:{}' \
              .format(age,beauty,gender,fs[face_shape],ft[face_type],exp[expression]))
        #return age,beauty,gender,fs[face_shape],ft[face_type],expression


if __name__ == '__main__':
    base_img = r'/Users/caopengfei/Documents/dabao/dabao1.jpg'
    img64 = en2base64(base_img)
    token = getToken()
    r = testface(img64,token)