#!/usr/bin/env python
# coding: utf-8

# # Course Recommender

# ## Import Libraries

# In[1]:


# data cleaning and EDA
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# text analysis
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import string


# ## Bring in Clean Data

# In[2]:


df = pd.read_csv('clean_data.csv')


# In[3]:


#df.head(1)


# In[4]:


#str(df['syllabus'])


# ## Create the Corpus

# I will combine all categorical columns except language.

# In[5]:


df["corpus"] = df["name"].map(str) + " " + df["instructor"].map(str) +" "+ df["level"].map(str)+ " "+df['category'].map(str)+" "+df['subcategory'].map(str) +" "+ df['about'].map(str) + df['syllabus'].map(str) 
#df["corpus"][0]


# In[6]:


#df.head()


# ## Data Cleaning/Wrangling

# - From corpus, I am going to remove stopwords which I expanded a little, remove special characters and punctuations. Then I tokenize it.

# In[7]:


stop_words = set(stopwords.words('english'))
stop_words.update(['course','module','introduction','will','week','learn','video','part','lecture','video','using','system','one','new','use','first','s','work'])

wn = WordNetLemmatizer()

def black_txt(token):
    return  token not in stop_words and token not in list(string.punctuation)  and len(token)>2   
  
def clean_txt(text):
    clean_text = []
    clean_text2 = []
    text = re.sub("'", "",text)
    text=re.sub("(\\d|\\W)+"," ",text) 
    text = text.replace("nbsp", "")
    clean_text = [ wn.lemmatize(word, pos="v") for word in word_tokenize(text.lower()) if black_txt(word)]
    clean_text2 = [word for word in clean_text if black_txt(word)]
    return " ".join(clean_text2) 


# print(stop_words) 
# print('\n')
# print('the length of expanded stop words set: {}'.format(len(stop_words)))

# In[9]:


df['corpus'] = df['corpus'].apply(lambda x: clean_txt(x))


# In[10]:


#df.head()


# ## Work Cloud

# In[11]:


from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# In[12]:


def get_wordcloud(text,coursename):
    bunch_text = " ".join(text for text in text.split(' '))
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", colormap= "magma").generate(bunch_text)
    plt.figure(figsize=[11,11])
    plt.imshow(wordcloud, interpolation="sinc")
    plt.axis("off")
    title = coursename
    plt.title('Course Name: ' + title.title(), fontsize=15)

    plt.show()
    return


# ## Using TFIDF

# In[13]:


#initializing tfidf vectorizer for feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

# for getting similarity
from sklearn.metrics.pairwise import cosine_similarity

tfidf_vectorizer = TfidfVectorizer()


# **Functions to be used:**

# In[14]:


# returns all the similarity scores between the given user_input and other entries

def get_cos_similarity_scores(user_input,vectorizer,vectorized_corpus):
    tokens = [str(tok) for tok in word_tokenize(user_input)]
    user_tfidf = vectorizer.transform(tokens)
    cos_similarity = map(lambda x: cosine_similarity(user_tfidf, x),vectorized_corpus)
    output = list(cos_similarity)
    return output


# In[15]:


# always first we need to vectorize a given input

def get_user_vectorized(user_input,vectorizer,vectorized_corpus):
    tokens = [str(tok) for tok in word_tokenize(user_input)]
    user_tfidf = vectorizer.transform(tokens)
    return user_tfidf


# In[16]:


# fit the data to apply the model

TFIDF = tfidf_vectorizer.fit_transform((df['corpus']))

# gives the five most similar results by using cosine similarity

def get_recommendation_TFIDF(user_input,df):
    output = get_cos_similarity_scores(user_input,vectorizer = tfidf_vectorizer,vectorized_corpus =  TFIDF)
    top = sorted(range(len(output)), key=lambda i: output[i][0], reverse=True)[:5]
    list_scores = [output[i][0][0] for i in top]
    
    recommendation = pd.DataFrame(columns = ['name',  'instructor','rating', 'score','index'])
    count = 0
    best_index = list()
    for i in top:
        recommendation.at[count, 'name'] = df['name'][i]
        recommendation.at[count, 'instructor'] = df['instructor'][i]
        recommendation.at[count, 'rating'] = df['rating'][i]
        recommendation.at[count, 'score'] =  list_scores[count]
        index = list(df. index)
        recommendation['index'][count] = i
        count += 1
        best_index.append(i) 
    return recommendation, best_index


# In[17]:


# example

#get_recommendation_TFIDF('python programming',df)[0]


# ## Using CountVectorizer

# In[18]:


#initializing count vectorizer for feature extraction

from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer()


# In[19]:


# fit the data into count vectorizer

CV = count_vectorizer.fit_transform((df['corpus']))

# gives the five most similar results by using cosine similarity

def get_recommendation_CV(user_input,df):
    output = get_cos_similarity_scores(user_input,vectorizer = count_vectorizer, vectorized_corpus= CV)
    top = sorted(range(len(output)), key=lambda i: output[i][0], reverse=True)[:5]
    list_scores = [output[i][0][0] for i in top]
    
    recommendation = pd.DataFrame(columns = ['name',  'instructor','rating', 'score','index'])
    count = 0
    best_index = list()
    for i in top:
        recommendation.at[count, 'name'] = df['name'][i]
        recommendation.at[count, 'instructor'] = df['instructor'][i]
        recommendation.at[count, 'rating'] = df['rating'][i]
        recommendation.at[count, 'score'] =  list_scores[count]
        index = list(df. index)
        recommendation['index'][count] = i
        count += 1
        best_index.append(i) 
    return recommendation, best_index


# In[20]:


#get_recommendation_CV('python programming',df)[0]


# ## Using KNN

# In[21]:


from sklearn.neighbors import NearestNeighbors

def get_NNS(user_input,n_neighbors,vectorizer, vectorized_corpus):   # vectorized_corpus could be TFIDF or CV
    KNN = NearestNeighbors(n_neighbors, p=2)
    KNN.fit(vectorized_corpus)
    user_tfidf = get_user_vectorized(user_input,vectorizer,vectorized_corpus)
    NNs = KNN.kneighbors(user_tfidf, return_distance=True) 
    return NNs


# In[22]:


def get_recommendation_KNN(user_input,df):
    top = get_NNS(user_input,6,vectorizer=tfidf_vectorizer, vectorized_corpus=TFIDF)[1][0][1:]
    index_score = get_NNS(user_input,6,vectorizer=tfidf_vectorizer, vectorized_corpus=TFIDF)[0][0][1:]
    recommendation = pd.DataFrame(columns = ['name',  'instructor','rating', 'score','index'])
    count = 0
    best_index = list()
    for i in top:
        recommendation.at[count, 'name'] = df['name'][i]
        recommendation.at[count, 'instructor'] = df['instructor'][i]
        recommendation.at[count, 'rating'] = df['rating'][i]
        recommendation.at[count, 'score'] =  index_score[count]
        index = list(df. index)
        recommendation['index'][count] = i
        count += 1
        best_index.append(i) 
    return recommendation, best_index
    


# In[23]:


#get_recommendation_KNN('python programming',df)[0]


# **Summary:**
# - More or less all three models give the same courses when I enter 'python programming' as keyword, but I choose the count vectorizer to build my recommendation engine. Because in the top five list of it, we don't see 'Global Warming ... ' course.

# # New aspect 

# So far recommendations were done by using user input as keywords. 
# Now, I expand it to that scenerio: if user puts a course that he has already completed in Coursera, I want to recommend similar courses to continue learning and reinforce his knowledge.

# In[24]:


# if user enters a course name, it finds the corresponding course

def locate_corpus_by_name(user_input,df):
    user_input = user_input.lower()
    df['name']= df['name'].str.lower()
    new = df.loc[df.name == user_input, 'corpus'].values[0]
    return new


# In[25]:


# machine learning is a course name

user_input = locate_corpus_by_name('machine learning',df)


# In[26]:


#user_input


# In[ ]:





# # Recommender 

# In[27]:


def recommender():
    response = input( "\033[1m" + """
                        Welcome to the Coursera course recommender! (It contains only free courses.)
                        Are you new here?(yes/no): """).lower().replace(" ", '')
    while response == 'yes':
        query_sentence = input("\033[1m" + """
                        I am glad you prefer studying today!
                        What do you want to learn? Give me some keywords that are important for you: 
                        """).lower()
            
        best_index = get_recommendation_CV(query_sentence,df)[1]
        #print(best_index)
        if len(best_index)==0:
            response = input("\033[1m" + """
                        Sorry, couldnt find a good match. Do you want to try again? (yes/no)
                        """)
            if response == 'yes':
                print("\033[1m"+ """
                        This time please give more details.
                        """)
            if response == 'no':
                print("\033[1m"+ """
                        Please don't quit on studying. See you later!
                        """)
            
        elif len(best_index)!=0:
            print("\033[1m"+"""
                        We have five courses for you, choose according to your level: """)
            
            for i in list(best_index):
                course_name = df['name'].iloc[i]
                instructor = df['instructor'].iloc[i]
                level = df['level'].iloc[i]
                url = df['url'].iloc[i]
                corpus = df['corpus'].iloc[i]
                print("\033[1m"+ """ 
                            {}: 
                            {} 
                            by {}.
                            Here is the link of the course, you can dive into get an idea whether it fits your need 
                            {}
                            """.format(level,"\u0332".join(course_name.title()),instructor,url))
            
            response = 'no'
            return 
        
    
            
    while response == 'no':
        query_sentence = str(input("\033[1m" + """
                            How nice you are back! Which course have you completed?(Full course name please)
                                """).lower())
        
        
        if query_sentence not in list(df['name']):
            response = input("\033[1m" + """
                        Sorry, you couldn't write the course name. Do you want to try again? (yes/no)
                        """)
            if response == 'yes':
                 query_sentence = str(input("\033[1m" + """
                            How nice you are back! Which course have you completed?(Full course name please)
                                """).lower())
            if response == 'no':
                print("\033[1m"+ """
                            Please don't quit on studying. See you later!
                        """)
                return
          
        query = locate_corpus_by_name(query_sentence,df)
        #print(query)
        best_index = get_recommendation_CV(query,df)[1]
        if len(best_index)!=0:
           
    
        #print(best_index)
            print("\033[1m"+"""
                        We have some courses for you, choose according to your level: """)
            
            for i in list(best_index):
                course_name = df['name'].iloc[i]
                instructor = df['instructor'].iloc[i]
                level = df['level'].iloc[i]
                url = df['url'].iloc[i]
                corpus = df['corpus'].iloc[i]
                if course_name != query_sentence:
                    print("\033[1m"+ """ 
                            {}: 
                            {} 
                            by {}
                            Here is the link of the course, you can dive into get an idea whether it fits your need 
                            {}""".format(level,"\u0332".join(course_name.title()),instructor,url))
                   
            response = 'yes'
            return
        








# bunch_text = " ".join(text for text in df['corpus'][110].split(' '))

# stopwords = set(list(STOPWORDS))
# stopwords.update(['course','module','introduction','will','week','learn','video','part','lecture','video','using','system','one','new','use','first','s','work'])
# 
# wordcloud = WordCloud(stopwords=stopwords, background_color="white", colormap= "magma").generate(bunch_text)

# from IPython.core.display import HTML
# HTML("""
# <style>
# .output_png {
#     display: table-cell;
#     text-align: center;
#     vertical-align: middle;
# }
# </style>
# """)

# plt.figure(figsize=[11,11])
# plt.imshow(wordcloud, interpolation="sinc", )
# plt.axis("off")
# title = df['name'].iloc[110]
# plt.title('Course Name: ' + title, fontsize=15)
# 
# plt.show()
# 

# In[ ]:




