from config import reporter_access_token
from pandas import DataFrame
from update import update_values
import pandas as pd
import reporter


def download_report(report_to_pull, day_of_report,vendor_code):
    """ 
        Returns a pandas DataFrame object

        reports_to_pull can be any of the following, but usually 
        are limited to AppleMusic reports which are demoted by a 
        preceding 'am':

            Sales, Pre-Order, Cloud, amEvent, amContent, amControl,amStreams,
            amContentDemographics,amArtistDemographics, ContentDemographics,
            ArtistDemographics

        day_of_report should be in string format

    """
    rep = reporter.Reporter(access_token=reporter_access_token)
    get_content = rep.download_sales_report
    
    if report_to_pull=='amContentDemographics':
        report =  get_content(vendor=vendor_code,report_type='amContentDemographics',date_type='Daily',date=day_of_report,report_subtype='Summary',report_version='1_1')
        df = DataFrame.from_dict(report).astype({r'Apple Identifier':int,r'Action Type':int,r'Gender':int,r'Listeners':str,r'Streams':str,r'Listeners Last 7 Days':int,r'Streams Last 7 Days':int})
        df[r'Report Date'] = pd.to_datetime(df[r'Report Date'],format='%Y-%m-%d')
        df[r'Report Date'] = pd.to_datetime(df[r'Report Date'],format='%Y%m%d')

    elif report_to_pull=='amContent':
        report =  get_content(vendor=vendor_code,report_type='amContent',date_type='Daily',date=day_of_report,report_subtype='Detailed',report_version='1_2')
        df = DataFrame.from_dict(report).astype({r'Apple Identifier':int,r'Item Type':int,r'Media Type':int,r'Media Duration':int})
        df[r'Report Date'] = day_of_report
        df[r'Report Date'] = pd.to_datetime(df[r'Report Date'],format='%Y%m%d')
    else: 
        report =  get_content(vendor=vendor_code,report_type=report_to_pull,date_type='Daily',date=day_of_report,report_subtype='Detailed',report_version='1_2')
        df = DataFrame.from_dict(report).astype({'Datestamp':str,r'Apple Identifier':int,r'Ingest Timestamp':str,r'Device Type':str,r'Operating System':str,r'Action Type':int,r'End Reason Type':str,r'Offline':str,r'Source of Stream':str,r'Container Type':str,r'Container Sub-Type':str, r'Stream Timestamp':str,r'Stream Start Position':int,r'Stream Duration':int})
        df[r'Datestamp'] = pd.to_datetime(df[r'Datestamp'],format='%Y-%m-%d')
        df[r'Report Date'] = day_of_report
        df[r'Report Date'] = pd.to_datetime(df[r'Report Date'],format='%Y%m%d')
        df = update_values(df)
    size = df.memory_usage(index=True,deep=True).sum()    
    print('Downloaded {}{} from {} account ({:,} bytes)'.format(report_to_pull,day_of_report,vendor_code,size))
    return df