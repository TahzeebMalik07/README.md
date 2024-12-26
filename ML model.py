#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
data= pd.read_csv("stud.csv")


# In[2]:


data.shape


# In[3]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[4]:


data.head(6)


# In[5]:


data.shape


# In[6]:


data.info()


# In[7]:


data.isnull().sum()


# In[8]:


data['Courses'].value_counts()


# In[9]:


from imblearn.over_sampling import SMOTE

# SMOTE is used to handle the imbalanced data
smote = SMOTE(random_state=42)


X = data.drop('Courses', axis=1)
y = data['Courses']

X_resampled, y_resampled = smote.fit_resample(X, y)


# In[10]:


y_resampled.value_counts()


# In[11]:


label_encoder = LabelEncoder()


data['Courses_label'] = label_encoder.fit_transform(data['Courses'])


data['Courses_label'].value_counts()
y=data['Courses_label']


# In[12]:



categorical_columns = ['Drawing','Dancing','Singing','Sports','Video Game','Acting','Travelling','Gardening','Animals','Photography','Teaching','Exercise','Coding','Electricity Components','Mechanic Parts','Computer Parts','Researching','Architecture','Historic Collection','Botany','Zoology','Physics','Accounting','Economics','Sociology','Geography','Psycology','History','Science','Bussiness Education','Chemistry','Mathematics','Biology','Makeup','Designing','Content writing','Crafting','Literature','Reading','Cartooning','Debating','Asrtology','Hindi','French','English','Urdu','Other Language','Solving Puzzles','Gymnastics','Yoga','Engeeniering','Doctor','Pharmisist','Cycling','Knitting','Director','Journalism','Bussiness','Listening Music']  # Replace with your categorical columns


label_encoders = {}

for col in categorical_columns:
    label_encoder = LabelEncoder()
    data[col] = label_encoder.fit_transform(data[col])
    label_encoders[col] = label_encoder


# In[13]:


data.head()


# In[14]:


#drop the feature Course and stored data into variable dataab
dataab=data.drop(['Courses'],axis=1)


# In[15]:


dataab.head()


# In[16]:



X=['Drawing','Dancing','Singing','Sports','Video Game','Acting','Travelling','Gardening','Animals','Photography','Teaching','Exercise','Coding','Electricity Components','Mechanic Parts','Computer Parts','Researching','Architecture','Historic Collection','Botany','Zoology','Physics','Accounting','Economics','Sociology','Geography','Psycology','History','Science','Bussiness Education','Chemistry','Mathematics','Biology','Makeup','Designing','Content writing','Crafting','Literature','Reading','Cartooning','Debating','Asrtology','Hindi','French','English','Urdu','Other Language','Solving Puzzles','Gymnastics','Yoga','Engeeniering','Doctor','Pharmisist','Cycling','Knitting','Director','Journalism','Bussiness','Listening Music']


X_df = dataab[X]


Y = dataab['Courses_label']


# In[17]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X_df, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
    
print(f"Accuracy: {accuracy:.2f}")

classification_rep = classification_report(y_test, y_pred)
print("Classification Report:\n", classification_rep)
print("Confusion Matrix:\n", conf_matrix)


# In[18]:


import joblib


joblib.dump(model , 'model .pkl')
import joblib


loaded_model = joblib.load('model .pkl')


# In[20]:


user_input = {}
feature_names=['Drawing','Dancing','Singing','Sports','Video Game','Acting','Travelling','Gardening','Animals','Photography','Teaching','Exercise','Coding','Electricity Components','Mechanic Parts','Computer Parts','Researching','Architecture','Historic Collection','Botany','Zoology','Physics','Accounting','Economics','Sociology','Geography','Psycology','History','Science','Bussiness Education','Chemistry','Mathematics','Biology','Makeup','Designing','Content writing','Crafting','Literature','Reading','Cartooning','Debating','Asrtology','Hindi','French','English','Urdu','Other Language','Solving Puzzles','Gymnastics','Yoga','Engeeniering','Doctor','Pharmisist','Cycling','Knitting','Director','Journalism','Bussiness','Listening Music']

for feature in feature_names:
    user_value = float(input(f"Enter value for {feature} (0 or 1): "))
    user_input[feature] = user_value


user_data = pd.DataFrame([user_input])


missing_columns = set(X_train.columns) - set(user_data.columns)
for column in missing_columns:
    user_data[column] = 0  


prediction = model.predict(user_data)


numeric_to_category = {
    0: 'Animation, Graphics and Multimedia',
    1: 'B.Arch- Bachelor of Architecture',
    2: 'B.Com- Bachelor of Commerce',
    3: 'B.Ed.',
    4: 'B.Sc- Applied Geology',
    5: 'B.Sc- Nursing',
    6: 'B.Sc. Chemistry',
    7: 'B.Sc. Mathematics',
    8: 'B.Sc.- Information Technology',
    9: 'B.Sc.- Physics',
    10: 'B.Tech.-Civil Engineering',
    11: 'B.Tech.-Computer Science and Engineering',
    12: 'B.Tech.-Electrical and Electronics Engineering',
    13: 'B.Tech.-Electronics and Communication Engineering',
    14: 'B.Tech.-Mechanical Engineering',
    15: 'BA in Economics',
    16: 'BA in English',
    17: 'BA in Hindi',
    18: 'BA in History',
    19: 'BBA- Bachelor of Business Administration',
    20: 'BBS- Bachelor of Business Studies',
    21: 'BCA- Bachelor of Computer Applications',
    22: 'BDS- Bachelor of Dental Surgery',
    23: 'BEM- Bachelor of Event Management',
    24: 'BFD- Bachelor of Fashion Designing',
    25: 'BJMC- Bachelor of Journalism and Mass Communication',
    26: 'BPharma- Bachelor of Pharmacy',
    27: 'BTTM- Bachelor of Travel and Tourism Management',
    28: 'BVA- Bachelor of Visual Arts',
    29: 'CA- Chartered Accountancy',
    30: 'CS- Company Secretary',
    31: 'Civil Services',
    32: 'Diploma in Dramatic Arts',
    33: 'Integrated Law Course- BA + LL.B',
    34: 'MBBS'
   }


prediction = model.predict(user_data)


numeric_prediction = prediction[0]


if numeric_prediction in numeric_to_category:
    categorical_prediction = numeric_to_category[numeric_prediction]


#
print("i sugest you to go with ", categorical_prediction)


# In[ ]:





# In[ ]:




