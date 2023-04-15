import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import json

st.set_page_config(
    page_title=' Paragon Technology and Innovation Sales Analysis ',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)


# Create Run Function
def run():
    # Membuat Title
    st.title('Paragon Technology and Innovation Sales Analysis')

    # Subheader
    st.subheader('Time Series Forecast')

    # Menambahkan gambar
    image = Image.open('./growth.jpg')
    st.image(image)

    # Menambahkan deskripsi
    st.write('## Introduction')
    st.write(
    '''
Forecasting the quantity of product sales is essential for any business, regardless of its size or industry. It enables businesses to anticipate market trends, customer behavior, and demand patterns, which are all critical factors that directly impact the business's bottom line. The ability to predict future product sales accurately can help businesses make informed decisions about production, inventory management, pricing, and marketing strategies. This, in turn, can help businesses optimize their operations, minimize risks, and maximize profits.

At Paragon Innovation, we understand the importance of accurate product sales forecasting for businesses looking to gain a competitive edge. Our team of experts uses cutting-edge forecasting models and advanced analytics techniques to help businesses predict future sales with precision. We work closely with our clients to understand their unique needs and tailor our forecasting solutions to meet their specific requirements.

Whether you are a small business owner or a large corporation, forecasting your product sales is critical for your success. With Paragon Innovation's forecasting solutions, you can gain insights into your business's future and make data-driven decisions that drive growth and profitability.
The objective of this project is not just to create a forecasting model, but to create one that accurately predicts Iekly sales for the next month. It's not just about making guesses, but about using historical sales data to identify patterns and trends, and making predictions based on those patterns. Beyond that, I will try to analyze how the performance of each products towards the set KPI, which I will assume based on the average of sales. By doing so, I hope I can help Paragon to plan their inventory and staffing levels more effectively, ensuring that they are always prepared for changes in demand.

To achieve this goal, I will take the following steps: 
- Gather historical sales data and analyze it to identify trends and patterns that could be useful in predicting future sales. 
- I will select an appropriate forecasting model and train it using the historical data, adjusting the parameters as necessary to optimize performance. 
- I will then evaluate the model using a holdout dataset, making any necessary adjustments to ensure its accuracy and reliability. 
- Finally, I will use the trained model to forecast Iekly sales for the next month based on the most recent sales data available.    
    '''
    )
    
    # Membuat garis lurus
    st.markdown('-'*42)

    st.write('## Table')
    # Show DF
    df = pd.read_csv('./data.csv')
    st.dataframe(df)

    # change dtype of week_start_date and week_end)date
    df['week_start_date'] = pd.to_datetime(df['week_start_date'])
    df['week_end_date'] = pd.to_datetime(df['week_end_date'])
    
    st.write('## Product Sold Trend ')
    # product sold trend
    fig, ax = plt.subplots(figsize=(20,5))
    sns.lineplot(data=df, x='week_end_date', y='quantity')
    # Display the plot in Streamlit
    st.pyplot(fig)
    st.write("""
    on the chart above, there is no seasonal pattern found on the data. the time series trend where the magnitude of the trend changes over time. In other words, the growth rate of the trend is not constant but varies. in other words the trend and seasonal are `multiplicative`.
    """)


    st.write('## Product Performance')
    # create new df grouped by product
    df_product = df.groupby(['product_item']).agg(
        total_quantity=('quantity', 'sum'),
        total_days_sold=('week_end_date', lambda x: (max(x) - min(x)).days +1)
    )
    # calculate days to sell 3000 products
    df_product['days_to_sell_3000'] = 3000 / df_product['total_quantity'] * df_product['total_days_sold']
    df_product['category'] = df_product['days_to_sell_3000'].apply(lambda x: 'in a day' if x <= 1 else 'in a week' if x > 1 and x <= 7 else 'in a month' if x > 7 and x <= 30 else '1-3 month' if x > 30 and x <= 90 else 'more than 3 month')
    df_product = df_product.reset_index()
    st.dataframe(df_product)
    st.write("""
    - total_quantity: accumulated product sold
    - total_days_sold: total days needed to sell `total_quantity`'s product
    - days_to_sell_3000: total days needed to sell 3,000 pcs product
    - category: time needed for a product to sell 3,000 products

    **I use 3,000 as baseline from the average quantity sold**
    """)

    st.write('## Product Category Proportion')
    # calculate percentage of each category
    df_product['percentage'] = df_product['total_quantity'] / df_product['total_quantity'].sum() * 100

    # create donut plot
    fig = px.pie(df_product, values='percentage', names='category', hole=.5, color_discrete_sequence=px.colors.qualitative.Pastel)

    # display plot in Streamlit
    st.plotly_chart(fig)

    st.write('## Product CategoryPerformance')
    # Create bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_product, x='category', y='total_quantity', ax=ax, errorbar=None)

    # Show values on top of bars
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'),
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 10),
                    textcoords='offset points')

    # Add labels and title
    ax.set_xlabel('Category', fontsize=14)
    ax.set_ylabel('Total Quantity', fontsize=14)
    ax.set_title('Product Sales by Category', fontsize=16)

    # Display plot in Streamlit
    st.pyplot(fig)



# calling function
if __name__ == '__main__':
   run()