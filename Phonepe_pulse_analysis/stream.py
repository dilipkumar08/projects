import streamlit as st
from streamlit_option_menu import option_menu
import phonepe

st.set_page_config(layout='wide')

db = phonepe.database()

with st.sidebar:
    option = option_menu('', options=['Home', 'Data Visualization', 'Analysis'], styles={'container': {'background-color': '#9933ff'}, 'icon': {'color': 'white'}, 'nav-link-selected': {'background-color': 'black'}})

if option == 'Home':
    st.title('Phonepe -:violet[Pulse Data Visualization and Exploration]')
    # if st.button('Reprocess data to database'):
    #     st.info('Please wait 😊, The process might take some time ⏲️')
    #     phonepe.phonepe_data().data_move()
    #     st.success('Data repoplated successfully ✅')
    
    st.subheader("General info :")
    logo_url = "D:/python/project/phonepe p/logo.png"  # Replace with the actual path or URL
    col1,col2=st.columns(2)
    with col1:
        st.image(logo_url,width=300,caption="PhonePe Logo")
    with col2:
        st.subheader('')
        st.subheader("Phonepe :violet[Digital Payments and Financial Services]")


    st.write("""
    :violet[PhonePe] is a leading digital payments and financial services company in India, founded in December 2015 and a subsidiary of Flipkart, owned by Walmart. 
    It provides a wide range of services including UPI-based payments, recharges, bill payments, and financial products.
    """)

    st.subheader(":violet[Key Features]")
    st.write("""
    - **UPI Payments**: Direct bank account transfers using UPI.
    - **Bill Payments and Recharges**: Pay utility bills and recharge mobile phones and DTH connections.
    - **Financial Services**:
        - Insurance: Health, travel, and car insurance.
        - Mutual Funds: Investment options.
        - Gold: Buy, sell, and store digital gold.
    - **Merchant Payments**: Payments to online and offline merchants via QR codes and UPI.
    - **Wallet Services**: Store money for quick payments.
    - **International Payments**: Includes remittance services.
    - **PhonePe Switch**: An in-app platform integrating various services like cab booking, food ordering, and shopping.
    """)

    st.subheader(":violet[How to Use PhonePe]")
    st.write("""
    1. **Download and Install**: Available on Android and iOS.
    2. **Registration**: Register with mobile number and link bank account using UPI.
    3. **Create UPI ID**: Set up UPI ID and PIN for transactions.
    4. **Transactions**: Send money, pay bills, and recharge directly from bank accounts.
    5. **Security**: Ensures secure transactions with encryption and UPI PINs.
    """)

    st.subheader(":violet[Popularity and Reach]")
    st.write("""
    PhonePe is a widely-used digital payment platform in India with millions of users and broad merchant acceptance, significantly contributing to India's cashless economy.
    """)

elif option == 'Data Visualization':
    tab1, tab2, tab3 = st.tabs(['Aggregate Data','Map Data','Top Data'])
    
    with tab1:
        method = st.radio('Select the Method', ['Aggregate Insurance', 'Aggregate Transaction', 'Aggregate User'])
        if method == 'Aggregate Insurance':
            col1,col2 =st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.agg_ins_df['year'].unique()), max_value=max(db.agg_ins_df['year'].unique()), key=f"agg_ins_{method}_year")
            with col2:
                quarter =st.slider('Select the quarter', min_value=min(db.agg_ins_df['quarter'].unique()), max_value=max(db.agg_ins_df['quarter'].unique()), key=f"agg_ins_{method}_quarter")
            if year==2020 and quarter==1:
                    st.info('The insurance feature is included in phonepe after year 2020 quarter 1. So, there won\'t be any data, Feel free to explore other data 😊.')
            else:
                fig1,fig2=db.ins_data_visualize(db.agg_ins_df,year,quarter)
                st.plotly_chart(fig1) 
                st.plotly_chart(fig2)

            
        elif method == 'Aggregate Transaction':
            col1,col2 =st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.agg_tran_df['year'].unique()), max_value=max(db.agg_tran_df['year'].unique()), key=f"agg_tran_{method}_year")
            with col2:
                quarter =st.slider('Select the quarter', min_value=min(db.agg_tran_df['quarter'].unique()), max_value=max(db.agg_tran_df['quarter'].unique()), key=f"agg_tran_{method}_quarter")
            fig1,fig2=db.tran_data_visualize(db.agg_tran_df, year,quarter)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)

        elif method == 'Aggregate User':
            col1,col2 =st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.agg_user_df['year'].unique()), max_value=max(db.agg_user_df['year'].unique()), key=f"agg_user_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.agg_user_df['quarter'].unique()), max_value=max(db.agg_user_df['quarter'].unique()), key=f"agg_user_{method}_quarter")
            if year==2022 and quarter>1:
                    st.info('The dataset format is changed to a new format from year 2022 quarter 2 by phonepe which affects the previous storage structure. So, I decided not to include it for now, Feel free to explore other data 😊.')
            else:
                fig1,fig2=db.agg_user_data_visualize(db.agg_user_df, year,quarter)
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)

    with tab2:
        method = st.radio('Select the Method', ['Map Insurance', 'Map Transaction', 'Map User'])
        if method == 'Map Insurance':
            col1,col2 =st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.map_ins_df['year'].unique()), max_value=max(db.map_ins_df['year'].unique()), key=f"map_ins_{method}_year")
            with col2:
                quarter=st.slider('Select the quarter', min_value=min(db.map_ins_df['quarter'].unique()), max_value=max(db.map_ins_df['quarter'].unique()), key=f"map_ins_{method}_quarter")
            if year==2020 and quarter==1:
                    st.info('The insurance feature is included in phonepe after year 2020 quarter 1. So, there won\'t be any data, Feel free to explore other data 😊.')
            else:
                fig1,fig2=db.ins_data_visualize(db.map_ins_df, year,quarter)
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)

        elif method == 'Map Transaction':
            col1,col2 =st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.map_tran_df['year'].unique()), max_value=max(db.map_tran_df['year'].unique()), key=f"map_tran_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.map_tran_df['quarter'].unique()), max_value=max(db.map_tran_df['quarter'].unique()), key=f"map_tran_{method}_quarter")
            
            fig1,fig2=db.tran_data_visualize(db.map_tran_df, year,quarter)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)

        elif method == 'Map User':
            col1,col2 =st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.map_user_df['year'].unique()), max_value=max(db.map_user_df['year'].unique()), key=f"map_user_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.map_user_df['quarter'].unique()), max_value=max(db.map_tran_df['quarter'].unique()), key=f"map_user_{method}_quarter")
           
            fig1,fig2=db.map_user_data_visualize(db.map_user_df, year,quarter)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)

    with tab3:
        method = st.radio('Select the Method', ['Top Insurance', 'Top Transaction', 'Top User'])
        
        
        if method == 'Top Insurance':
            st.subheader('District')
            col1,col2=st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.top_ins_district_df['year'].unique()), max_value=max(db.top_ins_district_df['year'].unique()), key=f"top_ins_district_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.top_ins_district_df['quarter'].unique()), max_value=max(db.top_ins_district_df['quarter'].unique()), key=f"top_ins_district_{method}_quarter")
            if year==2020 and quarter==1:
                    st.info('The insurance feature is included in phonepe after year 2020 quarter 1. So, there won\'t be any data, Feel free to explore other data 😊.')
            else:
                fig1,fig2=db.ins_data_visualize(db.top_ins_district_df, year,quarter)
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)
            st.subheader('Pincode')
            col1,col2=st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.top_ins_pincode_df['year'].unique()), max_value=max(db.top_ins_pincode_df['year'].unique()), key=f"top_ins_pincode_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.top_ins_pincode_df['quarter'].unique()), max_value=max(db.top_ins_pincode_df['quarter'].unique()), key=f"top_ins_pincode_{method}_quarter")
            if year==2020 and quarter==1:
                    st.info('The insurance feature is included in phonepe after year 2020 quarter 1. So, there won\'t be any data, Feel free to explore other data 😊.')
            else:
                fig1,fig2=db.ins_data_visualize(db.top_ins_pincode_df, year,quarter)
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)
        elif method == 'Top Transaction':
            st.subheader('District')
            col1,col2=st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.top_tran_district_df['year'].unique()), max_value=max(db.top_tran_district_df['year'].unique()), key=f"top_tran_district{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.top_tran_district_df['quarter'].unique()), max_value=max(db.top_tran_district_df['quarter'].unique()), key=f"top_tran_district{method}_quarter")

            
            fig1,fig2=db.tran_data_visualize(db.top_tran_district_df, year,quarter)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)  

            st.subheader('Pincode')
            col1,col2=st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.top_tran_pincode_df['year'].unique()), max_value=max(db.top_tran_pincode_df['year'].unique()), key=f"top_tran_pincode_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.top_tran_pincode_df['quarter'].unique()), max_value=max(db.top_tran_pincode_df['quarter'].unique()), key=f"top_tran_pincode_{method}_quarter")
            
            fig1,fig2=db.tran_data_visualize(db.top_tran_pincode_df, year,quarter)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)  
                      
        elif method == 'Top User':
            st.subheader('District')
            col1,col2=st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.top_user_district_df['year'].unique()), max_value=max(db.top_user_district_df['year'].unique()), key=f"top_user_district_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.top_user_district_df['quarter'].unique()), max_value=max(db.top_user_district_df['quarter'].unique()), key=f"top_user_district_{method}_quarter")

            st.plotly_chart(db.top_user_data_visualize(db.top_user_district_df, year,quarter))
            st.subheader('Pincode')
            col1,col2=st.columns(2)
            with col1:
                year = st.slider('Select the year', min_value=min(db.top_user_pincode_df['year'].unique()), max_value=max(db.top_user_pincode_df['year'].unique()), key=f"top_user_pincode_{method}_year")
            with col2:
                quarter = st.slider('Select the quarter', min_value=min(db.top_user_pincode_df['quarter'].unique()), max_value=max(db.top_user_pincode_df['quarter'].unique()), key=f"top_user_pincode_{method}_quarter")
            fig1,fig2=db.top_user_data_visualize(db.top_user_pincode_df, year,quarter)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)  
            


elif option == 'Analysis':
    tab1, tab2, tab3 = st.tabs(['Transaction Analysis','Insurance Analysis','User Analysis'])    
    with tab1:
        option=st.selectbox('data',options=['Top 10 Aggregate','Top 10 Map','Top 10 Top','Bottom 10 Aggregate','Bottom 10 Map','Bottom 10 Top'],key='transaction')
        if option=='Top 10 Aggregate':
            fig=db.top_ten_tran_data('Aggregate')
            st.plotly_chart(fig)
        elif option=='Top 10 Map':
            fig=db.top_ten_tran_data('Map')
            st.plotly_chart(fig)
        elif option=='Top 10 Top':
            fig=db.top_ten_tran_data('Top')
            st.plotly_chart(fig)
        elif option=='Bottom 10 Aggregate':
            fig=db.bottom_ten_tran_data('Aggregate')
            st.plotly_chart(fig)
        elif option=='Bottom 10 Map':
            fig=db.bottom_ten_tran_data('Map')
            st.plotly_chart(fig)
        elif option=='Bottom 10 Top':
            fig=db.bottom_ten_tran_data('Top')
            st.plotly_chart(fig)
    with tab2:
        option=st.selectbox('data',options=['Top 10 Aggregate','Top 10 Map','Top 10 Top','Bottom 10 Aggregate','Bottom 10 Map','Bottom 10 Top'],key='insurance')
        if option=='Top 10 Aggregate':
            fig1,fig2=db.top_ten_ins_data('Aggregate')
            st.plotly_chart(fig2)
            st.plotly_chart(fig1)
        elif option=='Top 10 Map':
            fig1,fig2=db.top_ins_ins_data('Map')
            st.plotly_chart(fig2)
            st.plotly_chart(fig1)
        elif option=='Top 10 Top':
            fig1,fig2=db.top_ten_ins_data('Top')
            st.plotly_chart(fig2)
            st.plotly_chart(fig1)
        elif option=='Bottom 10 Aggregate':
            fig1,fig2=db.bottom_ten_ins_data('Aggregate')
            st.plotly_chart(fig2)
            st.plotly_chart(fig1)
        elif option=='Bottom 10 Map':
            fig1,fig2=db.bottom_ten_ins_data('Map')
            st.plotly_chart(fig2)
            st.plotly_chart(fig1)
        elif option=='Bottom 10 Top':
            fig1,fig2=db.bottom_ten_ins_data('Top')
            st.plotly_chart(fig2)
            st.plotly_chart(fig1)

    with tab3:
        option=st.selectbox('data',options=['User Device Brand','App Open Count'])
        if option=='User Device Brand':
            fig=db.mobile_brand_user_data()
            st.plotly_chart(fig)
        elif option=='App Open Count':
            fig=db.open_count()
            st.plotly_chart(fig)
                

