from tkinter import *
from tkinter import messagebox
root=Tk()
game_on =True;
turn = 'X'

def check_win(marker):

    return ((button1['text'] == marker and button2['text'] == marker and button3['text'] == marker) or
    (button4['text'] == marker and button5['text'] == marker and button6['text'] == marker) or
    (button7['text'] == marker and button8['text'] == marker and button9['text'] == marker) or
    (button1['text'] == marker and button5['text'] == marker and button9['text'] == marker) or
    (button3['text'] == marker and button5['text'] == marker and button7['text'] == marker) or
    (button1['text'] == marker and button4['text'] == marker and button7['text'] == marker) or
    (button3['text'] == marker and button6['text'] == marker and button9['text'] == marker) or
    (button2['text'] == marker and button5['text'] == marker and button8['text'] == marker))

def click(button):
    global turn,game_on
    if(button['text']==' ' and turn == 'X'):

        if(game_on):

            button['text'] = 'X'
            turn = 'O'
            if(check_win('X')):
                game_on=False;
                messagebox.showinfo('congaratulation',"X is winner")

            elif(check_full()):
                game_on=False;
                messagebox.showinfo('draw'," tie ")


    elif(button['text']==' ' and turn == 'O'):
        if(game_on):
            button['text'] = 'O'
            turn = 'X'
            if (check_win('O')):
                game_on=False
                messagebox.showinfo('congaratulation', "O is winner")

            elif(check_full()):
                game_on = False;
                messagebox.showinfo('draw', " tie ")

button1= Button(root,text=' ',command=lambda :click(button1),bg="blue",height=4,width=4)
button2= Button(root,text=' ',command=lambda :click(button2),bg="blue",height=4,width=4)
button3= Button(root,text=' ',command=lambda :click(button3),bg="blue",height=4,width=4)
button4= Button(root,text=' ',command=lambda :click(button4),bg="blue",height=4,width=4)
button5= Button(root,text=' ',command=lambda :click(button5),bg="blue",height=4,width=4)
button6= Button(root,text=' ',command=lambda :click(button6),bg="blue",height=4,width=4)
button7= Button(root,text=' ',command=lambda :click(button7),bg="blue",height=4,width=4)
button8= Button(root,text=' ',command=lambda :click(button8),bg="blue",height=4,width=4)
button9= Button(root,text=' ',command=lambda :click(button9),bg="blue",height=4,width=4 )

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

def check_full():
    return (button1['text']!=' 'and button2['text']!=' 'and button3['text']!=' 'and button4['text']!=' 'and button5['text']!=' 'and button6['text']!=' 'and
            button7['text'] != ' ' and button8['text']!=' 'and button9['text']!=' ')

#root.geometry("400x400")

root.mainloop()
