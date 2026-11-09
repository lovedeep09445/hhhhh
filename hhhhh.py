import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="STUDENT MARKS DASHBOARD",layout="wide")
st.title("STUDENT MARKS ANALYTICS DASHBOARD")

np.random.seed(42)
students=[f"Student_{i}" for i in range(1,11)]
subjects=['Maths','Physics','chemistry','English','CS']

marks_data=np.random.randint(30,100,size=(10,5))

df=pd.DataFrame(marks_data,columns=subjects,index=students)
df['Total']=df.sum(axis=1)
df['Average']=df[subjects].mean(axis=1)

topper=df['Total'].idxmax()
top_score=df['Total'].max()
subject_averages =df[subjects].mean()
weakest_student=subject_averages.idxmin()

col1,col2=st.columns(2)
col1.metric("Class Topper",f"{topper}({top_score}Marks)")
col2.metric("Weakest Student(Class Avg)",f"{weakest_subject}({subject_averages.min():.1f})")

st.subheader("Student Marks Table")
st.dataframe(df)

col_chart1,col_chart2=st.columns(2)

with col_chart1:
    st.subheader("Total Marks by Student(Bar Chart)")
    fig,ax=plt.subplots(figsize=(8,5))
    ax.bar(df.index,df['Total'],color='royalblue')
    ax.set_ylabel("Total Marks")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col_chart2:
    st.subheader("Subject-wise Performance(Heatmap)")
    fig,ax=plt.subplots(figsize-(8,5))
    colors(red/orange==low,green/blue==high)
    sns.heatmap(df[subjects],annot=True,cmap="Y1GnBu",fmt='d',ax=ax)
    st.pyplot(fig)

      
