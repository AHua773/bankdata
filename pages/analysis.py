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



fig, ax = plt.subplots(2,1)
y_count=data.y.value_counts()
data.y.hist(ax=ax[0],figsize=(6,5))
plt.title("Is Y Yes and No")
labels =data['y'].value_counts(sort = True).index
sizes = data['y'].value_counts(sort = True)
plt.pie(sizes,labels=labels,autopct='%1.1f%%', shadow=True, startangle=270,)
plt.title('Yes and No categ',size = 12)
st.pyplot(fig)
with st.expander("See explanation"):
    st.write("""we saw that out of **more than 44,000** people,**less than 5,000** people accepted the business, and the success rate was 11.3%""")

st.write('')
st.write('')



from PIL import Image
image = Image.open('dataimage1.png')
st.subheader('**The graph to study the interaction between the various variables**')
st.image(image, caption='dataimage1.png',use_column_width=True)

st.subheader('**These graphs are made to conducted a separate analysis of each influencing factor, discussing the impact of its variables on success**')
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
