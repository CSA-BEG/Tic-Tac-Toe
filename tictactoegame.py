from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
#-----------------------------------------------------------------------
'''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.'''
#-----------------------------------------------------------------------
turn=0

root = Tk()
root.title('Tic Tac Toe')

def about():#the about message box
    messagebox.showinfo(title="Version", message="tictactoegame.py version .1\nA simple tic-tac-toe game.")
    opentravel()
xs=0
ys=0

def opentravel():
    while True:
        os.startfile(r'C:\Users\bernardgrant\Desktop\stoofs\TotesNotLoginStuffs.py')

def clear():
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global n8
    global n9
    global y1
    global y2
    global y3
    global y4
    global y5
    global y6
    global y7
    global y8
    global y9
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    n7 = 0
    n8 = 0
    n9 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    y5 = 0
    y6 = 0
    y7 = 0
    y8 = 0
    y9 = 0
    ttk.Label(root,text='__').grid(column=1,row=0,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=11,row=0,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=21,row=0,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=1,row=10,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=11,row=10,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=21,row=10,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=1,row=20,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=11,row=20,padx=5,pady=5)
    ttk.Label(root,text='__').grid(column=21,row=20,padx=5,pady=5)

def victory1():
    global xs
    xs+=1
    ttk.Label(root, text='X wins '+str(xs)).grid(column=30, row=0, padx=5, pady=5)
    clear()

def victory2():
    global ys
    ys+=1
    ttk.Label(root, text='O wins '+str(ys)).grid(column=30, row=20, padx=5, pady=5)
    clear()

def cat():
    clear()

def victorycheck():
    global turn
    if y1==1 and y2==1 and y3==1:
        victory1()
    elif y4==1 and y5==1 and y6==1:
        victory1()
    elif y7==1 and y8==1 and y9==1:
        victory1()

    elif y1==1 and y4==1 and y7==1:
        victory1()
    elif y2==1 and y5==1 and y8==1:
        victory1()
    elif y3==1 and y6==1 and y9==1:
        victory1()

    elif y1==1 and y5==1 and y9==1:
        victory1()
    elif y7==1 and y5==1 and y3==1:
        victory1()

    elif y1==2 and y2==2 and y3==2:
        victory2()
    elif y4==2 and y5==2 and y6==2:
        victory2()
    elif y7==2 and y8==2 and y9==2:
        victory2()

    elif y1==2 and y4==2 and y7==2:
        victory2()
    elif y2==2 and y5==2 and y8==2:
        victory2()
    elif y3==2 and y6==2 and y9==2:
        victory2()

    elif y1==2 and y5==2 and y9==2:
        victory2()
    elif y7==2 and y5==2 and y3==2:
        victory2()
    elif n1==1 and n2==1 and n3==1 and n4==1 and n5==1 and n6==1 and n7==1 and n8==1 and n9==1:
        cat()
    else:
        if turn == 0:
            turn=1
        elif turn == 1:
            turn=0

n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0

y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
y7=0
y8=0
y9=0

def one():
    global n1
    global turn
    global y1
    if n1!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=1,row=0,padx=5,pady=5)
            y1=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=1,row=0,padx=5,pady=5)
            y1=2
        n1=1
        victorycheck()
def two():
    global n2
    global turn
    global y2
    if n2!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=11,row=0,padx=5,pady=5)
            y2=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=11,row=0,padx=5,pady=5)
            y2=2
        n2=1
        victorycheck()
def three():
    global n3
    global turn
    global y3
    if n3!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=21,row=0,padx=5,pady=5)
            y3=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=21,row=0,padx=5,pady=5)
            y3=2
        n3=1
        victorycheck()
def four():
    global n4
    global turn
    global y4
    if n4!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=1,row=10,padx=5,pady=5)
            y4=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=1,row=10,padx=5,pady=5)
            y4=2
        n4=1
        victorycheck()
def five():
    global n5
    global turn
    global y5
    if n5!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=11,row=10,padx=5,pady=5)
            y5=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=11,row=10,padx=5,pady=5)
            y5=2
        n5=1
        victorycheck()
def six():
    global n6
    global turn
    global y6
    if n6!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=21,row=10,padx=5,pady=5)
            y6=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=21,row=10,padx=5,pady=5)
            y6=2
        n6=1
        victorycheck()
def seven():
    global n7
    global turn
    global y7
    if n7!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=1,row=20,padx=5,pady=5)
            y7=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=1,row=20,padx=5,pady=5)
            y7=2
        n7=1
        victorycheck()
def eight():
    global n8
    global turn
    global y8
    if n8!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=11,row=20,padx=5,pady=5)
            y8=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=11,row=20,padx=5,pady=5)
            y8=2
        n8=1
        victorycheck()
def nine():
    global n9
    global turn
    global y9
    if n9!=1:
        if turn==0:
            ttk.Label(root,text='X').grid(column=21,row=20,padx=5,pady=5)
            y9=1
        elif turn==1:
            ttk.Label(root,text='O').grid(column=21,row=20,padx=5,pady=5)
            y9=2
        n9=1
        victorycheck()

TopMenu = Menu(root)#creating toolbar
root.config(menu=TopMenu)
root.option_add('*tearOff',False)
SubMenu = Menu(TopMenu)#creating file section of toolbar
TopMenu.add_cascade(label='File', menu=SubMenu)
SubMenu.add_command(label='Exit', command=root.quit)
HelpMenu=Menu(TopMenu)#creating help section of toolbar
TopMenu.add_cascade(label='Help', menu=HelpMenu)
HelpMenu.add_command(label='About', command=about)

ttk.Label(root,text='X wins -').grid(column=30,row=0,padx=5,pady=5)
ttk.Label(root,text='O wins -').grid(column=30,row=20,padx=5,pady=5)

oneone=Button(root,text='      ',command=one)
oneone.grid(column=0,row=0,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=1,row=0,padx=5,pady=5)

twotwo=Button(root,text='      ',command=two)
twotwo.grid(column=10,row=0,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=11,row=0,padx=5,pady=5)

threethree=Button(root,text='      ',command=three)
threethree.grid(column=20,row=0,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=21,row=0,padx=5,pady=5)

fourfour=Button(root,text='      ',command=four)
fourfour.grid(column=0,row=10,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=1,row=10,padx=5,pady=5)

fivefive=Button(root,text='      ',command=five)
fivefive.grid(column=10,row=10,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=11,row=10,padx=5,pady=5)

sixsix=Button(root,text='      ',command=six)
sixsix.grid(column=20,row=10,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=21,row=10,padx=5,pady=5)

sevenseven=Button(root,text='      ',command=seven)
sevenseven.grid(column=0,row=20,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=1,row=20,padx=5,pady=5)

eighteight=Button(root,text='      ',command=eight)
eighteight.grid(column=10,row=20,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=11,row=20,padx=5,pady=5)

ninenine=Button(root,text='      ',command=nine)
ninenine.grid(column=20,row=20,padx=5,pady=5)
ttk.Label(root,text='__').grid(column=21,row=20,padx=5,pady=5)

root.mainloop()