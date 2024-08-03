import tkinter.messagebox as msg
import tkinter as tk

base = tk.Tk()

#def push():
#    print('MELON!')

#button1 = tk.Button(base, text='Water', width=20, bg='red', command=push).pack()
#button2 = tk.Button(base, text='PUSH 2', width=20, bg='green').pack(side=tk.LEFT)
#button3 = tk.Button(base, text='PUSH 3', width=20, bg='blue').pack(side=tk.RIGHT)

# -------------多選菜單-------------
#topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}
#check_value={}

#for i in range(len(topping)):
#    check_value[i] = tk.BooleanVar()
#    tk.Checkbutton(base, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)

#def buy():
#    for i in check_value:
#        if check_value[i].get() == True:
#            print(topping[i])

#tk.Button(base, text='點餐', command=buy).pack()    

# -------------單選菜單-------------
#radio_value = tk.IntVar()
#radio_value.set(0)

#lunch = {0:'A套餐', 1:'B套餐', 2:'C套餐'}
#tk.Radiobutton(base, text = lunch[0], variable= radio_value, value=0).pack()
#tk.Radiobutton(base, text = lunch[1], variable= radio_value, value=1).pack()
#tk.Radiobutton(base, text = lunch[2], variable= radio_value, value=2).pack()

#def buy():
#    value = radio_value.get()
#    print(lunch[value])

#tk.Button(base, text='點餐', command=buy).pack()

# -------------交談窗-------------
#response = msg.askyesno('糟糕了!!!', '還好嗎?')

#if response == True:
#    print('OK')
#else:
#    print('I got troble!')

# -------------輸入窗-------------
#string = tk.StringVar()
#entry = tk.Entry(base, textvariable=string).pack()
#label = tk.Label(base, textvariable=string).pack()



base.mainloop()