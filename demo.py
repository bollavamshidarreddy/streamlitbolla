import streamlit as st 

st.title('Venkat G addition class')
number1 = st.number_input("Enter the first number", min_value=0, max_value=100, step=1)
number2 = st.number_input("Enter the second number", min_value=0, max_value=100, step=1)
addi=number1+number2
sub1=abs(number1-number2)
st.write("Result of addition:", addi)
st.write("Result of subtraction:", sub1)
st.success("successed")

# conditional operator
if addi >=60: 
    st.write('Tharun topper')
else:
    st.write('Tharun super')
