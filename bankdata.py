import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('bank-additional-full.csv')
st.title('Bank Marketing Campaigns')
st.header('Data Analytics')
st.markdown('**The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed.**')
st.write(data)
st.markdown('**Number of Instances: 41188** ') 
st.markdown('**Number of Attributes: 20 + output attribute.**')



st.markdown('**These graphs are made to conducted a separate analysis of each influencing factor, discussing the impact of its variables on success**')
fig,ax= plt.subplots(4,1,figsize=(10,60))
temp_1 = pd.DataFrame()
temp_1['No_deposit'] = data[data['y'] == 'no']['job'].value_counts()
temp_1['Yes_deposit'] = data[data['y'] == 'yes']['job'].value_counts()    
ax[0].set_ylabel('Number of clients')
ax[0].set_title('Distribution of {} and deposit'.format('job'))
temp_1.plot.bar(ax=ax[0])

temp_2 = pd.DataFrame()
temp_2['No_deposit'] = data[data['y'] == 'no']['day_of_week'].value_counts()
temp_2['Yes_deposit'] = data[data['y'] == 'yes']['day_of_week'].value_counts()    
plt.ylabel('Number of clients')
ax[1].set_title('Distribution of {} and deposit'.format('day_of_week'))
temp_2.plot.bar(ax=ax[1])

temp_3 = pd.DataFrame()
temp_3['No_deposit'] = data[data['y'] == 'no']['education'].value_counts()
temp_3['Yes_deposit'] = data[data['y'] == 'yes']['education'].value_counts()    
plt.ylabel('Number of clients')
ax[2].set_title('Distribution of {} and deposit'.format('education'))
temp_3.plot.bar(ax=ax[2])

temp_4= pd.DataFrame()
temp_4['No_deposit'] = data[data['y'] == 'no']['cons_price_idx'].value_counts()
temp_4['Yes_deposit'] = data[data['y'] == 'yes']['cons_price_idx'].value_counts() 
 
ax[3].set_ylabel('Number of clients')
ax[3].set_title('Distribution of {} and deposit'.format('cons_price_idx'))
temp_4.plot.bar(ax=ax[3])
st.pyplot(fig)





st.write('')
st.write('')
st.markdown('After the above analysis, we can find that the customer is  occupation_and_the day of the week_for_promotion have important influence on whether the customer agrees to deposit_or_not')
st.markdown('The education level of customers and CPI are the same as them; At the same time, we found that these two groups of variables can influence each other, so we want to know:')
st.markdown('**The first question is that the number of people who in different occupations will agree to deposit money on different day of a week. And then exchange.**')
st.markdown('**The second question is that the number of people who will agree or disagree to deposit money in different CPI when they are in different considerably by education. And then exchange.**')
job_label= st.sidebar.radio(
     'Select job',
     ('management','services','admin.','blue-collar','entrepreneur','housemaid','retired','self-employed','student','technician','unemployed','unknown'))  
education_label= st.sidebar.radio(
     'Select education',
     ("basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown"))
day_of_week_label= st.sidebar.radio(
     'Select day',
     ('mon','tue','wed','thu','fri'))



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
st.write(data_forms)

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



for c in data.education: 
    if education_label==c:
         h=education_label
    else:
        pass
fig, ax = plt.subplots()
data_education_yes = data[data.education == h]
data_education_yes_group = data_education_yes.groupby('cons_price_idx')
d3 = data_education_yes_group.y.value_counts()
d3.plot(ax=ax,figsize=(20,10))
ax.set_title('Distribution of cons.price.idx and education') 
ax.set_xlabel('cons.price.idx ')
ax.set_ylabel('Number of clients')
st.pyplot(fig)


fig, ax = plt.subplots()
index = st.sidebar.slider('cons_price_idx', 90.00, 100.00)
for g in data.cons_price_idx: 
    if index==g:
        q=index
    else:
        pass
data_cpi_yes= data[data.cons_price_idx == q]
data_cpi_yes_group = data_cpi_yes.groupby('education')
d4=data_cpi_yes_group.y.value_counts()
d4.plot(ax=ax,figsize=(20,10))
st.pyplot(fig)
