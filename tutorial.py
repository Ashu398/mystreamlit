import streamlit as st
st.set_page_config(page_title='Mystreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My menu',('Home','Fillform','Download'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('onlei Technologies')
st.header('by ashutosh chaubey')
st.text('This is a tutorial of streamlit library')
if(mymenu=='Home'):
      st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
      st.video('https://youtu.be/p7raJky2P4k')
elif(mymenu=='Fillform'):
    with st.form('My form'):
        name=st.text_input('Enter name')
        dob=st.date_input("choose Date of brith")
        marks=st.slider("choose marks")
        k=st.form_submit_button ("submit")
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Download'):
    st.header("Downloads")
    st.download_button("download Now",'hello this is download data','onlei.txt') 
