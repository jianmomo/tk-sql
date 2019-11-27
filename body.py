import tkinter as tk
from app.user.model import Sleep, menu
window = tk.Tk()
window.title('form')
window.geometry('680x750')
# 这是窗口的内容'

# 头部布局
select = tk.Frame(window, height=2)
select.pack()
select_text = tk.Frame(select)
select_button = tk.Frame(select)
# 细分布局。
select_name = tk.Frame(select_text)
select_score = tk.Frame(select_text)
select_text.pack(side='left')
select_button.pack(side='right')
select_name.pack(side='left')
select_score.pack(side='right')
# 指定大小位置
name_var = tk.StringVar()
tk.Label(select_name, width=20, text='姓名').pack()
tk.Entry(select_name, width=18, textvariable=name_var).pack()


# 第二窗体

def create(data):
    top = tk.Toplevel()
    top.title('1')
    top.geometry('680x350')
    for i in range(1, 4):
        t = Sleep.display(data, i)
        tk.Label(top, text=str(t)).grid(row=1, column=i, padx=40, pady=15)
    u_var = tk.StringVar()
    v_var = tk.StringVar()
    w_var = tk.StringVar()
    tk.Entry(top, width=10, textvariable=u_var).grid(row=2, column=1, padx=40, pady=15)
    tk.Entry(top, width=10, textvariable=v_var).grid(row=2, column=2, padx=40, pady=15)
    tk.Entry(top, width=10, textvariable=w_var).grid(row=2, column=3, padx=40, pady=15)

    def on():
        value_name = u_var.get()
        value_score =v_var.get()
        value_time = w_var.get()
        Sleep.update(value_name, value_score, data)

    tk.Button(top, text='保存', command=on).grid(row=3, column=3, padx=40, pady=15)


def select():
    top = tk.Toplevel()
    top.title('1')
    top.geometry('680x350')
    name = name_var.get()
    tk.Label(top, text=str(Sleep.select(name,))).grid(row=1, column=1, padx=40, pady=15)


tk.Button(select_button, text='搜索', command=select).pack()

# 主体布局
body = tk.Frame(window, height=42, width=100)
body.pack(pady=15, padx=0)
body_text = tk.Text(body, height=40, width=160)
body_text.pack(pady=30)
# 姓名，分数，时间三个标题的显示
for j in range(1, 4):
    var = tk.StringVar()
    var.set(menu(j))
    tk.Label(body_text, textvariable=var, width=5, height=2).grid(row=0, column=j, ipadx=50)


def update(data):   # 修改按钮闭包
    def war():
        create(data)
    return war


def delete(data):   # 删除按钮闭包
    def war():
        Sleep.delete(data)
    return war


for i in range(1, 11):  # 第一次获取的中间页面
    for j in range(1, 4):
        # 十条数据的显示，调用函数。用循环控制，
        tk.Label(body_text, text=str(Sleep.display(i, j)), width=20).grid(row=i, column=j, padx=5, pady=5)
    # 删除和修改按钮显示，修改的时候注意。删除要注意刷新。
    tk.Button(body_text, text='修改' + str(i), width=5, command=update(i),).grid(row=i, column=4, padx=10, pady=5)
    tk.Button(body_text, text='删除' + str(i), width=5, command=delete(i)).grid(row=i, column=5, padx=10, pady=5)

# 获取主界面的修改文本信息，进行添加
x_var = tk.StringVar()
y_var = tk.StringVar()
z_var = tk.StringVar()
x = tk.Entry(body_text, width=15, textvariable=x_var).grid(row=12, column=1, padx=25, pady=15)
y = tk.Entry(body_text, width=15, textvariable=y_var).grid(row=12, column=2, padx=25, pady=15)
z = tk.Entry(body_text, width=15, textvariable=z_var).grid(row=12, column=3, padx=25, pady=15)

Up = 0


def on():  # 将添加的数据进行置顶刷新
    global Up
    Up = Up+1
    value_name = x_var.get()
    value_score = y_var.get()
    value_time = z_var.get()
    zj = Sleep.add(value_name, value_score, value_time)
    # for t in range(1, 4):
    #     list_l.append(Sleep.display(zj, t))
    # print(list_l)
    for xx in range(Up, 11):
        for yy in range(1, 4):
            # for tt in range(-Up, -1):
            #     for kk in range(-3 * tt, -1):
            #         h = 0
            #         if abs(kk) % 3 == 0:
            #             h = 1
            #         elif abs(kk) % 3 == 2:
            #             h = 2
            #         else:
            #             h = 3
            #         tk.Label(body_text, text=str(list_l[kk]), width=20).grid(row=abs(tt), column=h, padx=5, pady=5)
            # 十条数据的显示，调用函数。用循环控制
            tk.Label(body_text, text=str(Sleep.display(zj, yy)), width=20).grid(row=Up, column=yy, padx=5, pady=5)
            tk.Label(body_text, text=str(Sleep.display((xx-Up+1), yy)), width=20).grid(row=xx, column=yy, padx=5, pady=5)
        # 删除和修改按钮显示，修改的时候注意。删除要注意刷新。
        tk.Button(body_text, text='修改' + str(xx), width=5, command=update(xx)).grid(row=xx, column=4, padx=10, pady=5)
        tk.Button(body_text, text='删除' + str(xx), width=5, command=delete(xx)).grid(row=xx, column=5, padx=10, pady=5)
    tk.Label(end_one, text=str(Sleep.count('页数')), ).grid(row=1, column=2, padx=10, pady=10)


tk.Button(body_text, text='增加', command=on).grid(row=12, column=5, padx=25, pady=5)

# 将最下面的一栏按钮进行布局分割
end_one = tk.Frame(window, height=20, width=30)
end_one.pack(pady=15)
a = 0


def down_page():  # 向下翻页，数据刷新
    global a
    a = a+10
    if a > Sleep.count(1)*10-1:
        a = Sleep.count(1)*10-1
    for t in range(1+a, 11+a):
        for k in range(1, 4):
            tk.Label(body_text, text=str(Sleep.display(t,  k)), width=20,).grid(row=t-a, column=k, padx=5, pady=5)
        tk.Button(body_text, text='修改' + str(t), width=5, command=update(t)).grid(row=t-a, column=4, padx=10, pady=5)
        tk.Button(body_text, text='删除' + str(t), width=5, command=delete(t)).grid(row=t-a, column=5, padx=10, pady=5)
    tk.Label(end_one, text=str(a//10+1)).grid(row=1, column=0, padx=10, pady=10)


def up_page():  # 向上翻页，数据刷新
    global a
    a = a-10
    if a <= 0:
        a = 0
    for x in range(a+1, a+11):
        for y in range(1, 4):
            tk.Label(body_text, text=str(Sleep.display(x,  y)), width=20,).grid(row=x-a, column=y, padx=5, pady=5)
        tk.Button(body_text, text='修改' + str(x), width=5, command=update(x)).grid(row=x-a, column=4, padx=10, pady=5)
        tk.Button(body_text, text='删除' + str(x), width=5, command=delete(x)).grid(row=x-a, column=5, padx=10, pady=5)
    tk.Label(end_one, text=str(a // 10 + 1)).grid(row=1, column=0, padx=10, pady=10)


tk.Button(end_one, text='上一页', command=up_page).grid(row=1, column=4, padx=10, pady=10)
tk.Button(end_one, text='下一页', command=down_page).grid(row=1, column=5, padx=10, pady=10)
tk.Label(end_one, text='1').grid(row=1, column=0, padx=10, pady=10)
tk.Label(end_one, text='页码',).grid(row=1, column=1, padx=10, pady=10)
tk.Label(end_one, text=str(Sleep.count('页数')), ).grid(row=1, column=2, padx=10, pady=10)
tk.Label(end_one, text='总数', ).grid(row=1, column=3, padx=10, pady=10)
window.mainloop()