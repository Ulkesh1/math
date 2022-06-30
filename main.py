import streamlit as st
from mathop import math
st.title("Math Operation")
a=st.number_input("1")
b=st.number_input('2')
m=math(a,b)
operation=st.selectbox("Select math operation",("add","sub","div","mul"))
if operation=='add':
    result=m.add()
if operation=='sub':
    result=m.sub()
if operation=='div':
    result=m.div()
if operation=='mul':
    result=m.mul()
st.info(f"The {operation} of {a} and {b} is {result}")

