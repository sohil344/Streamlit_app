import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

final_df=pd.read_csv('Indian.csv')
st.sidebar.title("India  Data Visualization")

list_of_states = list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')



df_prim=final_df[['Latitude','Longitude','District','Population','Households_with_Internet','Sex_Ratio','Literacy_ratte']]
df_para=final_df[['Population','Households_with_Internet','Sex_Ratio','Literacy_ratte']]
cols_para=df_para.columns

selected_state=st.sidebar.selectbox('Select a State',list_of_states)
primary=st.sidebar.selectbox('Select a Primary_Parameter',cols_para)
secondary=st.sidebar.selectbox('Select a Secondary_rate',cols_para)

plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent Primary Parameter')
    st.text('Color represent Secondary Parameter')

    if selected_state =='Overall India':

        fig=px.scatter_mapbox(df_prim,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=4,size_max=35,
                              mapbox_style='carto-positron',width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df= df_prim[df_prim['State']== selected_state]

        fig=px.scatter_mapbox(state_df,lon='Longitude',size=primary,color=secondary,zoom=4,size_max=35,
                              mapbox_style='carto-positron',width=1200,height=700)

        st.plotly_chart(fig,use_container_width=True)