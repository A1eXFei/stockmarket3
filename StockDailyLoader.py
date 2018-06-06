# -*- coding: UTF-8 -*-
import logging
import ConfigParser
import multiprocessing as mp
from datetime import *
from logging.config import fileConfig
from util import DateUtil as du
from util import StockUtil as su
from basic import StockBasicData
from StockTechCalculator import StockTechCalculator
from fundamental import StockFundamentalData
from StockExporter import StockExporter
from StockCleaner import StockCleaner

EXP_DIR = "D:\\StockData\\"
config_file = ConfigParser.SafeConfigParser()
config_file.read("./ss_config.ini")
EXP_DIR = config_file.get('export', 'dir')

fileConfig("logging_config.ini")
logger = logging.getLogger("daily")


def create_process(stock_code, start_date, end_date):
    logger.info("Start to process stock code: " + stock_code + " from " + start_date + " to " + end_date)
    sbd = StockBasicData()
    basic_data = sbd.download_basic_data(stock_code, start_date, end_date)
    basic_data_fq = sbd.download_basic_data_fq(stock_code, start_date, end_date)
    if (basic_data is not None) and (basic_data.shape[0] > 0):
        sbd.save_data(basic_data, basic_data_fq)
        sbd.update_end_date(stock_code, basic_data)
        logger.info("Basic data is downloaded and saved into database, is going to calculate tech indicator")
        for each in basic_data.itertuples():
            business_date = str(each.Index)
            logger.info("Calculate " + stock_code + " tech indicator for " + business_date)
            stc = StockTechCalculator(stock_code, business_date)
            stc.calculate_indicator()
        logger.info("All tech indicators are calculated")
        sfd = StockFundamentalData(stock_code, EXP_DIR)
        sfd.download_fundamental_data()
        if end_date[-5:] == "01-01":
            se = StockExporter(EXP_DIR, stock_code, start_date, end_date)
            se.export()
            sc = StockCleaner(stock_code, end_date)
            sc.clean()
        else:
            logger.info("Only the first day of the year will do export and clean")
    else:
        logger.warn("No data found for stock code: " + stock_code)

if __name__ == '__main__':
    try:
        now = datetime.now()
        today = du.convertDateToString(now, '%Y-%m-%d')
        logger.debug("Today is: " + today)

        # today = '2017-09-29'
        if su.is_working_day(today):
            sbd = StockBasicData()
            stock_list = sbd.get_stock_list(today)

            pool = mp.Pool(processes=1)
            for stock in stock_list:
                stock_code = stock[0]
                last_updated_date = du.convertDateToString(stock[1], '%Y-%m-%d')
                pool.apply_async(create_process, (stock_code, last_updated_date, today))

            pool.close()
            pool.join()
            logger.info("All stocks information is downloaded")
        else:
            logging.info("Today is holiday, program will terminate...")
    except Exception, e:
        print(e)
        logger.error(e.message)
