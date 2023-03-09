# Skincare Recommendation App



Welcome to the Skincare Recommendation App project by Juanjo!

Use it yourself: https://juanjocr00-skincare-recommendation-app-skincare-xfb2oq.streamlit.app


Programming Languages: Python and SQL

The Skincare Recommendation App is a project aimed at providing personalized skincare recommendations to users based on their skin type, concerns, and preferences.

The app was built by using Python and utilizes libraries, including streamlit and Pandas. The app will feature a user-friendly interface that allows users to input their skin type, goal for the product, and product types. The app will then use this data to generate personalized skincare product recommendations sorted by price or rating.

For this project I used MySQL for data cleaning the original dataset. By using MySQL and creating a snowflake schema, I was able to create Primary and Foreign keys for each table to optimize the dataset I used.

The Dataset used for this project (link on Acknowledgments) contains information scraped from Sephora's website on 1472 skincare products and their ingredients. After the data cleaning process, only 927 were suited for my needs. In addition to their price, rating, and ingredients, each row also indicates if the product is recommended for combination, oily, dry, normal, or sensitive skin. The products can be one of the following categories: Face cream, Cleanser, Face mask, Treatment, Eye cream or Sun protection.
## App and Screenshots

Use it yourself: https://juanjocr00-skincare-recommendation-app-skincare-xfb2oq.streamlit.app

![App Screenshot](https://i.imgur.com/TFBXzTn.png)
## Dimensional model
![dimensional_model](https://i.imgur.com/LYlrIfi.png)
## Acknowledgements

 - [Dataset used for the project](https://www.kaggle.com/datasets/dominoweir/skincare-product-ingredients)

