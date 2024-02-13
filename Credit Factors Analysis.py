#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
print("Current working directory: {0}".format(os.getcwd()))
os.chdir('Project_1_Credit_Safari')

print("Current working directory: {0}".format(os.getcwd()))


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
 
# Load the dataset
import os
import pandas as pd
outname = 'credit_score.csv'

outdir = 'dir'
if not os.path.exists(outdir):
    os.mkdir(outdir)

credit_score = pd.read_csv(outname)

 
# Create the dataframe
credit_df = pd.DataFrame(credit_score)

print(credit_df.head())


# In[4]:


credit_df.columns


# In[5]:


plt.boxplot(credit_df['CURRENT_DEBT_TO_YEARLY_INCOME_RATIO'], labels =['Debt to income'])


# In[23]:


print(credit_df.corr())


# In[56]:


corr = credit_df.corr()['CREDIT_SCORE']


print(corr)


# In[58]:


credit_df.plot(x='CURRENT_DEBT_TO_YEARLY_INCOME_RATIO', y = 'CREDIT_SCORE', kind = 'scatter',  title='Negative Correlation 1')


# In[59]:


credit_df.plot(x='CURRENT_DEBT_TO_CURRENT_SAVINGS_RATIO', y = 'CREDIT_SCORE', kind = 'scatter',  title='Negative Correlation 2')


# In[66]:


credit_df.plot(x='YEARLY_EDUCATION_TO_YEARLY_INCOME_RATIO', y = 'CREDIT_SCORE', kind = 'scatter',  title='Negative Correlation 3')


# In[67]:


credit_df.plot(x='YEARLY_EXPENDITURE_TO_CURRENT_DEBT_RATIO', y = 'CREDIT_SCORE', kind = 'scatter',  title='Positive Correlation 1')


# In[68]:


credit_df.plot(x='YEARLY_UTILITIES_TO_CURRENT_DEBT_RATIO', y = 'CREDIT_SCORE', kind = 'scatter',  title='Positive Correlation 2')


# In[69]:


credit_df.plot(x='YEARLY_TAX_TO_CURRENT_DEBT_RATIO', y = 'CREDIT_SCORE', kind = 'scatter',  title='Positive Correlation 3')


# In[ ]:




