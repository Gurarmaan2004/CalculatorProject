from tkinter import *
import sympy as sp

def btn_click(item):
    """continuously updates the input field whenever you enter a number or operator"""
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_solve():
    """ Toggles expression solver and enters solve( into calculator """
    global isSolve, expression
    isSolve = True
    expression = ""
    btn_click("solve(")

def btn_clear(): 
    """function used to clear the input field"""
    global expression
    expression = "" 
    input_text.set("")
 
def btn_equal():
    """
    Solves using "eval" if it is an arithmetic operation
    If it is an algebraic equation, it uses symPy solve and Eq
    """
    global expression, isSolve
    if isSolve == False:
        try:
            result = str(eval(expression)) 
            input_text.set(result)
        except:
            result = "Syntax Error"
    else:
        # removes "solve(" from expression" and splits into LHS and RHS
        arr = expression[6:].split("=")
        # if the arr doesnt have an equals sign (or has more than 1)
        if len(arr) != 2:
            result = "Syntax Error"
        #attempts to solve
        try:
            result = sp.solve(sp.Eq(sp.parse_expr(arr[0]), sp.parse_expr(arr[1])))
            # if it has no solution
            if result == []:
                result = "No solution"
            # returns an x value
            else:
                result = "x = " + str(result).strip('[]')
        # if there is an error, returns as such
        except:
	        result = "Syntax Error"
    input_text.set(result)     
    expression = ""


win = Tk() # Create a basic window
win.geometry("500x400")  # this is for the size of the window 
win.title("Calculator")

expression = ""
isSolve = False
 
# get the instance of input field
 
input_text = StringVar()
 
# create a frame for the input field
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="black", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=272.5, bg="black")
 
btns_frame.pack()

# first row

solve = Button(btns_frame, text = "solve", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = btn_solve).grid(row = 0, column = 0, padx = 1, pady = 1)

algebra_x = Button(btns_frame, text = "x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("x")).grid(row = 0, column = 1, padx = 1, pady = 1)

exp = Button(btns_frame, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("**")).grid(row = 0, column = 2, padx = 1, pady = 1)

divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# second row

clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 1, column = 0, padx = 1, pady = 1)

left_bracket = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("(")).grid(row = 1, column = 1, padx = 1, pady = 1)

right_bracket = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(")")).grid(row = 1, column = 2, padx = 1, pady = 1)

multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 2, column = 2, padx = 1, pady = 1)

minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

  
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 3, column = 2, padx = 1, pady = 1)

plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 4, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 4, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("=")).grid(row = 4, column = 3, padx = 1, pady = 1)

# fifth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 24, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 5, column = 0,columnspan=2,padx = 1, pady = 1)

 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 5, column = 2, padx = 1, pady = 1)
 
execute = Button(btns_frame, text = "EXE", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
 
win.mainloop()