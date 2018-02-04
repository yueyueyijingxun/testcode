import qrcode

#img = qrcode.make('hello, whupps')
# img.save('test22.png')
def make_qr(str,save):
    qr= qrcode.QRCode(
        version=1,#值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）如果想让程序自动确定，将值设置为None并使用fit参数即可。
        error_correction=qrcode.constants.ERROR_CORRECT_L,#L:7% M:15% Q:25% H:30%
     box_size=10,# 控制二维码中每个小格子包含的像素数。
        border=4,#控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
    )
    qr.add_data(str)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(save)
#make a QRimg with logo
def make_logo_qr(str,logo,save):
    qr=qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )
    qr.add_data(str)
    qr.make(fit=True)
    img=img.convert("RGBA")
    if logo and path.exists(logo):
        icon=Image.open(logo)
        img_w,img_h=img.size
        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        img.paste(icon,(w,h),icon)
        img.save(save)
    if _name_=='_main_':
        save_path='my22qrcode.png'
        logo='logo.jpg'
        str=raw_input('请输入要生成二维码的文本内容：')
        make_logo_qr(str,logo,save_path)