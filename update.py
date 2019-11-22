import pandas as pd

def update_values(stream_df):
    """
    Updates AppleMusic Streams report based to the detailed titles listed on the online documentation.
    https://help.apple.com/itc/contentreporterguide/#/
    """
    device_type_dic = {'0':"Other",'1':"Mobile",'2':"Desktop"}
    os_dic = {'0':"Other",'1':"iOS",'2':"Macintosh",'3':"Android",'4':"Windows",'5':"tvOS",'6':"Sonos"}
    end_reason_dic = {'0':"Complete",'1':"Skip",'2':"Other",'3':"Manually Changed",'4':"Paused"}
    offline_dic = {'0':"Online",'1':"Offline"}
    source_of_streams_dic = {'0':"Other",'1':"Library",'2':"Search",'3':"Discovery",'4':"MusicKit",'5':"External",'6':"Now Playing",}
    container_type_dic = {'0': "Single Track",'1': "Radio station",'2': "Playlist",'3': "Album"}
    container_sub_type_dic = {'0': 'Not applicable','1': 'Private User Playlist','2': 'Editorial Playlist','3': 'Artist Playlist','4': 'Curator Playlist','5': 'Seeded by Artist/Song','6': 'Format Station','7': 'Editorial Station','8': 'Personal Mix Playlist','9': 'New Music Mix','10': 'Favorites Mix','11': 'Chill Mix','13': 'Friends Mix','14':'Algorithm Station'}
    stream_df[r'Device Type'] = stream_df[r'Device Type'].replace(device_type_dic)
    stream_df[r'Operating System'] = stream_df[r'Operating System'].replace(os_dic)
    stream_df[r'End Reason Type'] = stream_df[r'End Reason Type'].replace(end_reason_dic)
    stream_df[r'Offline'] = stream_df[r'Offline'].replace(offline_dic)
    stream_df[r'Source of Stream'] = stream_df[r'Source of Stream'].replace(source_of_streams_dic)
    stream_df[r'Container Type'] = stream_df[r'Container Type'].replace(container_type_dic)
    stream_df[r'Container Sub-Type'] = stream_df[r'Container Sub-Type'].replace(container_sub_type_dic)
    return stream_df