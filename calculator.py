#Omisha Singh 10 F
import streamlit as st
st.title("My calculator")
a=int(input("Enter First Number")
      print("First Number=",a)
b=int(input("Enter Second Number")
      print("Second Number=",b)
c=int(input("Choose your programme:"
            "Click 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
      print("Programme chosen=", c)
if c == 1:
      print(a+b)
elif c== 2:
      print(a-b)
elif c == 3:
      print(a*b)
elif c == 4:
      print(a/b)
