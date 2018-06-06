import logging
from logging.config import fileConfig
from util import DatabaseUtil as dbu

fileConfig("logging_config.ini")
logger = logging.getLogger(__name__)


class StockCleaner():
    def __init__(self, stock_code, end_date):
        self.last_day = str(int(end_date[:4])-1) + "-01-01"
        self.stock_code = stock_code
        self.year = end_date[:4]
        self.sql_basic_data = "DELETE FROM pdtb_stock_basic_data t WHERE t.CODE ='" + stock_code + "' "
        self.sql_tech_data = "DELETE FROM pdtb_stock_basic_data t WHERE t.CODE ='" + stock_code + "' "
        self.sql_basic_data = self.sql_basic_data + "and t.DATE < '" + self.last_day + "'"
        self.sql_tech_data = self.sql_tech_data + "and t.DATE < '" + self.last_day + "'"

    def clean(self):
        logger.info("Delete data for stock code: " + self.stock_code)
        dbu.update(self.sql_basic_data)
        dbu.update(self.sql_tech_data)
        logger.info("Basic and Tech data less than year " + self.year + " are deleted")