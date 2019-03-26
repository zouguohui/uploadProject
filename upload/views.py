from django.shortcuts import render
from django.http import HttpResponse

import os
import qrcode
# Create your views here.


def upload_file(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            # 打开待定的文件进行二进制的写操作
            with open("./upload/temp_file/%s" % File.name, 'wb+') as f:
                # 分块写入文件
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse("UPload over!")
    else:
        return render(request, "upload.html",)


def app_list(request):
    app_list = []
    apk_name_list = []
    ipa_name_list = []
    file_path = './upload/temp_file'
    filename_list = os.listdir(file_path)
    print(filename_list)
    for file_name in filename_list:
        index = file_name.rfind(".")
        extension = file_name[index+1:]
        app_list.append(extension)
    print(app_list)
    for f in app_list:
        print(f)
        if f == "apk":
            index = app_list.index(f)
            print(index)
            apk_name = filename_list[index]
            apk_name_list.append(apk_name)
        else:
            index = app_list.index(f)
            print(index)
            apk_name = filename_list[index]
            ipa_name_list.append(apk_name)
    print(apk_name_list)
    print(ipa_name_list)
    return render(request, "index.html", locals())


def download_file(request, par):
    if os.path.exists("./upload/static/%s.png" % par):
        print(1)
    else:
        img = qrcode.make("http://127.0.0.1:8000/temp_file/%s" % par)
        img.save("./upload/static/%s.png" % par)
        print(2)
    print(par)
    return render(request, "download.html", {'par': par})
