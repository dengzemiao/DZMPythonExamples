# 方式一：
dict = { 'name': 'dzm', 'age': '20' }
print('name' in dict)    # True
print('id' in dict)      # False
print('id' not in dict)  # True

# 导入系统库
# import sys
# # 脚本参数
# argv = sys.argv[1:]
# # 是否有参数
# if len(argv):
#     print(len(argv))
# else:
#     print(2222)
#     sys.exit()
# print(33333)
# # import re
# # import conf

# # print(conf.confs['name'])

# # # f = open('dzm.js', 'r+')
# # # # 加载到内存
# # # data = f.read()
# # # print(data)

# # def r_4(k, d):
# #     return re.search(r'(?<=\"%s\"\>).*?(?=\<)'%k, d)

# # # 读取内容
# # f = open('./dzm.vue', 'r+')
# # # 加载到内存
# # data = f.read()
# # # r = r_4('pk-company-fname', data)
# # result = data.replace('剧好看网络', 'dzmdzm')

# # # print(r.group())
# # # name = 'package'
# # # name2 = '\"'
# # # 替换
# # # result = sub(r"(?<=\"%s\"\: \").*?(?=%s)"%(name,name2), 'com.haixing9.module', data, 1)
# # # result = re.sub(r'(?<=\"name\"\: \").*?(?=\")', '海星小剧场2', result, 1)
# # # result = re.sub(r'(?<=\"versionName\"\: \").*?(?=\")', '1.0.1', result, 1)
# # # result = re.sub(r'(?<=\"icon\"\: \").*?(?=\")', '/assets/images/logo-hx.png', result, 1)
# # # 需要将光标移动到开始位置
# # f.seek(0)
# # # 截断文件，也就是将光标之后的内容全部清空不要了，这样也就达到了清空的
# # f.truncate()
# # # 把新内容写回硬盘
# # f.write(result)
# # # 关闭
# # f.close()

# # # result = re.sub(r'(?<=\"name\"\: \").*?(?=\")', 'dzm', string, 1)
# # # print(result)
 
# # # string = '''
# # # {
# # #   "package": "com.lanjing.module",
# # #   "name": "蓝鲸剧场",
# # #   "versionName": "1.0.0",
# # #   "versionCode": 1,
# # #   "minPlatformVersion": 1100,
# # #   "icon": "/assets/images/logo-lj.png",
# # #   "features": [
# # #     {
# # #       "name": "system.prompt"
# # #     },
# # #     {
# # #       "name": "system.router"
# # # '''

# # # m = re.match(r'(?<=\"name\"\: \").*?(?=\")', string)
# # # m = re.match(r'name', string)
# # # s = regex.search(string)
# # # m.group()
# # # print(m)

# # # result = re.sub(r'(?<=\"name\"\: \").*?(?=\")', 'dzm', string, 1)
# # # print(result)

# # # regex = re.compile(r'(?<=\"name\"\: \").*?(?=\")')
# # # s = regex.search(string)
# # # s.group()
# # # print(s)

# # # def cut_out(a,b,string):
# # #     result = re.findall(".*%s(.*)%s.*"%(a,b),string)
# # #     print(result)
# # #     for x in result:
# # #         print(x)

# # #     # result = re.sub(".*%s(.*)%s.*"%(a,b), "dzm", string)
# # #     # print(result, string)

# # # # 注意以下的取值要用转义字符（如果字符是要需要转义的话【例如：\ ' 】，普通的字符就不需要）
 
# # # a = '\"'
# # # b = '\"'
# # # cut_out(a,b,string)

# import zipfile
# import os
 
# # f = zipfile.ZipFile("./sign-hx.zip",'r') # 压缩文件位置
# # for file in f.namelist():
# #     f.extract(file, "./")               # 解压位置
# # f.close()

# import shutil
# # print(os.path.exists('./sign'))
# # shutil.rmtree('./sign')

# # ================ 移除现有证书
# # 移除指定文件夹
# def rm(p):
#     # 是否存在该文件夹
#     if (os.path.exists(p)):
#         # 移除证书文件夹
#         shutil.rmtree(p)
# # 进度提示

# print('\033[1;32m============================== 移除现有证书 \033[0m')
# # 移除文件夹
# rm('./sign')

# # ================ 解压对应平台证书

# # 进度提示
# print('\033[1;32m============================== 解压对应平台证书 \033[0m')
# # 解压 zip
# f = zipfile.ZipFile('./sign-hx.zip','r')
# # 输出到指定文件夹
# for file in f.namelist():
#     f.extract(file, './')
# # 关闭
# f.close()
# # 解压附带的垃圾文件夹
# # rm('./__MACOSX')