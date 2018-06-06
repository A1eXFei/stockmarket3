import logging
from logging.config import fileConfig
from util import DatabaseUtil as dbu

class StockTechIndicator(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        pass

    def save_tech_data(self, stock_code, date, dict):
        update_tech_sql = "update pdtb_stock_tech_data set "
        for key in dict:
            update_tech_sql = update_tech_sql + key+ "=" + str(dict[key]) + ", "
        update_tech_sql = update_tech_sql[:-2] + " where code = '" + stock_code + "' and date = '" + str(date) + "'"
        #print(update_tech_sql)
        dbu.update(update_tech_sql)


