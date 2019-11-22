from pandas import date_range

from config import vendor_list,report_table_list,server_info,report_types
from download_report import download_report
from sqlalchemy import create_engine

import turbodbc

def data_to_sql(report, vendor_code, table, day):
    """
        AppleMusic report types currently used
        are as follows:
        amStreams
        amContent
        amContentDemographics

        day arg should be in string formatted 'YYYYMMDD' format
    """
    
    engine = create_engine(server_info)
    df = download_report(report,day,vendor_code)
    df.to_sql(name=table, con=engine, if_exists='append',index=False)
    print('SQL Transfer Complete')
    return 


def sql_import(start_date, end_date):
    """ 
        This is to pull in all report types listed in report_types list. 
        Current available report types are:
            'amStreams'
            'amContent'
            'amContentDemographics'
    
        start_date and end_date args should both be in string format
    """

    counter = 0
    day_list = [day.strftime('%Y%m%d') for day in date_range(start_date,end_date)]
    for day in day_list:
        for vendor in vendor_list:
            for report in report_types:
                if report == 'amStreams':
                    table = 'AppleStreams'
                if report == 'amContent':
                    table = 'AppleTracks'
                else:
                    table = 'AppleContentDemographics'
                data_to_sql(report,vendor,table,day)
        counter = counter + 1
    print('Finished ' + str(counter) + ' Day(s) Transfered')
    return
