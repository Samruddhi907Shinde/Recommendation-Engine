# Recommendation-Engine

# Resturant Recomendation System

This project is an Resturant Recommendation System using Collabarative Filtering. It aims to build a recommender system which provides recommendations of other resturants when the user browses.

Collaborative filtering uses the ratings, and can recommend the resturants based on the ratings provided by the users.
The project is based on python and uses scipy, pandas, numpy, sklearn, streamlit, PIL, datetime libraries.

I have developed a web application using the streamlit library in which user enters the resturant name and when the submit button is pressed the recommendations for the resturant will be displayed.
On the same page in the sider section the facility for addition of new resturants , addition of user rating for the resturants is provided. User can add a new resturant and the ratings.

# About Algorithms :

In this project Pivot table is created from 'ratings' csv file and then the sparsity is removed by using csr_matrix.
Then the new 'Linear' index is recreated for the dataset.
Nearest Neighbor implements unsupervised nearest neighbors learning.Cosine Similarity is applied on csr matrix. This matrix is used to fit the nearest neighbors estimaters using brute Force algorithm.

# Implementation : 

Assuming that python is installed with all the essential libraries
Run RecommendationSystem.py in python .
After successful running, go to terminal and type the command "streamlit run RecommendationSystem.py" and press enter.
After that you will get a local url link . Press on the link to open the web application. Now you can enter Resturant Name e.g. 'Hong Kong Cafe' and submit you will get the Resturant Recommendations. Also you can add a new resturant and user ratings in sidebar.

# Limitation : 

When we add a new Resturant and find its recommendations then more user ratings should be given for that resturant to get more accurate results.
