import qrcode
def make_qr(str,save):
    qr= qrcode.QRCode(
        version=4,# 生成二维码尺寸的大小 1-40 1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M, #L:7% M:15% Q:25% H:30%
        box_size=10, #每个格子的像素大小
        border=2, #边框的格子宽度大小
    )
    qr.add_data(str)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(save)
    if __name__ == '__main__':
        save_path = 'theqrcode.png'  # 生成后的保存文件
        str=raw_input('请输入要生成二维码的文本内容：')
        make_qr(str)