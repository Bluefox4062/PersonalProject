import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk

# 创建主窗口
base = tk.Tk()
base.title('QRcode Generator')

# 输入区域框架
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)

# 输入标签
input_label = tk.Label(input_area, text="输入網址: ")
input_label.pack(side=tk.LEFT, padx=5)

# 输入文本框
encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text, width=40)
entry.pack(side=tk.LEFT, padx=5)

# 生成二维码并显示
qr_label = tk.Label(image_area)

def generate():
    if encode_text.get():
        qr_label.qr_img = qr.make(encode_text.get())
        img_width, img_height = qr_label.qr_img.size
        qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
        qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
        qr_label.pack(padx=5, pady=5)

# 生成按钮
encode_button = tk.Button(input_area, text='生成 QRcode!', command=generate)
encode_button.pack(side=tk.LEFT, padx=5)

# 布局
input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)

# 保存二维码图片
def save():
    filename = fd.asksaveasfilename(title='保存文件', initialfile='qrcode.png', defaultextension=".png",
                                    filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename)

# 退出程序
def exit():
    base.destroy()

# 显示关于对话框
def about():
    tk.messagebox.showinfo("关于", "QRcode Generator\n版本: 1.0\n作者: OpenAI")

# 创建菜单
menubar = tk.Menu(base)

# 文件菜单
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='保存', command=save)
filemenu.add_separator()
filemenu.add_command(label='退出', command=exit)
menubar.add_cascade(label='文件', menu=filemenu)

# 帮助菜单
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label='关于', command=about)
menubar.add_cascade(label='帮助', menu=helpmenu)

# 配置菜单
base.config(menu=menubar)

# 运行主循环
base.mainloop()
