from googleapiclient.discovery import build
import pandas as pd
import pymongo as pm
import streamlit as sl


class database():
      def __init__(self):
            client=pm.MongoClient('mongodb://localhost:27017')
            self.db=client['guvi']
            self.db['channel_data']
            self.db['video_data']
            self.db['comment_data']

      def db_mover(self,channel_data: dict):


            #channel data insertion
            for i in range(len(channel_data['channel_id'])):
                  data={'channel_id': channel_data['channel_id'][i],'channel_name':channel_data['channel_name'][i],
                        'start_date':channel_data['start_date'][i],'total_views':channel_data['total_views'][i],
                        'total_subscribers':channel_data['total_subscribers'][i],'total_videos':channel_data['total_videos'][i],
                        'upload_id':channel_data['upload_id'][i]}
                  self.db.channel_data.insert_one(data)
                  #video data insertion
                  for j in range(len(channel_data['video_data'][i]['video_id'])):
                        data={'video_id':channel_data['video_data'][i]['video_id'][j],'channel_id':channel_data['video_data'][i]['channel_id'][j],
                              'video_title':channel_data['video_data'][i]['video_title'][j],'video_desc':channel_data['video_data'][i]['video_desc'][j]}
                        self.db.video_data.insert_one(data)
                        #comment data insertion
                        for k in range(len(channel_data['video_data'][i]['comment_data'][j]['comment_id'])):
                              data={'comment_id':channel_data['video_data'][i]['comment_data'][j]['comment_id'][k],'video_id':channel_data['video_data'][i]['comment_data'][j]['video_id'][k],
                                    'channel_id':channel_data['video_data'][i]['comment_data'][j]['channel_id'][k],'comment_by':channel_data['video_data'][i]['comment_data'][j]['comment_by'][k],
                                    'comment_msg':channel_data['video_data'][i]['comment_data'][j]['comment_msg'][k]}
                              self.db.comment_data.insert_one(data)

      def db_channel_data(self,id:str =None):
            if id:
                  return pd.DataFrame(self.db.channel_data.find({'channel_id':id},{"_id":0}))
            else:
                  return pd.DataFrame(self.db.channel_data.find({},{"_id":0}))
      def db_video_data(self,id:str=None):
            if id:
                  return pd.DataFrame(self.db.video_data.find({'channel_id':id},{"_id":0}))
            else:
                  return pd.DataFrame(self.db.video_data.find({},{"_id":0}))
      def db_comment_data(self,id:str=None):
            if id:
                  return pd.DataFrame(self.db.comment_data.find({'channel_id':id},{"_id":0}))
            else:
                  return pd.DataFrame(self.db.comment_data.find({},{"_id":0}))
            
      def db_delete(self,id:str):
            self.db.channel_data.delete_many({"channel_id":id})
            self.db.video_data.delete_many({"channel_id":id})
            self.db.comment_data.delete_many({"channel_id":id})

class YT_channel():
    
    def __init__(self):   
        service="youtube"
        version="v3"
        key='your YouTube api key'
        self.yt=build(service,version,developerKey=key)
    
    def extract_comment_data(self, id):
        comment_data=dict()
        nxt=None
        temp=0
        while True:
            comment_request=self.yt.commentThreads().list(part='snippet',videoId=id,pageToken=nxt,maxResults=50).execute()

            for i in range(len(comment_request['items'])):
                if temp==0:   
                    comment_data['channel_id']=[comment_request['items'][i]['snippet']['channelId']]
                    comment_data['video_id']=[comment_request['items'][i]['snippet']['topLevelComment']['snippet']['videoId']]
                    comment_data['comment_id']=[comment_request['items'][i]['snippet']['topLevelComment']['id']]
                    comment_data['comment_id']=[comment_request['items'][i]['id']]
                    comment_data['comment_by']=[comment_request['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']]
                    comment_data['comment_msg']=[comment_request['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']]
                    temp+=1
                
                else:
                    comment_data['channel_id'].append(comment_request['items'][i]['snippet']['channelId'])
                    comment_data['video_id'].append(comment_request['items'][i]['snippet']['topLevelComment']['snippet']['videoId'])
                    comment_data['comment_id'].append(comment_request['items'][i]['snippet']['topLevelComment']['id'])
                    comment_data['comment_id'].append(comment_request['items'][i]['id'])
                    comment_data['comment_by'].append(comment_request['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'])
                    comment_data['comment_msg'].append(comment_request['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']) 

            nxt=comment_request.get('nextPageToken')
            if nxt==None:
                break
        unique_id = []
        #removing duplicate comment ids
        for comment_id in comment_data['comment_id']:
            if comment_id not in unique_id:
                unique_id.append(comment_id)
        comment_data['comment_id']=unique_id

        return comment_data


    
    def extract_video_data(self,upload_id: list):
        playlist_data=dict()
        p=0
        for id in upload_id:
            nxt=None
            temp=0
            while True:
                playlist_response=self.yt.playlistItems().list(part='snippet',playlistId=id,pageToken=nxt,maxResults=50).execute()
             
                for i in range(len(playlist_response['items'])):
        
                    if temp==0:
                        playlist_data['channel_id']=[playlist_response['items'][i]['snippet']['channelId']]
                        playlist_data['video_id']=[playlist_response['items'][i]['snippet']['resourceId']['videoId']]
                        playlist_data['video_title']=[playlist_response['items'][i]['snippet']['title']]
                        playlist_data['video_desc']=[playlist_response['items'][i]['snippet']['description']]
                        playlist_data['video_crd']=[playlist_response['items'][i]['snippet']['publishedAt']]
                        playlist_data['video_upd']=[]
                        playlist_data['video_length']=[]
                        playlist_data['view_count']=[]
                        playlist_data['like_count']=[]
                        playlist_data['comment_count']=[]
                        playlist_data['favorite_count']=[]
                        playlist_data['playlist_id']=[playlist_response['items'][i]['snippet']['playlistId']]
                        playlist_data['comment_data']=[]
                        temp+=1
                    else:
                        playlist_data['channel_id'].append(playlist_response['items'][i]['snippet']['channelId'])
                        playlist_data['video_id'].append(playlist_response['items'][i]['snippet']['resourceId']['videoId'])
                        playlist_data['video_title'].append(playlist_response['items'][i]['snippet']['title'])
                        playlist_data['video_desc'].append(playlist_response['items'][i]['snippet']['description'])
                        playlist_data['video_crd'].append(playlist_response['items'][i]['snippet']['publishedAt'])
                        playlist_data['playlist_id'].append(playlist_response['items'][i]['snippet']['playlistId'])
                        
                    p+=1
                    video_response=self.yt.videos().list(part='snippet,contentDetails,statistics',id=playlist_response['items'][i]['snippet']['resourceId']['videoId']).execute()

                    for items in video_response['items']:
                        playlist_data['video_length'].append(items['contentDetails']['duration'])                        
                        playlist_data['view_count'].append(items['statistics']['viewCount'])
                        playlist_data['like_count'].append(items['statistics']['likeCount'])
                        playlist_data['comment_count'].append(items['statistics']['commentCount'])
                        playlist_data['favorite_count'].append(items['statistics']['favoriteCount'])
                    if items['statistics']['commentCount']==0:
                        playlist_data['comment_data'].append(None)    
                    else:
                        playlist_data['comment_data'].append(self.extract_comment_data(playlist_response['items'][i]['snippet']['resourceId']['videoId']))

                nxt=playlist_response.get('nextPageToken')
                if nxt==None:
                    break  
        return playlist_data


    def extract_channel_data(self,id : list):
        channel_data=dict()
        for channel_id in id:
            channel_response=self.yt.channels().list(part="id,snippet,contentDetails,statistics,localizations,status,topicDetails",id=channel_id).execute()
            temp=0
            for items in channel_response['items']:
                if temp==0:
                    channel_data['channel_id']=[items['id']]
                    channel_data['channel_name']=[items['snippet']['title']]
                    channel_data['start_date']=[items['snippet']['publishedAt']]
                    channel_data['total_views']=[items['statistics']['viewCount']]
                    channel_data['total_subscribers']=[items['statistics']['subscriberCount']]
                    channel_data['total_videos']=[items['statistics']['videoCount']]
                    channel_data['upload_id']=[items['contentDetails']['relatedPlaylists']['uploads']]
                    channel_data['video_data']=[]
                    temp+=1

                else:
                    channel_data['channel_id'].append(items['id'])
                    channel_data['channel_name'].append(items['snippet']['title'])
                    channel_data['start_date'].append(items['snippet']['publishedAt'])
                    channel_data['total_views'].append(items['statistics']['viewCount'])
                    channel_data['total_subscribers'].append(items['statistics']['subscriberCount'])
                    channel_data['total_videos'].append(items['statistics']['videoCount'])
                    channel_data['upload_id'].append(items['contentDetails']['relatedPlaylists']['uploads'])

            channel_data['video_data'].append(self.extract_video_data(channel_data['upload_id']))
        return channel_data
   
