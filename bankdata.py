import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('bank-additional-full.csv')
from PIL import Image
image = Image.open('bank.jpg')
st.image(image, caption='bank.jpg',use_column_width=True)
st.subheader('Final  Project  from   Chuanyue Liu   and   Houhua Zhang')
st.title('Bank Marketing Campaigns')
st.header('Data Analytics')
st.markdown('**The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed.**')
st.write(data)
st.markdown('**Number of Instances: 41188** ') 
st.markdown('**Number of Attributes: 20 + output attribute.**')
st.balloons()







st.write('')
st.write('')
st.markdown('After the above analysis, we can find that the customer is  occupation_and_the day of the week_for_promotion have important influence on whether the customer agrees to deposit_or_not')
st.markdown('The education level of customers and CPI are the same as them; At the same time, we found that these two groups of variables can influence each other, so we want to know:')
job_label= st.sidebar.radio(
     'Select job',
     ('management','services','admin.','blue-collar','entrepreneur','housemaid','retired','self-employed','student','technician','unemployed','unknown'))  
day_of_week_label= st.sidebar.radio(
     'Select day',
     ('mon','tue','wed','thu','fri'))
education_label= st.sidebar.radio(
     'Select education',
     ("basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown"))




for k in data.job: 
    if job_label==k:
         l=job_label
    else:
        pass



for m in data.day_of_week: 
    if day_of_week_label==m:
         n=day_of_week_label
    else:
        pass



for o in data.education: 
    if education_label==o:
         p=education_label
    else:
        pass
data_forms=data[data.education==p][data.day_of_week==n][data.job == l]
st.header('')
st.markdown('**This is a table where data can be filtered by job, day of week and education**')
st.write(data_forms)


st.header('Q1: ')
st.subheader('The number of people who in different occupations will agree to deposit money on different day of a week. And then exchange.')

for b in data.job: 
    if job_label==b:
         a=job_label
    else:
        pass

data_day_yes = data[data.job == a]
data_day_yes_group = data_day_yes.groupby('day_of_week')
d1 = data_day_yes_group.y.value_counts()
fig, ax = plt.subplots(2,1)
d1.plot.bar(ax=ax[0],figsize=(20,10))
ax[0].set_title('Distribution of jobs and deposit') 
ax[0].set_xlabel('day of week ')  
ax[0].set_ylabel('Number of clients')




for e in data.day_of_week: 
    if day_of_week_label==e:
         f=day_of_week_label
    else:
        pass

data_job_yes = data[data.day_of_week == f]
data_job_yes_group = data_job_yes.groupby('job')
d2 = data_job_yes_group.y.value_counts()
d2.plot.bar(ax=ax[1],figsize=(20,10))
ax[1].set_title('Distribution of jobs and deposit') 
ax[1].set_xlabel('job')  
ax[1].set_ylabel('Number of clients')
st.pyplot(fig)


with st.expander("See explanation"):
    st.write("""There is a chart about the people who do different jobs most and least likely to agree to deposit on a day of a week. We can see that many jobs don’t want to deposit on Mon, which maybe is related that Mon is the first day after weekends, we don’t want to work.\n 
In terms of salary and job freedom, services, blue-collar, technician, student and unknown are who get relatively low pay and work freedom because they work for someone else as an employed person. They are most likely to agree to deposit on Friday. We suspect this has something to do with the upcoming holidays.\n 
We think admin, retired, self-employed, housemaid, unemployed have the same point which is they have a relatively stable job, and they are most likely to agree to deposit on Wednesday.\n
And management and entrepreneur who have less pressure to earn money are likely to agree to deposit on Tuesday.
""")
    image = Image.open('data1.png')
    st.image("data1.png")


st.header('Q2: ')
st.subheader('The number of people who will agree or disagree to deposit money in different CPI when they are in different considerably by education. And then exchange.')



for c in data.education: 
    if education_label==c:
         h=education_label
    else:
        pass
fig, ax = plt.subplots()
data_education_yes = data[data.education == h][data['y'] == 'yes']
data_education_yes_group = data_education_yes.groupby('cons_price_idx')
d3 = data_education_yes_group.y.value_counts()
d3.plot(ax=ax,figsize=(20,10))
ax.set_title('Distribution of cons.price.idx and education') 
ax.set_xlabel('cons.price.idx ')
ax.set_ylabel('Number of clients')
st.pyplot(fig)


st.markdown('If you see there is an error, the reason why it happens is that we want to do a slider to change the value of cpi, but we found it seems that the slider’s exact value is at most two decimal places, but the data has three decimal places. However, when we rounded the data, we reduced them to a decimal place. Even if we limit its value between 90 and 100, it just only has twenty more values. So now we use the slider with integer to find the right value easily. Next time we will correct the mistake.')
fig, ax = plt.subplots()
index = st.sidebar.slider('cons_price_idx', 92.20, 94.77)
for g in data.cons_price_idx: 
    if index==g:
        q=index
    else:
        pass
data_cpi_yes= data[data.cons_price_idx == q][data['y'] == 'yes']
data_cpi_yes_group = data_cpi_yes.groupby('education')
d4=data_cpi_yes_group.y.value_counts()
d4.plot(ax=ax,figsize=(20,10))

st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""According to the chart, we can see that different levels of education have a significant impact on the impact of CPI on whether people agree to save money and vice versa
""")