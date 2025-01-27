import pickle
import pandas as pd
movie50=pickle.load(open('books.pkl', 'rb'))

import streamlit as st

movie50=pd.DataFrame(movie50)
link_with_book=movie50['Image-URL-M']

st.title('Book Recommender System')
click=st.button('Show top50 books')

book50=movie50.drop(['Image-URL-M'],axis=1)
popular2=book50.reset_index()
link_with_book=(link_with_book.reset_index().drop('index',axis=1))

popular2.drop('index',axis=1,inplace=True)
if click:
    st.title("THESE ARE THE TOP 50 BOOKS TO READ WITH RESPECT TO RATINGS")
    for k in range(0,50):
        st.divider()
        st.write("_________________")
        st.title(f"Book {k+1}")
        st.image(link_with_book.iloc[k][0])
        st.write(link_with_book.iloc[k][0])
        
        for i,p in enumerate(popular2):
            with st.container():
                if p=='Book-Title':
                    st.markdown(f"**{p} : {popular2[p][k]}**")
                
                else:
                
                    st.write(f"{p} : {popular2[p][k]}")
               
                