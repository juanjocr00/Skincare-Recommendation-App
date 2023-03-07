### Import the libraries ###
import pandas as pd
import streamlit as st
import base64

### Set the page to always wide ###
st.set_page_config(layout="wide")

### Add a background image to the Streamlit App  ###
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Resources/background.jpg')    

### Read all the Datasets from the Dataset folder ###
product = pd.read_excel('./Dataset/products.xlsx')
skin_type = pd.read_excel('./Dataset/dim_skin_type.xlsx')
product_type = pd.read_excel('./Dataset/dim_product_type.xlsx')
brand = pd.read_excel('./Dataset/dim_brand.xlsx')
ingredients = pd.read_excel('./Dataset/dim_ingredients.xlsx')

### Create title and header for the App ###
st.title("Skincare products for you!")
st.header("Criteria Selection for the product:")

### Add the Selectboxes for the different criteria selection for the recommendation engine ###
col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    criteria_1 = st.selectbox("Type of product:",[ "All", "Face cream", "Cleanser", "Sun protect", "Treatment", "Eye cream", "Face Mask"])
with col1:
    criteria_2 = st.selectbox("Your skin type:", ["Dry", "Oily", "Combination", "Normal", "Sensitive"])
with col2:
    criteria_3 = st.selectbox("What are you lookink for?", ["Moisturizing", "Skin Protection", "Anti-wrinkle", "Anti-inflammatory", "Skin tone and texture" , "Anti-acne"])

### Add a Selectbox for choosing in which criteria the user would like to sort te products selection ###
sort1, sort2, sort3, sort4 = st.columns([1,1,1,1])
with sort1:
    criteria_sort = st.selectbox("Sort By:", ["Lowest price", "Highest price", "Best rating", "Worst rating"]) 

### Use the criteria given by the user to just show the protuct type of their choice from the dataset ###
if criteria_1 == "All":
    filtered_df_1 = product_type[product_type["product_type"] == product_type["product_type"].tolist()]
elif criteria_1 == "Face cream":
    filtered_df_1 = product_type[product_type["product_type"] == "Moisturizer"]
else:
    filtered_df_1 = product_type[product_type["product_type"] == criteria_1]

### Use the criteria given by the user to just show the skin type of their choice from the dataset ###
if criteria_2 == "Dry":
    filtered_df_2 = skin_type[skin_type["skin_dry"] == 1]
elif criteria_2 == "Oily":
    filtered_df_2 = skin_type[skin_type["skin_oily"] == 1]
elif criteria_2 == "Combination":
    filtered_df_2 = skin_type[skin_type["skin_combination"] == 1]
elif criteria_2 == "Normal":
    filtered_df_2 = skin_type[skin_type["skin_normal"] == 1]
elif criteria_2 == "Sensitive":
    filtered_df_2 = skin_type[skin_type["skin_sensitive"] == 1]

### Use the criteria given by the user to just show the purpose of the product of their choice from the dataset ###
### Each criteria have its own set of active ingredients depending on the goal with the product ###
if criteria_3 == "Moisturizing":
    active_ingredients = ["fatty acid", "Hyaluronic acid", "Glycerin", "Urea", "Aloe", "panthenol"]
    filtered_df_3 = ingredients[ingredients['ingredients'].str.contains('|'.join(active_ingredients), case=False)]        
elif criteria_3 == "Skin Protection":
    active_ingredients = ["Vitamin E", "Vitamin C", "Niacinamide", "Ferulic acid", "Zinc", "Hyaluronic acid",  "Butyl Methoxydibenzoylmethane"]
    filtered_df_3 = ingredients[ingredients['ingredients'].str.contains('|'.join(active_ingredients), case=False)]
elif criteria_3 == "Anti-wrinkle":
    active_ingredients = ["Retin", "Peptide", "Hyaluronic Acid", "Antioxidant", "Vitamin E", "Vitamin C", "green tea", "resveratrol", "Glycolic", "Algae"]
    filtered_df_3 = ingredients[ingredients['ingredients'].str.contains('|'.join(active_ingredients), case=False)]
elif criteria_3 == "Anti-inflammatory":
    active_ingredients = ["Aloe", "Green tea", "Chamomile", "Niacinamide", "Licorice", "Calendula", "Bisabolol"]
    filtered_df_3 = ingredients[ingredients['ingredients'].str.contains('|'.join(active_ingredients), case=False)]
elif criteria_3 == "Skin tone and texture":
    active_ingredients = ["Vitamin C", "Retin", "Niacinamide", "Peptide", "Salicylic acid", "glycolic", "lactic acid", "AHA"]
    filtered_df_3 = ingredients[ingredients['ingredients'].str.contains('|'.join(active_ingredients), case=False)]
elif criteria_3 == "Anti-acne":
    active_ingredients = ["Salicylic acid",  "Retin", "Niacinamide", "Zinc", "Tea tree"]
    filtered_df_3 = ingredients[ingredients['ingredients'].str.contains('|'.join(active_ingredients), case=False)]        

### With all the criteria given, filter from the main datasets to show the recommendations with only those criterias being used to display ###
filter1 = product[product["type_id"].isin(filtered_df_1.type_id)]
filter2 = filter1[filter1["product_id"].isin(filtered_df_2.product_id)]
filter3 = filter2[filter2["product_id"].isin(filtered_df_3.product_id)]

### Merge the product datframe and the brand dataframe when the correct brand_id in both datafarmes ###
df1=pd.DataFrame(filter3)
df2=pd.DataFrame(brand)
df_merged = pd.merge(df1, df2, on='brand_id')

### Sort the products based on the criteria given by the user ###
if criteria_sort == 'Lowest price':
    filter4 = df_merged.sort_values('product_price', ascending=True)
elif criteria_sort == 'Highest price':
    filter4 = df_merged.sort_values('product_price', ascending=False)
elif criteria_sort == 'Best rating':
    filter4 = df_merged.sort_values('product_rating', ascending=False)
elif criteria_sort == 'Worst rating':
    filter4 = df_merged.sort_values('product_rating', ascending=True)



### Add a header for the list of recommended products###
st.header("Product recommendations:")
### Establish a different column for Procuct name, Brand, Rating and Price ###
col_1, col_2, col_3, col_4 = st.columns([4.5, 2, 1, 1])
### Number of rows of products to show in each column ###
c_max=10
c_1=0
c_2=0
c_3=0
c_4=0
### Display the product name, brand name, rating and price in each column ###
with col_1:
    st.subheader("Product Name: ")
    for i in filter4["product_name"]:
        st.write(i)
        st.write('\n')
        c_1=c_1+1
        if c_1==c_max:
            break

with col_2:
    st.subheader("Brand: ")
    for k in filter4["brand_name"]:
        st.write(k)
        st.write('\n')
        c_3=c_3+1
        if c_3==c_max:
            break

with col_3:
    st.subheader("Rating: ")
    for j in filter4["product_rating"]:
        st.write("{:.1f}".format(j))
        st.write('\n')
        c_2=c_2+1
        if c_2==c_max:
            break

with col_4:
    st.subheader("Price: ")
    for l in filter4["product_price"]:
        st.write("%s USD" % (l) )
        st.write('\n')
        c_4=c_4+1
        if c_4==c_max:
            break

### Display a expandable box to show a table with all the products ###
with st.expander("Show all products " + '(%s):'%len(filter4)):
    ### Drop the columns that are not desire to show in the expandable box ###
    filter4 = filter4.drop(['product_id', 'brand_id'], axis=1)
    filter4 = filter4[['product_name', 'brand_name', 'product_rating', 'product_price']]
    filter4 = filter4.rename(columns={'product_name': 'Product name', 'brand_name':'Brand', 'product_rating' : 'Rating', 'product_price': 'Price'})
    st.table(filter4)
