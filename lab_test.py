#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

arr1 = np.array([["Electronics", 'I4'],
                ["Groceries", 'I4'],
                ["Clothing", 'I4'],
                ["Furniture", 'I4'],
                ["Stationery", 'I4']])


# In[4]:


arr = [[120, 500, 230, 75, 45], 
       [130, 520, 210, 80, 40], 
       [125, 530, 220, 70, 50], 
       [140, 540, 200, 90, 60]]


# In[ ]:


data = {
    "Electronics" = [120, 500, 230, 75, 45],
    "Groceries" = [130, 520, 210, 80, 40],
    "Furniture" = [125, 530, 220, 70, 50],
    "Stationery" = [140, 540, 200, 90, 60]
}


# In[ ]:


int sum = 0;
def totalUnits(a):
    


# In[5]:


print(arr)


# In[36]:


arr1[0] = [120, 130, 125, 140]
arr1[1] = [500, 520, 530, 540]
arr1[2] = [230, 210, 220, 200]
arr1[3] = [75, 80, 70, 90]
arr1[4] = [45, 40, 50, 60]


# In[9]:


arr1 = [[120, 130, 125, 140],
        [500, 520, 530, 540],
        [230, 210, 220, 200],
        [75, 80, 70, 90],
        [45, 40, 50, 60]]


# In[10]:


print(arr1)


# In[16]:


def total_unit(arr):
    sum = 0
    l = []
#     l[0] = sum += arr[0]
    for i in arr:
        sum += arr[0, i]
        l[i] = sum
    return l


# In[17]:


print(total_unit(arr1))


# In[22]:


def week(arr, j):
    sum = 0
    for i in arr:
        sum += arr[j, i]
        return sum


# In[20]:


def average(arr, j):
    sum = 0
    for i in arr:
        for j in range(0, 5):
            sum += arr[j, i]
            return sum / 4


# In[37]:


def sumi(arr, j):
    sum = 0
    for i in arr[j]:
        sum += i
        return sum


# In[38]:


print(sumi(arr1, 0))


# In[43]:


# import matplotlib.pyplot as plt
# # a0 = a1 = a2 = a3 = []
# a = []
# a[0]=sumi(arr1, 0) 
# a[1]=sumi(arr1, 1)
# a[2]=sumi(arr1, 2)
# a[3]=sumi(arr1, 3)
# # arrq = [a0,a1,a2,a3]

a = []
for j in range(5):
    a.append(sumi(arr1, j))

week = ['w1', 'w2', 'w3', 'w4', 'w5']
# for a, sales in arr1:
#     plt.plot(a, sales)
# plt.line()

plt.bar(week, a)
# plt.legend()
plt.title("Product vs Week")
plt.xlabel("Week")
plt.ylabel("Product Data")
plt.show()


# In[ ]:


def worst(arr):
    int mini =0
    for i in arr:
        sumi(arr, i)
        mini = min(sumi, mini)
        return mini


# In[ ]:


def best(arr):
    int maxi =0
    for i in arr:
        sumi(arr, i)
        maxi = max(sumi, maxi)
        return maxi


# In[ ]:


def total_sales(arr):
    return [sum(product_sales) for product_sales in arr]

sales_totals = total_sales(arr1)

product_labels = [f'Product {i + 1}' for i in range(len(arr1))]

plt.bar(product_labels, sales_totals, color='skyblue')
plt.title("Total Sales of Product Categories")
plt.xlabel("Product Categories")
plt.ylabel("Total Sales")
plt.show()

