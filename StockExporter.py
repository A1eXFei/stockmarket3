# -*- coding: UTF-8 -*-
import os
import logging
from logging.config import fileConfig
from util import DatabaseUtil as dbu
from util import ExportUtil as eu


fileConfig("logging_config.ini")
logger = logging.getLogger(__name__)


class StockExporter():
    def __init__(self, export_dir, stock_code, start_date, end_date):
        self.dir = export_dir
        self.stock_code = stock_code
        self.end_year = int(end_date[:4])
        self.start_year = int(start_date[:4])

        if self.end_year == self.start_year:
            self.start_year = self.end_year - 1

        self.sql_basic_data = "SELECT * FROM pdtb_stock_basic_data t WHERE t.CODE ='" + self.stock_code + "' "
        self.sql_tech_data = "SELECT * FROM pdtb_stock_tech_data t WHERE t.CODE ='" + self.stock_code + "' "

    def export(self):
        for year in range(self.start_year, self.end_year):
            logger.info("Export data for stock code " + self.stock_code + " for year " + str(year))
            current_dir = self.dir + os.sep + self.stock_code + os.sep + str(year)

            first_day = str(year) + "-01-01"
            last_day = str(year) + "-12-31"

            '''EXPORT BASIC DATA'''
            basic_data_filename = "BASIC_" + self.stock_code + "_" + str(year) + ".csv"
            sql_basic_data = self.sql_basic_data + "and t.DATE BETWEEN '" + first_day + "' AND '" + last_day + "'"
            basic_data = dbu.get_pd_data(sql_basic_data)
            if basic_data.shape[0] > 0:
                if not os.path.exists(current_dir):
                    logger.debug("Make dir because there is no existing dir")
                    os.makedirs(current_dir)
                eu.export(current_dir, basic_data_filename, basic_data)
                logger.info("Basic data exported")

            '''EXPORT TECH DATA'''
            tech_data_filename = "TECH_" + self.stock_code + "_" + str(year) + ".csv"
            sql_tech_data = self.sql_tech_data + "and t.DATE BETWEEN '" + first_day + "' AND '" + last_day + "'"
            tech_data = dbu.get_pd_data(sql_tech_data)
            if tech_data.shape[0] > 0:
                if not os.path.exists(current_dir):
                    logger.debug("Make dir because there is no existing dir")
                    os.makedirs(current_dir)
                eu.export(current_dir, tech_data_filename, tech_data)
                logger.info("Tech data exported")
