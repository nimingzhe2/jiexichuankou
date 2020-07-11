import requests     #网络请求
import re           #正则
import webbrowser
import tkinter as tk  #gui


url='http://www.qmaile.com'
resp=requests.get(url)
#print(resp.text)             #打印返回文本
#response=resp.content.decode('utf-8')
resp.encoding = resp.apparent_encoding       #自动获取编码
response=resp.text
#print(response)

#数据提取  re xpath bs4
res = re.compile('<option value="(.*?)" selected')
reg=re.findall(res,response)
print(reg)
one1=reg[1]
one2=reg[2]
one3=reg[3]
one4=reg[4]
one5=reg[5]
one6=reg[6]




#画板
root=tk.Tk()
root.title('坏狗解析')
root.geometry('500x250+200+200')  #大小
l1=tk.Label(root,text='请选择播放接口:',font=('Arial',12))
l1.grid()
l2=tk.Label(root,text='播放链接:',font=('Arial',12))
l2.grid(row=9,column=0)
t1=tk.Entry(root,text="",width=50)
t1.grid(row=9,column=1)
#单选按钮
var=tk.StringVar()
r1=tk.Radiobutton(root,text='播放接口1',variable=var,value=one1)
r1.grid(row=0,column=1)
r2=tk.Radiobutton(root,text='播放接口2',variable=var,value=one2)
r2.grid(row=1,column=1)
r3=tk.Radiobutton(root,text='播放接口3',variable=var,value=one3)
r3.grid(row=2,column=1)
r4=tk.Radiobutton(root,text='播放接口4',variable=var,value=one4)
r4.grid(row=3,column=1)
r5=tk.Radiobutton(root,text='播放接口5',variable=var,value=one5)
r5.grid(row=4,column=1)
r6=tk.Radiobutton(root,text='播放接口6',variable=var,value=one6)
r6.grid(row=5,column=1)


def bf():
    webbrowser.open(var.get()+t1.get())

#播放按钮
b1=tk.Button(root,text='播放',font=('Arial',12),width=7,command=bf)
b1.grid(row=7,column=1)
def del_text():
    t1.delete(0,'end')

b2=tk.Button(root,text='清除',font=('Arial',12),width=7,command=del_text)
b2.grid(row=8,column=1)


#循环
root.mainloop()