# Course Recommender Prototype
by [Ummuhan Demir](https://github.com/UmmuDem), December 2021



<a href="url"><img src="https://user-images.githubusercontent.com/55329025/145736875-983db9b4-82c7-4cc7-ba88-f9b171a66774.jpeg" align="center" height="400" width="800" ></a>


### Table of Contents  
[Project Description](#project-description)

[Dataset](#dataset)

[Cleaning](#cleaning)

[Models used](#models-for-content-based-recommendation)

[Recommender]

[Visualisations]

[Future Work](#future-work)




# Project Description

In daily life, all of us needs recommendations on basically everything and we should not hesitate about asking it. To learn new things that we haven't heard before or have been afraid of trying, recommendation system works really great. Similarly in the case that we encounter with a lot of choices of something and we can not decide which one we should choose, again it would be great to have 'someone' who knows us and guides us through it by his valuable recommendations based on our past experiences and knowledge. Of course, it is not quite possible to have that person. Soooo, let's create one. I think that as natural language processing is evolving, this kind of content-based recommendation systems will be more accurate and valuable. 

In this project I aimed to build a recommendation system for free courses in Coursera. The pandemic has an huge effect on the education system all around the world. Students not only get sicked of online lessons but also get used to it. As I am also an online math tutor right now, time to time I have to give recommendation to students about which online course they should follow.  However, it is not possible for me to go through syllabus of every course and recommend the good match with the student's need and knowledge. That is why I wanted to create a recommendation engine which does that for me. It is, of course, just a prototype but I am going to use it to get recommendation after I complete the course that is called '[Foundations of Data Science: K-Means Clustering in Python](https://www.coursera.org/learn/data-science-k-means-clustering-python)' in Coursera. 

# Dataset

The plan was the scrape 'coursera.org' to get course urls by using only BeautifulSoup and then scrape course webpages authomatically. Somehow I couldn't manage the first part. Because of that I used **Web Scraper** which is a google chrome extension I downloaded. As in the picture, we can see it while investigating the webpage. I used it just to get the course webpage urls.
<img width="1388" alt="Screenshot 2021-12-15 at 15 26 34" src="https://user-images.githubusercontent.com/55329025/146204648-fb277a69-42f1-4f72-b573-806dec3b8f2a.png">
Next I moved to python and scraped pages with the [urls](link koy) I obtained. In [this notebook], you can find code itself. I collected 1515 course data in the beginning. Then I decided to stick with the [courses in English](link koy) to avoid the noise which is created by the non-Latin alphetic languages. 

At the end, my data contains 911 rows with columns: course name, instructor, rating, number of rating, number of students who enrolled, category, subcategory, language(just English), syllabus, about and url of the course page.

# Cleaning
The usual data cleaning procedures were applied in [this notebook](link koy). I dropped nulls, cleaned some entries which were numeric by nature but came with description, eg. ratings came like '4.8stars'. 

# Exploration
I tried to understand the data better in Python column by column, checked what I have in them. Also, I got some bar graphs to see the distribution of the courses.

<img width="800" alt="Screenshot 2021-12-15 at 15 48 27" src="https://user-images.githubusercontent.com/55329025/146208197-da753449-183f-45a5-857c-d8f14b582e82.png">

# Models for Content Based Recommendation

- To be able to apply natural language processing, I created text corpus first by concataneting columns: name, level, category, subcategory, about and syllabus.
- I did some more cleaning, like removing numbers, special characters, punctuations and stopwords(I also added extra stopwords to nltk.stopwords) from the corpus, lemmatize the corpus.
- I used both [tfidf](https://scikitlearn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#:~:text=The%20formula%20that%20is%20used,document%20frequency%20of%20t%3B%20the) and [countvectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html?highlight=countvectorizer#sklearn.feature_extraction.text.CountVectorizer) as features extractor to compare the recomemdations. For these vectorizers, I applied [pairwise cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html?highlight=cosine%20similarity#sklearn.metrics.pairwise.cosine_similarity) to be able to recommend the courses with the most similar content.

<img width="563" alt="Screenshot 2021-12-15 at 17 37 33" src="https://user-images.githubusercontent.com/55329025/146229764-ed54f3eb-af36-4124-990f-27d05e5fb672.png"> The 4th recommendation is weird.
<img width="572" alt="Screenshot 2021-12-15 at 17 38 42" src="https://user-images.githubusercontent.com/55329025/146229837-c8ec9455-5472-4fbf-920f-7fbc66b42db4.png">

- I also used KNN after I vectorized corpus by using tfidf to get the nearest neighbors of the given input by using Euclidean distance. Actually, KNN did the worst job.
<img width="598" alt="Screenshot 2021-12-15 at 17 45 28" src="https://user-images.githubusercontent.com/55329025/146229234-a3205204-975d-4f29-9caa-a857e69c19a8.png">

- I decided to continue with the CountVectorizer because it gives courses more related with the given input(at least I thought it so).




Conclusion
Future Work

Tools
Links
