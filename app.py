import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import plotly.colors as pcolors

st.set_page_config(layout="wide")

st.title("Co-lab notebook to Streamlit app!")

df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")

with st.expander("Press to view data frame"):
    st.write(df)


col1, col2 = st.columns(2)

with col2:
    st.write("""
## Histogram of Sales :moneybag:

Here is a standard histogram binning the number of sales by their amount.

The largest number of the sales are for amounts of $25 and below. Only a few
sales are larger than $10,000, and only one larger than $20,000.
        """)
    log = st.checkbox("Log the y-axis")

with col1:
    fig = px.histogram(df, x="Sales", log_y=log)
    st.plotly_chart(fig)


st.write("---")
col3,col4 = st.columns(2)

with col3:
    st.write("""
## Pie charts :pie:

Choose between `Region`, `Category`, `Segment` and `Ship Mode` to show the Qunatity
based on those features!
    """)
    feature = st.selectbox("Choose a Feature", ['Region','Category', 'Segment','Ship Mode'])

with col4:
    fig = px.pie(df, values='Quantity', names=feature, title='Quantity by {}'.format(feature))
    st.plotly_chart(fig)

st.write("---")
col5,col6 = st.columns(2)

with col6:
    st.write("""
## Scatter plot :game_die:

Choose between graphing `Sales` or `Profit` by `State` or `City`.
    """)
    location = st.radio("Choose a feature:",['State','City'])
    y_values = st.radio("Profit or Sales:", ['Sales','Profit'])

    if y_values == "Sales":
        color = pcolors.sequential.Plasma
    else:
        color = pcolors.sequential.RdBu

with col5:
    fig = go.Figure(data=go.Scatter(x=df[location],
                                    y=df[y_values],
                                    mode='markers',
                                    marker_color=df[y_values],
                                    marker_colorscale = color,
                                    text=df[location])) # hover text goes here

    fig.update_layout(title='{a} by USA {b}'.format(a=y_values,b=location))
    st.plotly_chart(fig)

st.write("---")
col7,col8 = st.columns(2)

with col7:
    st.write("""
## Tree map :palm_tree:

Default is set to:
- `Sales` for colour mapping and;
- `Region` and `State` for the path,
    """)
    path_opt = ["Region","State","Category", "Sub-Category", "Segment","Ship Mode"]
    path = st.multiselect("Select the options to compare", path_opt, default= ["Region","State"])
    color_opt = ["Sales","Profit","Discount"]
    color = st.selectbox("Select coloring:", color_opt)


with col8:
    fig = px.treemap(df, path=path, values="Quantity", hover_name=path[-1], color=color)
    st.plotly_chart(fig)
