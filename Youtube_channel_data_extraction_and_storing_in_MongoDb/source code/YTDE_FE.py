
import streamlit as sl
from youtube import YT_channel
from youtube import database

DB=database()
YT=YT_channel()

def display_data(data_type, channel_id):
    if data_type == "Channel Data":
        df = DB.db_channel_data(channel_id)
        sl.write(f"{data_type}:")
        sl.dataframe(df)
    elif data_type == "Video Data":
        df = DB.db_video_data(channel_id)
        sl.write(f"{data_type}:")
        sl.dataframe(df)
    elif data_type == "Comment Data":
        df = DB.db_comment_data(channel_id)
        sl.write(f"{data_type}:")
        sl.dataframe(df)
    else:
        sl.write("Channel Data")
        sl.dataframe(DB.db_channel_data(channel_id))
        sl.write("Video Data")
        sl.dataframe(DB.db_video_data(channel_id))
        sl.write("Comment Data")
        sl.dataframe(DB.db_comment_data(channel_id))


nav_option = sl.sidebar.selectbox("Navigation", ["Home", "Display Data"])

if  nav_option=='Home':
    sl.title('Youtube Channel Data Harvesting')
    channel_id=sl.text_input("Enter the channel id")
    col1, col2, col3 = sl.columns(3)
    
    sl.empty()
    with col1:
        if sl.button('Extract and Insert Data'):
            try:
                if channel_id not in DB.db_channel_data(channel_id)['channel_id'][0]:
                    channel_data=YT.extract_channel_data([channel_id])
                    DB.db_mover(channel_data)
                    sl.success('Data Moved Successfully ✅')
                else:
                    sl.error('Data already Present ❗')
            except:
                channel_data=YT.extract_channel_data([channel_id])
                DB.db_mover(channel_data)
                sl.success('Data Moved Successfully ✅')
    with col2:
        if sl.button('Repopulate Data'):
            try:
                if channel_id in DB.db_channel_data(channel_id)['channel_id'][0]:
                    DB.db_delete(channel_id)
                    channel_data=YT.extract_channel_data([channel_id])
                    DB.db_mover(channel_data)
                    sl.success('Data Moved Successfully ✅')
                else:
                    sl.error('Data not found ❗')
            except:
                sl.error('Database is Empty ❗kindly Extract and Insert First')
    with col3:
        if  sl.button('Delete Data'):
            try:
                if channel_id in DB.db_channel_data(channel_id)['channel_id'][0]:
                    DB.db_delete(channel_id)
                    sl.success('Data Deleted Successfully ✅')
                else:
                    sl.error('Data not found ❗')
            except:
                sl.error('Database is Empty ❗')


elif nav_option=='Display Data':
    try:
        sl.title('Youtube Channel Data Display')

        channel_id=sl.text_input("Enter the channel id")    
        col1, col2, col3, col4 = sl.columns(4)
        sl.empty()
        
        if channel_id in DB.db_channel_data(channel_id)['channel_id'][0]:
            data_type = sl.sidebar.radio("Select Data to Display", ["Channel Data", "Video Data", "Comment Data", "Display All"])
            display_data(data_type, channel_id)
            # with col1:
            #     if sl.button('Channel Data'):
            #         channel_df=DB.db_channel_data(channel_id)
            #         sl.dataframe(channel_df,wide_mode=True)

                        
            # with col2:
            #     if sl.button('Video Data'):

            #         video_df=DB.db_video_data(channel_id)
            #         sl.dataframe(video_df)
            # with col3:
            #     if sl.button('Comment Data'):
            #         comment_df=DB.db_comment_data(channel_id)
            #         sl.dataframe(comment_df)
            # with col4:
            #     if sl.button('Display All'):

            #         channel_df=DB.db_channel_data(channel_id)
            #         video_df=DB.db_video_data(channel_id)
            #         comment_df=DB.db_comment_data(channel_id)
            #         sl.dataframe(channel_df)
            #         sl.dataframe(video_df)
            #         sl.dataframe(comment_df)


        else:
            sl.error('Data not found ❗')
    except:
        sl.error('Database is empty ❗')
 

     


