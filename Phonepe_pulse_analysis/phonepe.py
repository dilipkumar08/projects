import os
import json
import pandas as pd 
import pymysql
import plotly.express as pltx



class database():

    def __init__(self):
        connector=pymysql.connect(host='localhost',user='root',password='mysql',database='phonepe')
        self.cursor=connector.cursor()
        file=open('D:/python/project/states_india.geojson','r')
        self.geo=json.load(file)

        self.cursor.execute('select* from agg_ins_data;')
        table=self.cursor.fetchall()
        self.agg_ins_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_ins_count', 'total_ins_amount', 'country','state', 'year', 'quarter'])
        

        self.cursor.execute('select* from agg_tran_data;')
        table=self.cursor.fetchall()
        self.agg_tran_df=pd.DataFrame(table,columns=['data', 'datatype', 'tran_type', 'total_tran_count','total_tran_amount', 'country', 'state', 'year', 'quarter'])
        

        self.cursor.execute('select* from agg_user_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.agg_user_df=pd.DataFrame(table,columns=['data', 'datatype', 'user_brand', 'total_user_count', 'percentage','country', 'state', 'year', 'quarter'])
        # print(agg_user_df)
        

        self.cursor.execute('select* from map_ins_data;')
        table=self.cursor.fetchall()
        #print(table)
        self.map_ins_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_ins_count', 'total_ins_amount', 'country','state', 'district', 'year', 'quarter'])
        #print(map_ins_df)
        

        self.cursor.execute('select* from map_tran_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.map_tran_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_tran_count', 'total_tran_amount', 'country','state', 'district', 'year', 'quarter'])
        # print(map_tran_df)
        

        
        self.cursor.execute('select* from map_user_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.map_user_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_reg_user_count', 'app_open_count', 'country','state', 'district', 'year', 'quarter'])
        # print(map_user_df)
        

        self.cursor.execute('select* from top_ins_district_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.top_ins_district_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_ins_count', 'total_ins_amount', 'country','state', 'district', 'year', 'quarter'])
        # print(top_ins_district_df)
        

        self.cursor.execute('select* from top_ins_pincode_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.top_ins_pincode_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_ins_count', 'total_ins_amount', 'country','state', 'pincode', 'year', 'quarter'])
        # print(top_ins_pincode_df)
        

        self.cursor.execute('select* from top_tran_district_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.top_tran_district_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_tran_count', 'total_tran_amount', 'country','state', 'district', 'year', 'quarter'])
        # print(top_tran_district_df)
        

        self.cursor.execute('select* from top_tran_pincode_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.top_tran_pincode_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_tran_count', 'total_tran_amount', 'country','state', 'pincode', 'year', 'quarter'])
        # print(top_tran_pincode_df)
        

        self.cursor.execute('select* from top_user_district_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.top_user_district_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_reg_user_count', 'country', 'state',
       'district', 'year', 'quarter'])
        # print(top_user_district_df)
        

        self.cursor.execute('select* from top_user_pincode_data;')
        table=self.cursor.fetchall()
        # print(table)
        self.top_user_pincode_df=pd.DataFrame(table,columns=['data', 'datatype', 'total_reg_user_count', 'country', 'state',
       'pincode', 'year', 'quarter'])
        # print(top_user_pincode_df)
        

    def tran_data_visualize(self,df,year,quarter):
        data=df[(df['year']==year) & (df['quarter']==quarter)]
        data.reset_index(drop=True,inplace=True)

        grouped_data=data.groupby('state')[['total_tran_count','total_tran_amount']].sum()
        grouped_data.reset_index(inplace=True)

        fig1=pltx.bar(grouped_data,x='state',y='total_tran_amount',title=f'{year} Quarter {quarter} Transaction Data ',
                    color_discrete_sequence=['#9933ff'],height=600,width=950)
        
        fig2=pltx.choropleth(grouped_data,locations='state',geojson=self.geo,scope='asia',fitbounds='locations',color_continuous_scale='purp',
        color='total_tran_amount',range_color=(grouped_data['total_tran_amount'].min(),grouped_data['total_tran_amount'].max()),height=1000,width=1000,
        featureidkey='properties.ST_NM')
        fig2.update_geos(visible=False,bgcolor='black')
        fig2.update_layout(title_text=f'Transaction Data {year}',title_font=dict(size=24, color='white'))
        return fig1,fig2
    

    def ins_data_visualize(self,df,year,quarter):
        
        data=df[(df['year']==year) & (df['quarter']==quarter)]
        data.reset_index(drop=True,inplace=True)
        
        grouped_data=data.groupby('state')[['total_ins_amount','total_ins_count']].sum()
        grouped_data.reset_index(inplace=True)

        fig1=pltx.bar(grouped_data,x='state',y='total_ins_amount',title=f'{year} Quarter {quarter} Insurance Data',
                    color_discrete_sequence= ['#9933ff'],height=600,width=950  )
        fig2=pltx.choropleth(grouped_data,locations='state',geojson=self.geo,scope='asia',fitbounds='locations',color_continuous_scale='purp',
        color='total_ins_amount',range_color=(grouped_data['total_ins_amount'].min(),grouped_data['total_ins_amount'].max()),height=1000,width=1000,
        featureidkey='properties.ST_NM')
        fig2.update_geos(visible=False,bgcolor='black')
        fig2.update_layout(title_text=f'Insurance Data {year}',title_font=dict(size=24, color='white'))
        return fig1,fig2


    def agg_user_data_visualize(self,df,year,quarter):
        df['total_user_count']=df['total_user_count'].astype('Int64')
        data=df[(df['year']==year) & (df['quarter']==quarter)]
        data.reset_index(drop=True,inplace=True)
        
        grouped_data=data.groupby('state')[['total_user_count','percentage']].sum()
        grouped_data.reset_index(inplace=True)

        fig1=pltx.bar(grouped_data,x='state',y='total_user_count',title=f'{year} Quarter {quarter} Aggregate Data',
                        color_discrete_sequence= ['#9933ff'],height=600,width=950)
                        
        
        data=df[(df['year']==year) & (df['quarter']==quarter)]
        data.reset_index(drop=True,inplace=True)    
        grouped_data=data.groupby('state')[['total_user_count','percentage']].sum()
        grouped_data.reset_index(inplace=True)
        fig2=pltx.choropleth(grouped_data,locations='state',geojson=self.geo,scope='asia',fitbounds='locations',color_continuous_scale='purp',
        color='total_user_count',range_color=(grouped_data['total_user_count'].min(),grouped_data['total_user_count'].max()),height=1000,width=1000,
        featureidkey='properties.ST_NM')
        fig2.update_geos(visible=False,bgcolor='black')
        fig2.update_layout(title_text=f'Aggregate Data {year}',title_font=dict(size=24, color='white'))
        return fig1,fig2
    
    def map_user_data_visualize(self,df,year,quarter):
        
        df['total_reg_user_count']=df['total_reg_user_count'].astype('Int64')
        data=df[(df['year']==year) & (df['quarter']==quarter)]
        data.reset_index(drop=True,inplace=True)    
        grouped_data=df.groupby('state')[['total_reg_user_count']].sum()
        grouped_data.reset_index(inplace=True)

        fig1=pltx.bar(grouped_data,x='state',y='total_reg_user_count',title=f'{year} Quarter {quarter} Map Data',color_discrete_sequence= ['#9933ff'],height=600,width=950)

        fig2=pltx.choropleth(grouped_data,locations='state',geojson=self.geo,scope='asia',fitbounds='locations',color_continuous_scale='purp',
        color='total_reg_user_count',range_color=(grouped_data['total_reg_user_count'].min(),grouped_data['total_reg_user_count'].max()),height=1000,width=1000,
        featureidkey='properties.ST_NM')
        fig2.update_geos(visible=False,bgcolor='black')
        fig2.update_layout(title_text=f'Map User Data {year}',title_font=dict(size=24, color='white'))
        return fig1,fig2
    
    def top_user_data_visualize(self,df,year,quarter):
        df=self.top_user_district_df
        data=df[(df['year']==year) & (df['quarter']==quarter)]
        data.reset_index(drop=True,inplace=True)

        grouped_data=data.groupby('state')[['total_reg_user_count']].sum()
        grouped_data.reset_index(inplace=True)

        fig1=pltx.bar(grouped_data,x='state',y='total_reg_user_count',title=f'{year} Quarter {quarter} Top Data',color_discrete_sequence= ['#9933ff'],height=650,width=950)

        fig2=pltx.choropleth(grouped_data,locations='state',geojson=self.geo,scope='asia',fitbounds='locations',color_continuous_scale='purp',
        color='total_reg_user_count',range_color=(grouped_data['total_reg_user_count'].min(),grouped_data['total_reg_user_count'].max()),height=650,width=1000,
        featureidkey='properties.ST_NM')
        fig2.update_geos(visible=False,bgcolor='black')
        fig2.update_layout(title_text=f'Top user Data {year}',title_font=dict(size=24, color='white'))
        return fig1,fig2
    
    def top_ten_tran_data(self,option):
        if option=='Aggregate':
            query='select atd_state,sum(atd_tran_amt) from agg_tran_data group by atd_state order by sum(atd_tran_amt) asc limit 10;'
        elif option=='Map':
            query='select mtd_state,sum(mtd_tran_amt) from map_tran_data group by mtd_state order by sum(mtd_tran_amt) asc limit 10;'
        elif option=='Top':
            query='select ttdd_state,sum(ttdd_tran_amt) from top_tran_district_data group by ttdd_state order by sum(ttdd_tran_amt) asc limit 10;'

        self.cursor.execute(query)
        table=self.cursor.fetchall()
        df=pd.DataFrame(table,columns=['state','total amount'])
        fig=pltx.bar(df,x='state',y='total amount',title=f'Top ten states based on {option} Transaction amount data',color_discrete_sequence= ['#9933ff'],height=650,width=950)
        return fig
    
    def bottom_ten_tran_data(self,option):
        if option=='Aggregate':
            query='select atd_state,sum(atd_tran_amt) from agg_tran_data group by atd_state order by sum(atd_tran_amt) desc limit 10;'
        elif option=='Map':
            query='select mtd_state,sum(mtd_tran_amt) from map_tran_data group by mtd_state order by sum(mtd_tran_amt) desc limit 10;'
        elif option=='Top':
            query='select ttdd_state,sum(ttdd_tran_amt) from top_tran_district_data group by ttdd_state order by sum(ttdd_tran_amt)  desc limit 10;'

        self.cursor.execute(query)
        table=self.cursor.fetchall()
        df=pd.DataFrame(table,columns=['state','total amount'])
        fig=pltx.bar(df,x='state',y='total amount',title=f'Bottom ten states based on {option} Transaction amount data',color_discrete_sequence= ['#9933ff'],height=650,width=950)
        return fig
        
        
    def top_ten_ins_data(self,option):
        if option=='Aggregate':
            amt_query='select aid_state,sum(aid_ins_amt) from agg_ins_data group by aid_state order by sum(aid_ins_amt) desc limit 10;'
            cnt_query='select aid_state,sum(aid_ins_cnt) from agg_ins_data group by aid_state order by sum(aid_ins_cnt) desc limit 10;'
        elif option=='Map':
            amt_query='select mid_state,sum(mid_ins_amt) from map_ins_data group by mid_state order by sum(mid_ins_amt) desc limit 10;'
            cnt_query='select mid_state,sum(mid_ins_cnt) from map_ins_data group by mid_state order by sum(mid_ins_cnt) desc limit 10;'
        elif option=='Top':
            amt_query='select tidd_state,sum(tidd_ins_amt) from top_ins_district_data group by tidd_state order by sum(tidd_ins_amt) desc limit 10 ;'
            cnt_query='select tidd_state,sum(tidd_ins_cnt) from top_ins_district_data group by tidd_state order by sum(tidd_ins_cnt) desc limit 10 ;'

        self.cursor.execute(amt_query)
        table1=self.cursor.fetchall()
        df1=pd.DataFrame(table1,columns=['state','total amount'])
        fig1=pltx.bar(df1,x='state',y='total amount',title=f'Top ten states based on {option} Insurance amount data',color_discrete_sequence= ['#9933ff'],height=650,width=950)
        
        self.cursor.execute(cnt_query)
        table2=self.cursor.fetchall()
        df2=pd.DataFrame(table2,columns=['state','total count'])
        fig2=pltx.bar(df2,x='state',y='total count',title=f'Top ten states based on {option} Insurance count data',color_discrete_sequence= ['#9933ff'],height=650,width=950)


        return fig1,fig2
    
    def bottom_ten_ins_data(self,option):
        if option=='Aggregate':
            amt_query='select aid_state,sum(aid_ins_amt) from agg_ins_data group by state order by sum(aid_ins_amt) asc limit 10;'
            cnt_query='select aid_state,sum(aid_ins_cnt) from agg_ins_data group by state order by sum(aid_ins_cnt) asc limit 10;'
        elif option=='Map':
            amt_query='select mid_state,sum(mid_ins_amt) from map_ins_data group by mid_state order by sum(mid_ins_amt) asc limit 10;'
            cnt_query='select mid_state,sum(mid_ins_cnt) from map_ins_data group by mid_state order by sum(mid_ins_cnt) asc limit 10;'
        elif option=='Top':
            amt_query='select tidd_state,sum(tidd_ins_amt) from top_ins_district_data group by tidd_state order by sum(tidd_ins_amt) asc limit 10 ;'
            cnt_query='select tidd_state,sum(tidd_ins_cnt) from top_ins_district_data group by tidd_state order by sum(tidd_ins_cnt) asc limit 10 ;'

        self.cursor.execute(amt_query)
        table1=self.cursor.fetchall()
        df1=pd.DataFrame(table1,columns=['state','total amount'])
        fig1=pltx.bar(df1,x='state',y='total amount',title=f'Bottom ten states based on {option} Insurance amount data',color_discrete_sequence= ['#9933ff'],height=650,width=950)
        
        self.cursor.execute(cnt_query)
        table2=self.cursor.fetchall()
        df2=pd.DataFrame(table2,columns=['state','total count'])
        fig2=pltx.bar(df2,x='state',y='total count',title=f'Bottom ten states based on {option} Insurance count data',color_discrete_sequence= ['#9933ff'],height=650,width=950)
        
        return fig1,fig2


    def mobile_brand_user_data(self):
        query=('select aud_user_brand,sum(aud_user_cnt) from agg_user_data group by aud_user_brand order by sum(aud_user_cnt) desc;')
        self.cursor.execute(query)
        table=self.cursor.fetchall()
        df=pd.DataFrame(table,columns=['Brand','user count'])
        fig=pltx.bar(df,x='Brand',y='user count',title=f'Aggregate user device brand data',color_discrete_sequence=['#9933ff'],height=650,width=950)
        
        return fig
    
    def open_count(self):
        query=('select mud_state,sum(mud_appopen_cnt) from map_user_data group by mud_state order by sum(mud_appopen_cnt) desc;')
        self.cursor.execute(query)
        table=self.cursor.fetchall()
        df=pd.DataFrame(table,columns=['state','open count'])
        fig=pltx.bar(df,x='state',y='open count',title=f'Map user app open data',color_discrete_sequence=['#9933ff'],height=650,width=950)
        return fig
    
        
        
    




class phonepe_data():

    def __init__(self):
        connector=pymysql.connect(host='localhost',user='root',password='mysql',database='phonepe')
        self.cursor=connector.cursor()

    def data_move(self):
        agg_insurance_path=('D:/python/project/phonepe p/pulse/data/aggregated/insurance/country/india/state/')

        country='India'
        datatype='insurance'
        data='aggregated'
        agg_insurance_data={'data':[],'datatype':[],'total_ins_count':[],'total_ins_amount':[],'country':[],'state':[],'year':[],'quarter':[]}
        state_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/aggregated/insurance/country/india/state')

        for state in state_list:
            cur_year_path=agg_insurance_path+state
            year_list=os.listdir(cur_year_path)
            for year in year_list:
                cur_file_path=cur_year_path+'/'+year  
                file_list=os.listdir(cur_file_path)
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)
                    
                    for items in temp['data']['transactionData']:
                        agg_insurance_data['data'].append(data)
                        agg_insurance_data['datatype'].append(datatype)
                        agg_insurance_data['total_ins_count'].append(items['paymentInstruments'][0]['count'])
                        agg_insurance_data['total_ins_amount'].append(items['paymentInstruments'][0]['amount'])
                        agg_insurance_data['country'].append(country)
                        agg_insurance_data['state'].append(state)
                        agg_insurance_data['year'].append(year)
                        agg_insurance_data['quarter'].append(int(file.strip('.json')))
                        
        agg_ins_df=pd.DataFrame(agg_insurance_data)

        agg_ins_df['state']=agg_ins_df['state'].str.replace('-',' ')
        agg_ins_df['state']=agg_ins_df['state'].str.title()
        agg_ins_df['state']=agg_ins_df['state'].str.replace('&','and')


        self.agg_ins_df=agg_ins_df

        #cursor.execute('Drop table agg_ins_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS agg_ins_data (aid_data varchar(30),aid_datatype varchar(20),aid_ins_cnt int,aid_ins_amt float,aid_country varchar(10),aid_state varchar(100),aid_year int,aid_quarter int);')
        insert='INSERT INTO agg_ins_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE agg_ins_data')
        m,n=agg_ins_df.shape
        for i in range(m):
            values=[agg_ins_df['data'][i],agg_ins_df['datatype'][i],agg_ins_df['total_ins_count'][i],agg_ins_df['total_ins_amount'][i],
                    agg_ins_df['country'][i],agg_ins_df['state'][i],agg_ins_df['year'][i],agg_ins_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')
        


        agg_transaction_path=('D:/python/project/phonepe p/pulse/data/aggregated/transaction/country/india/state/')

        country='India'
        datatype='transaction'
        data='aggregated'
        agg_transaction_data={'data':[],'datatype':[],'tran_type':[],'total_tran_count':[],'total_tran_amount':[],'country':[],'state':[],'year':[],'quarter':[]}
        state_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/aggregated/transaction/country/india/state')

        for state in state_list:
            cur_year_path=agg_transaction_path+state+'/'
            year_list=os.listdir(cur_year_path)
            for year in year_list:
                cur_file_path=cur_year_path+year+'/'  
                file_list=os.listdir(cur_file_path)
                for file in file_list:
                    cur_file= cur_file_path+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)

                    for items in temp['data']['transactionData']:
                        agg_transaction_data['data'].append(data)
                        agg_transaction_data['datatype'].append(datatype)
                        agg_transaction_data['tran_type'].append(items['name'])
                        agg_transaction_data['total_tran_count'].append(items['paymentInstruments'][0]['count'])
                        agg_transaction_data['total_tran_amount'].append(items['paymentInstruments'][0]['amount'])
                        agg_transaction_data['country'].append(country)
                        agg_transaction_data['state'].append(state)
                        agg_transaction_data['year'].append(year)
                        agg_transaction_data['quarter'].append(int(file.strip('.json')))
                        
            agg_tran_df=pd.DataFrame(agg_transaction_data)

            agg_tran_df['state']=agg_tran_df['state'].str.replace('-',' ')
            agg_tran_df['state']=agg_tran_df['state'].str.title()
            agg_tran_df['state']=agg_tran_df['state'].str.replace('&','and')

            self.agg_tran_df=agg_tran_df

            #cursor.execute('drop table agg_tran_data;')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS agg_tran_data (atd_data varchar(30),atd_datatype varchar(20),atd_tran_typ varchar(30),atd_tran_cnt int,atd_tran_amt float,atd_country varchar(10),atd_state varchar(100),atd_year int,atd_quarter int);')  
            insert='INSERT INTO agg_tran_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            self.cursor.execute('TRUNCATE TABLE agg_tran_data')
            m,n=agg_tran_df.shape

            for i in range(m):
                values=[agg_tran_df['data'][i],agg_tran_df['datatype'][i],agg_tran_df['tran_type'][i],agg_tran_df['total_tran_count'][i],
                        agg_tran_df['total_tran_amount'][i],
                        agg_tran_df['country'][i],agg_tran_df['state'][i],agg_tran_df['year'][i],agg_tran_df['quarter'][i]]
                self.cursor.execute(insert,values)
            self.cursor.execute('COMMIT;')



            agg_user_path=('D:/python/project/phonepe p/pulse/data/aggregated/user/country/india/state/')

        country='India'
        datatype='user'
        data='aggregate'
        agg_user_data={'data':[],'datatype':[],'user_brand':[],'total_user_count':[],'percentage':[],'country':[],'state':[],'year':[],'quarter':[]}
        state_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/aggregated/user/country/india/state')

        for state in state_list:
            cur_year_path=agg_user_path+state
            year_list=os.listdir(cur_year_path)

            for year in year_list:
                cur_file_path=cur_year_path+'/'+year
                file_list=os.listdir(cur_file_path)
            
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)
                
                    try:

                        for items in temp['data']['usersByDevice']:
                            agg_user_data['data'].append(data)
                            agg_user_data['datatype'].append(datatype)
                            agg_user_data['user_brand'].append(items['brand'])
                            agg_user_data['total_user_count'].append(items['count'])
                            agg_user_data['percentage'].append(items['percentage'])
                            agg_user_data['country'].append(country)
                            agg_user_data['state'].append(state)
                            agg_user_data['year'].append(year)
                            agg_user_data['quarter'].append(int(file.strip('.json')))

                    except:
                
                        pass
                        
        agg_user_df=pd.DataFrame(agg_user_data)

        agg_user_df['state']=agg_user_df['state'].str.replace('-',' ')
        agg_user_df['state']=agg_user_df['state'].str.title()
        agg_user_df['state']=agg_user_df['state'].str.replace('&','and')

        self.agg_user_df=agg_user_df

        #cursor.execute('drop table agg_user_data;')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS agg_user_data (aud_data varchar(30),aud_datatype varchar(20),aud_user_brand varchar(30),aud_user_cnt int,aud_percentage float,aud_country varchar(10),aud_state varchar(100),aud_year int,aud_quarter int);')  
        insert='INSERT INTO agg_user_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE agg_user_data')
        m,n=agg_user_df.shape
        for i in range(m):
            values=[agg_user_df['data'][i],agg_user_df['datatype'][i],agg_user_df['user_brand'][i],agg_user_df['total_user_count'][i],
                    agg_user_df['percentage'][i],agg_user_df['country'][i],agg_user_df['state'][i],agg_user_df['year'][i],agg_user_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')



        map_insur_hover_path=('D:/python/project/phonepe p/pulse/data/map/insurance/hover/country/india/state/')

        country='India'
        datatype='insurance'
        data='map'
        map_insurance_data={'data':[],'datatype':[],'total_ins_count':[],'total_ins_amount':[],'country':[],'state':[],'district':[],'year':[],'quarter':[]}
        year_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/map/insurance/hover/country/india/state')

        for state in state_list:
            cur_year_path=map_insur_hover_path+state
            year_list=os.listdir(cur_year_path)

            for year in year_list:
                cur_file_path=cur_year_path+'/'+year
                file_list=os.listdir(cur_file_path)
            
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)

                        
                    for items in temp['data']['hoverDataList']:
            
                        map_insurance_data['data'].append(data)
                        map_insurance_data['datatype'].append(datatype)
                        map_insurance_data['total_ins_count'].append(items['metric'][0]['count'])
                        map_insurance_data['total_ins_amount'].append(items['metric'][0]['amount']) 
                        map_insurance_data['country'].append(country)
                        map_insurance_data['state'].append(state)
                        map_insurance_data['district'].append(items['name'])
                        map_insurance_data['year'].append(year)
                        map_insurance_data['quarter'].append(int(file.strip('.json')))


        map_ins_df=pd.DataFrame(map_insurance_data )

        map_ins_df['state']=map_ins_df['state'].str.replace('-',' ')
        map_ins_df['state']=map_ins_df['state'].str.title()
        map_ins_df['state']=map_ins_df['state'].str.replace('&','and')

        map_ins_df['district']=map_ins_df['district'].str.replace('-',' ')
        map_ins_df['district']=map_ins_df['district'].str.title()
        map_ins_df['district']=map_ins_df['district'].str.replace('&','and')
        map_ins_df['district']=map_ins_df['district'].str.replace(' And ',' and ')

        self.map_ins_df=map_ins_df
        


        #cursor.execute('Drop table map_ins_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS map_ins_data (mid_data varchar(30),mid_datatype varchar(20),mid_ins_cnt int,mid_ins_amt float,mid_country varchar(10),mid_state varchar(100),mid_district varchar(100),mid_year int,mid_quarter int);')
        insert='INSERT INTO map_ins_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE map_ins_data')
        m,n=map_ins_df.shape
        for i in range(m):
            values=[map_ins_df['data'][i],map_ins_df['datatype'][i],map_ins_df['total_ins_count'][i],map_ins_df['total_ins_amount'][i],
                    map_ins_df['country'][i],map_ins_df['state'][i],map_ins_df['district'][i],map_ins_df['year'][i],map_ins_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')



        map_tran_hover_path=('D:/python/project/phonepe p/pulse/data/map/transaction/hover/country/india/state/')

        country='India'
        datatype='transaction'
        data='map'
        map_transaction_data={'data':[],'datatype':[],'total_tran_count':[],'total_tran_amount':[],'country':[],'state':[],'district':[],'year':[],'quarter':[]}
        year_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/map/transaction/hover/country/india/state')

        for state in state_list:
            cur_year_path=map_tran_hover_path+state
            year_list=os.listdir(cur_year_path)
            for year in year_list:
                cur_file_path=cur_year_path+'/'+year
                file_list=os.listdir(cur_file_path)
            
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)
                            
                    for items in temp['data']['hoverDataList']:
                        map_transaction_data['data'].append(data)
                        map_transaction_data['datatype'].append(datatype)
                        map_transaction_data['total_tran_count'].append(items['metric'][0]['count'])
                        map_transaction_data['total_tran_amount'].append(items['metric'][0]['amount']) 
                        map_transaction_data['country'].append(country)
                        map_transaction_data['state'].append(state)
                        map_transaction_data['district'].append(items['name'])
                        map_transaction_data['year'].append(year)
                        map_transaction_data['quarter'].append(int(file.strip('.json')))


        map_tran_df=pd.DataFrame(map_transaction_data)
        #print(map_tran_df['state'].unique())
        map_tran_df['state']=map_tran_df['state'].str.replace('-',' ')
        map_tran_df['state']=map_tran_df['state'].str.title()
        map_tran_df['state']=map_tran_df['state'].str.replace('&','and')
        # print(map_tran_df['state'].unique())
        # print(map_tran_df['district'].unique())
        map_tran_df['district']=map_tran_df['district'].str.replace('-',' ')
        map_tran_df['district']=map_tran_df['district'].str.title()
        map_tran_df['district']=map_tran_df['district'].str.replace('&','and')
        map_tran_df['district']=map_tran_df['district'].str.replace(' And ',' and ')
        # print(map_tran_df['district'].unique())

        self.map_tran_df=map_tran_df

        #cursor.execute('drop table map_tran_data;')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS map_tran_data (mtd_data varchar(30),mtd_datatype varchar(20),mtd_tran_cnt int,mtd_tran_amt float,mtd_country varchar(10),mtd_state varchar(100),mtd_district varchar(100),mtd_year int,mtd_quarter int);')  
        insert='INSERT INTO map_tran_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE map_tran_data')
        m,n=map_tran_df.shape
        for i in range(m):
            values=[map_tran_df['data'][i],map_tran_df['datatype'][i],map_tran_df['total_tran_count'][i],
                    map_tran_df['total_tran_amount'][i],
                    map_tran_df['country'][i],map_tran_df['state'][i],map_tran_df['district'][i],map_tran_df['year'][i],map_tran_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')




        map_tran_hover_path=('D:/python/project/phonepe p/pulse/data/map/user/hover/country/india/state/')

        country='India'
        datatype='user'
        data='map'
        map_user_data={'data':[],'datatype':[],'total_reg_user_count':[],'app_open_count':[],'country':[],'state':[],'district':[],'year':[],'quarter':[]}
        year_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/map/user/hover/country/india/state')

        for state in state_list:
            cur_year_path=map_tran_hover_path+'/'+state
            year_list=os.listdir(cur_year_path)

            for year in year_list:
                cur_file_path=cur_year_path+'/'+year  
                file_list=os.listdir(cur_file_path)
        
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)
                
                    for items in temp['data']['hoverData'].items():
                        map_user_data['data'].append(data)
                        map_user_data['datatype'].append(datatype)
                        map_user_data['total_reg_user_count'].append(items[1]['registeredUsers'])
                        map_user_data['app_open_count'].append(items[1]['appOpens']) 
                        map_user_data['country'].append(country)
                        map_user_data['state'].append(state)
                        map_user_data['district'].append(items[0])
                        map_user_data['year'].append(year)
                        map_user_data['quarter'].append(int(file.strip('.json')))


        map_user_df=pd.DataFrame(map_user_data)

        # print(map_user_df['state'].unique())
        map_user_df['state']=map_user_df['state'].str.replace('-',' ')
        map_user_df['state']=map_user_df['state'].str.title()
        map_user_df['state']=map_user_df['state'].str.replace('&','and')
        # print(map_user_df['state'].unique())
        # print(map_user_df['district'].unique())
        map_user_df['district']=map_user_df['district'].str.replace('-',' ')
        map_user_df['district']=map_user_df['district'].str.title()
        map_user_df['district']=map_user_df['district'].str.replace('&','and')
        map_user_df['district']=map_user_df['district'].str.replace(' And ',' and ')
        # print(map_user_df['district'].unique())

        self.map_user_df=map_user_df

        #cursor.execute('drop table map_user_data;')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS map_user_data (mud_data varchar(30),mud_datatype varchar(20),mud_reg_user_cnt varchar(30),mud_appopen_cnt int,mud_country varchar(10),mud_state varchar(100),mud_district varchar(100),mud_year int,aud_quarter int);')  
        insert='INSERT INTO map_user_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE map_user_data')
        m,n=map_user_df.shape
        for i in range(m):
            values=[map_user_df['data'][i],map_user_df['datatype'][i],map_user_df['total_reg_user_count'][i],map_user_df['app_open_count'][i],
                    map_user_df['country'][i],
                    map_user_df['state'][i],map_user_df['district'][i],map_user_df['year'][i],map_user_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')



        top_ins_path=('D:/python/project/phonepe p/pulse/data/top/insurance/country/india/state/')

        country='India'
        datatype='insurance'
        data='top'
        top_insurance_district_data={'data':[],'datatype':[],'total_ins_count':[],'total_ins_amount':[],'country':[],'state':[],'district':[],'year':[],'quarter':[]}
        top_insurance_pincode_data={'data':[],'datatype':[],'total_ins_count':[],'total_ins_amount':[],'country':[],'state':[],'pincode':[],'year':[],'quarter':[]}

        year_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/top/insurance/country/india/state')     

        for state in state_list:
            cur_year_path=top_ins_path+state
            year_list=os.listdir(cur_year_path)

            for year in year_list:
                cur_file_path=cur_year_path+'/'+year
                file_list=os.listdir(cur_file_path)
        
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)

                                
                    for items in temp['data']['districts']:
            
                        top_insurance_district_data['data'].append(data)
                        top_insurance_district_data['datatype'].append(datatype)
                        top_insurance_district_data['total_ins_count'].append(items['metric']['count'])
                        top_insurance_district_data['total_ins_amount'].append(items['metric']['amount']) 
                        top_insurance_district_data['country'].append(country)
                        top_insurance_district_data['state'].append(state)
                        top_insurance_district_data['district'].append(items['entityName'])
                        top_insurance_district_data['year'].append(year)
                        top_insurance_district_data['quarter'].append(int(file.strip('.json')))
                    
                    for items in temp['data']['pincodes']:
            
                        top_insurance_pincode_data['data'].append(data)
                        top_insurance_pincode_data['datatype'].append(datatype)
                        top_insurance_pincode_data['total_ins_count'].append(items['metric']['count'])
                        top_insurance_pincode_data['total_ins_amount'].append(items['metric']['amount']) 
                        top_insurance_pincode_data['country'].append(country)
                        top_insurance_pincode_data['state'].append(state)
                        top_insurance_pincode_data['pincode'].append(items['entityName'])
                        top_insurance_pincode_data['year'].append(year)
                        top_insurance_pincode_data['quarter'].append(int(file.strip('.json')))


        top_ins_district_df=pd.DataFrame(top_insurance_district_data)
        top_ins_pincode_df=pd.DataFrame(top_insurance_pincode_data)

        # print(top_ins_district_df['state'].unique())
        top_ins_district_df['state']=top_ins_district_df['state'].str.replace('-',' ')
        top_ins_district_df['state']=top_ins_district_df['state'].str.title()
        top_ins_district_df['state']=top_ins_district_df['state'].str.replace('&','and')
        # print(top_ins_district_df['state'].unique())
        # print(top_ins_district_df['district'].unique())
        top_ins_district_df['district']=top_ins_district_df['district'].str.replace('-',' ')
        top_ins_district_df['district']=top_ins_district_df['district'].str.title()
        top_ins_district_df['district']=top_ins_district_df['district'].str.replace('&','and')
        top_ins_district_df['district']=top_ins_district_df['district'].str.replace(' And ',' and ')

        self.top_ins_district_df=top_ins_district_df

        # print(top_ins_pincode_df['state'].unique())
        top_ins_pincode_df['state']=top_ins_pincode_df['state'].str.replace('-',' ')
        top_ins_pincode_df['state']=top_ins_pincode_df['state'].str.title()
        top_ins_pincode_df['state']=top_ins_pincode_df['state'].str.replace('&','and')
        # print(top_ins_pincode_df['state'].unique())

        self.top_ins_pincode_df=top_ins_pincode_df

        #cursor.execute('Drop table top_ins_district_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS top_ins_district_data (tidd_data varchar(30),tidd_datatype varchar(20),tidd_ins_cnt int,tidd_ins_amt float,tidd_country varchar(10),tidd_state varchar(100),tidd_district varchar(100),tidd_year int,tidd_quarter int);')
        insert='INSERT INTO top_ins_district_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE top_ins_district_data')
        m,n=top_ins_district_df.shape
        for i in range(m):
            values=[top_ins_district_df['data'][i],top_ins_district_df['datatype'][i],top_ins_district_df['total_ins_count'][i],top_ins_district_df['total_ins_amount'][i],
                    top_ins_district_df['country'][i],top_ins_district_df['state'][i],top_ins_district_df['district'][i],top_ins_district_df['year'][i],top_ins_district_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')

        #cursor.execute('Drop table top_ins_pincode_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS top_ins_pincode_data (tipd_data varchar(30),tipd_datatype varchar(20),tipd_ins_cnt int,tipd_ins_amt float,tipd_country varchar(10),tipd_state varchar(100),tipd_pincode varchar(100),tipd_year int,tipd_quarter int);')
        insert='INSERT INTO top_ins_pincode_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE top_ins_pincode_data')
        m,n=top_ins_pincode_df.shape
        for i in range(m):
            values=[top_ins_pincode_df['data'][i],top_ins_pincode_df['datatype'][i],top_ins_pincode_df['total_ins_count'][i],top_ins_pincode_df['total_ins_amount'][i],
                    top_ins_pincode_df['country'][i],top_ins_pincode_df['state'][i],top_ins_pincode_df['pincode'][i],top_ins_pincode_df['year'][i],top_ins_pincode_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')




        top_tran_path=('D:/python/project/phonepe p/pulse/data/top/transaction/country/india/state/')

        country='India'
        datatype='transaction'
        data='top'
        top_transaction_district_data={'data':[],'datatype':[],'total_tran_count':[],'total_tran_amount':[],'country':[],'state':[],'district':[],'year':[],'quarter':[]}
        top_transaction_pincode_data={'data':[],'datatype':[],'total_tran_count':[],'total_tran_amount':[],'country':[],'state':[],'pincode':[],'year':[],'quarter':[]}
        year_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/top/transaction/country/india/state')

        for state in state_list:
            cur_year_path=top_tran_path+state
            year_list=os.listdir(cur_year_path)

            for year in year_list:
                cur_file_path=cur_year_path+'/'+year
                file_list=os.listdir(cur_file_path)
        
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)                       
                    for items in temp['data']['districts']:
            
                        top_transaction_district_data['data'].append(data)
                        top_transaction_district_data['datatype'].append(datatype)
                        top_transaction_district_data['total_tran_count'].append(items['metric']['count'])
                        top_transaction_district_data['total_tran_amount'].append(items['metric']['amount']) 
                        top_transaction_district_data['country'].append(country)
                        top_transaction_district_data['state'].append(state)
                        top_transaction_district_data['district'].append(items['entityName'])
                        top_transaction_district_data['year'].append(year)
                        top_transaction_district_data['quarter'].append(int(file.strip('.json')))
                    
                    for items in temp['data']['pincodes']:
            
                        top_transaction_pincode_data['data'].append(data)
                        top_transaction_pincode_data['datatype'].append(datatype)
                        top_transaction_pincode_data['total_tran_count'].append(items['metric']['count'])
                        top_transaction_pincode_data['total_tran_amount'].append(items['metric']['amount']) 
                        top_transaction_pincode_data['country'].append(country)
                        top_transaction_pincode_data['state'].append(state)
                        top_transaction_pincode_data['pincode'].append(items['entityName'])
                        top_transaction_pincode_data['year'].append(year)
                        top_transaction_pincode_data['quarter'].append(int(file.strip('.json')))


        top_tran_district_df=pd.DataFrame(top_transaction_district_data)
        top_tran_pincode_df=pd.DataFrame(top_transaction_pincode_data)


        # print(top_tran_district_df['state'].unique())
        top_tran_district_df['state']=top_tran_district_df['state'].str.replace('-',' ')
        top_tran_district_df['state']=top_tran_district_df['state'].str.title()
        top_tran_district_df['state']=top_tran_district_df['state'].str.replace('&','and')
        # print(top_tran_district_df['state'].unique())
        # print(top_tran_district_df['district'].unique())
        top_tran_district_df['district']=top_tran_district_df['district'].str.replace('-',' ')
        top_tran_district_df['district']=top_tran_district_df['district'].str.title()
        top_tran_district_df['district']=top_tran_district_df['district'].str.replace('&','and')
        top_tran_district_df['district']=top_tran_district_df['district'].str.replace(' And ',' and ')

        self.top_tran_district_df=top_tran_district_df

        # print(top_tran_pincode_df['state'].unique())
        top_tran_pincode_df['state']=top_tran_pincode_df['state'].str.replace('-',' ')
        top_tran_pincode_df['state']=top_tran_pincode_df['state'].str.title()
        top_tran_pincode_df['state']=top_tran_pincode_df['state'].str.replace('&','and')
        # print(top_tran_pincode_df['state'].unique())

        self.top_tran_pincode_df=top_tran_pincode_df

        #cursor.execute('Drop table top_tran_district_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS top_tran_district_data (ttdd_data varchar(30),ttdd_datatype varchar(20),ttdd_tran_cnt int,ttdd_tran_amt float,ttdd_country varchar(10),ttdd_state varchar(100),ttdd_district varchar(100),ttdd_year int,ttdd_quarter int);')
        insert='INSERT INTO top_tran_district_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE top_tran_district_data')
        m,n=top_tran_district_df.shape
        for i in range(m):
            values=[top_tran_district_df['data'][i],top_tran_district_df['datatype'][i],top_tran_district_df['total_tran_count'][i],top_tran_district_df['total_tran_amount'][i],
                    top_tran_district_df['country'][i],top_tran_district_df['state'][i],top_tran_district_df['district'][i],top_tran_district_df['year'][i],top_tran_district_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')

        #cursor.execute('Drop table top_tran_pincode_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS top_tran_pincode_data (ttpd_data varchar(30),ttpd_datatype varchar(20),ttpd_tran_cnt int,ttpd_tran_amt float,ttpd_country varchar(10),ttpd_state varchar(100),ttpd_pincode varchar(100),ttpd_year int,ttpd_quarter int);')
        insert='INSERT INTO top_tran_pincode_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE top_tran_pincode_data')
        m,n=top_tran_pincode_df.shape
        for i in range(m):
            values=[top_tran_pincode_df['data'][i],top_tran_pincode_df['datatype'][i],top_tran_pincode_df['total_tran_count'][i],top_tran_pincode_df['total_tran_amount'][i],
                    top_tran_pincode_df['country'][i],top_tran_pincode_df['state'][i],top_tran_pincode_df['pincode'][i],top_tran_pincode_df['year'][i],top_tran_pincode_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')



        top_tran_path=('D:/python/project/phonepe p/pulse/data/top/user/country/india/state/')

        country='India'
        datatype='user'
        data='top'
        top_user_district_data={'data':[],'datatype':[],'total_reg_user_count':[],'country':[],'state':[],'district':[],'year':[],'quarter':[]}
        top_user_pincode_data={'data':[],'datatype':[],'total_reg_user_count':[],'country':[],'state':[],'pincode':[],'year':[],'quarter':[]}
        year_list=os.listdir(r'D:/python/project/phonepe p/pulse/data/top/user/country/india/state')

        for state in state_list:
            cur_year_path=top_tran_path+state
            year_list=os.listdir(cur_year_path)

            for year in year_list:
                cur_file_path=cur_year_path+'/'+year
                file_list=os.listdir(cur_file_path)
        
                for file in file_list:
                    cur_file= cur_file_path+'/'+file
                    cur_data=open(cur_file,'r')
                    temp=json.load(cur_data)                       
                    for items in temp['data']['districts']:
            
                        top_user_district_data['data'].append(data)
                        top_user_district_data['datatype'].append(datatype)
                        top_user_district_data['total_reg_user_count'].append(items['registeredUsers'])
                        top_user_district_data['country'].append(country)
                        top_user_district_data['state'].append(state)
                        top_user_district_data['district'].append(items['name'])
                        top_user_district_data['year'].append(year)
                        top_user_district_data['quarter'].append(int(file.strip('.json')))
                    
                    for items in temp['data']['pincodes']:
            
                        top_user_pincode_data['data'].append(data)
                        top_user_pincode_data['datatype'].append(datatype)
                        top_user_pincode_data['total_reg_user_count'].append(items['registeredUsers'])
                        top_user_pincode_data['country'].append(country)
                        top_user_pincode_data['state'].append(state)
                        top_user_pincode_data['pincode'].append(items['name'])
                        top_user_pincode_data['year'].append(year)
                        top_user_pincode_data['quarter'].append(int(file.strip('.json')))


        top_user_district_df=pd.DataFrame(top_user_district_data)
        top_user_pincode_df=pd.DataFrame(top_user_pincode_data)


        # print(top_user_district_df['state'].unique())
        top_user_district_df['state']=top_user_district_df['state'].str.replace('-',' ')
        top_user_district_df['state']=top_user_district_df['state'].str.title()
        top_user_district_df['state']=top_user_district_df['state'].str.replace('&','and')
        # print(top_user_district_df['state'].unique())
        # print(top_user_district_df['district'].unique())
        top_user_district_df['district']=top_user_district_df['district'].str.replace('-',' ')
        top_user_district_df['district']=top_user_district_df['district'].str.title()
        top_user_district_df['district']=top_user_district_df['district'].str.replace('&','and')
        top_user_district_df['district']=top_user_district_df['district'].str.replace(' And ',' and ')

        self.top_user_district_df=top_user_district_df

        # print(top_user_pincode_df['state'].unique())
        top_user_pincode_df['state']=top_user_pincode_df['state'].str.replace('-',' ')
        top_user_pincode_df['state']=top_user_pincode_df['state'].str.title()
        top_user_pincode_df['state']=top_user_pincode_df['state'].str.replace('&','and')
        # print(top_user_pincode_df['state'].unique())

        self.top_user_pincode_df=top_user_pincode_df

        #cursor.execute('Drop table top_user_district_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS top_user_district_data (tudd_data varchar(30),tudd_datatype varchar(20),tudd_reg_user_cnt int,tudd_country varchar(10),tudd_state varchar(100),tudd_district varchar(100),tudd_year int,tudd_quarter int);')
        insert='INSERT INTO top_user_district_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE top_user_district_data')
        m,n=top_tran_district_df.shape
        for i in range(m):
            values=[top_user_district_df['data'][i],top_user_district_df['datatype'][i],top_user_district_df['total_reg_user_count'][i],
                    top_user_district_df['country'][i],top_user_district_df['state'][i],top_user_district_df['district'][i],top_user_district_df['year'][i],top_user_district_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')

        #cursor.execute('Drop table top_user_pincode_data')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS top_user_pincode_data (tupd_data varchar(30),tupd_datatype varchar(20),tupd_reg_user_cnt int,tupd_country varchar(10),tupd_state varchar(100),tupd_pincode varchar(100),tupd_year int,tupd_quarter int);')
        insert='INSERT INTO top_user_pincode_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'
        self.cursor.execute('TRUNCATE TABLE top_user_pincode_data')
        m,n=top_user_pincode_df.shape
        for i in range(m):
            values=[top_user_pincode_df['data'][i],top_user_pincode_df['datatype'][i],top_user_pincode_df['total_reg_user_count'][i],
                    top_user_pincode_df['country'][i],top_user_pincode_df['state'][i],top_user_pincode_df['pincode'][i],top_user_pincode_df['year'][i],top_user_pincode_df['quarter'][i]]
            self.cursor.execute(insert,values)
        self.cursor.execute('COMMIT;')


    