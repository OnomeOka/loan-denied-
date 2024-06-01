#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[31]:


df=pd.read_csv('loan.csv')


# In[32]:


df.head()


# In[33]:


df.isnull().sum()


# In[34]:


df.duplicated()


# In[35]:


df.describe()


# In[36]:


denied_loans=df[df['loan_status']=='Denied']


# In[37]:


num_denied_loans=denied_loans.shape[0]
print(f"Number of loans denied:{num_denied_loans}")


# In[38]:


# Analyze the credit scores for denied loans
denied_credit_scores = denied_loans['credit_score']
print('Credit scores of denied loans:')
print(denied_credit_scores.describe())


# In[39]:


#Visualize the distribution for credit scores for denied loans
plt.figure(figsize=(10, 6))
plt.hist(denied_credit_scores, bins=30, edgecolor='k')
plt.title('Distribution of Credit Scores for Denied Loans')
plt.xlabel('Credit score')
plt.ylabel('Count')
plt.show()



# In[40]:


# Compare credit score distributions for the approved and denied loans
approved_loans = df[df['loan_status'] == 'Approved']
approved_credit_scores = approved_loans['credit_score']


# In[44]:


plt.figure(figsize=(10, 6))
plt.hist(approved_credit_scores, bins=30, alpha=0.5, label='Approved', edgecolor='k')
plt.hist(denied_credit_scores, bins=30, alpha=0.5, label='Denied', edgecolor='k')
plt.title('Credit Score Distribution for Approved and Denied Loans')
plt.xlabel('Credit Score')
plt.ylabel('count')
plt.legend()
plt.show()


# In[ ]:




