SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS  `bktb_strategy`;
CREATE TABLE `bktb_strategy` (
  `STRATEGY_ID` varchar(20) NOT NULL,
  `BUY_SELL_INDICATOR` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`STRATEGY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `bktb_strategy_ratio`;
CREATE TABLE `bktb_strategy_ratio` (
  `CODE` varchar(20) NOT NULL,
  `START_DATE` date NOT NULL,
  `END_DATE` date NOT NULL,
  `STRATEGY_ID` varchar(20) NOT NULL,
  `RATIO` double DEFAULT NULL,
  `STATUS` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`CODE`,`START_DATE`,`END_DATE`,`STRATEGY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `bktb_strategy_ratio_his`;
CREATE TABLE `bktb_strategy_ratio_his` (
  `CODE` varchar(20) NOT NULL,
  `START_DATE` date NOT NULL,
  `END_DATE` date NOT NULL,
  `STRATEGY_ID` varchar(20) NOT NULL,
  `RATIO` double DEFAULT NULL,
  `STATUS` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_basic_data`;
CREATE TABLE `pdtb_stock_basic_data` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `OPEN` double DEFAULT NULL,
  `HIGH` double DEFAULT NULL,
  `CLOSE` double DEFAULT NULL,
  `LOW` double DEFAULT NULL,
  `VOLUME` double DEFAULT NULL,
  `PRICE_CHANGE` double DEFAULT NULL,
  `P_CHANGE` double DEFAULT NULL,
  `MA5` double DEFAULT NULL,
  `MA10` double DEFAULT NULL,
  `MA20` double DEFAULT NULL,
  `V_MA5` double DEFAULT NULL,
  `V_MA10` double DEFAULT NULL,
  `V_MA20` double DEFAULT NULL,
  `TURNOVER` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_basic_data_fq`;
CREATE TABLE `pdtb_stock_basic_data_fq` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `OPEN` double DEFAULT NULL,
  `HIGH` double DEFAULT NULL,
  `CLOSE` double DEFAULT NULL,
  `LOW` double DEFAULT NULL,
  `VOLUME` double DEFAULT NULL,
  `AMOUNT` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_basic_data_fq_his`;
CREATE TABLE `pdtb_stock_basic_data_fq_his` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `OPEN` double DEFAULT NULL,
  `HIGH` double DEFAULT NULL,
  `CLOSE` double DEFAULT NULL,
  `LOW` double DEFAULT NULL,
  `VOLUME` double DEFAULT NULL,
  `AMOUNT` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_basic_data_his`;
CREATE TABLE `pdtb_stock_basic_data_his` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `OPEN` double DEFAULT NULL,
  `HIGH` double DEFAULT NULL,
  `CLOSE` double DEFAULT NULL,
  `LOW` double DEFAULT NULL,
  `VOLUME` double DEFAULT NULL,
  `PRICE_CHANGE` double DEFAULT NULL,
  `P_CHANGE` double DEFAULT NULL,
  `MA5` double DEFAULT NULL,
  `MA10` double DEFAULT NULL,
  `MA20` double DEFAULT NULL,
  `V_MA5` double DEFAULT NULL,
  `V_MA10` double DEFAULT NULL,
  `V_MA20` double DEFAULT NULL,
  `TURNOVER` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_calendar`;
CREATE TABLE `pdtb_stock_calendar` (
  `MONTH` varchar(10) NOT NULL,
  `CALENDAR` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`MONTH`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_cashflow_data`;
CREATE TABLE `pdtb_stock_cashflow_data` (
  `period` varchar(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `cf_sales` double DEFAULT NULL COMMENT '经营现金净流量对销售收入比率',
  `rateofreturn` double DEFAULT NULL COMMENT '资产的经营现金流量回报率',
  `cf_nm` double DEFAULT NULL COMMENT '经营现金净流量与净利润的比率',
  `cf_liabilities` double DEFAULT NULL COMMENT '经营现金净流量对负债比率',
  `cashflowratio` double DEFAULT NULL COMMENT '现金流量比率',
  PRIMARY KEY (`code`,`period`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_debtpaying_data`;
CREATE TABLE `pdtb_stock_debtpaying_data` (
  `period` varchar(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `currentratio` double DEFAULT NULL COMMENT '流动比率',
  `quickratio` double DEFAULT NULL COMMENT '速动比率',
  `cashratio` double DEFAULT NULL COMMENT '现金比率',
  `icratio` double DEFAULT NULL COMMENT '利息支付倍数',
  `sheqratio` double DEFAULT NULL COMMENT '股东权益比率',
  `adratio` double DEFAULT NULL COMMENT '股东权益增长率',
  PRIMARY KEY (`code`,`period`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_growth_data`;
CREATE TABLE `pdtb_stock_growth_data` (
  `period` varchar(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `mbrg` double DEFAULT NULL COMMENT '主营业务收入增长率(%)',
  `nprg` double DEFAULT NULL COMMENT '净利润增长率(%)',
  `nav` double DEFAULT NULL COMMENT '净资产增长率',
  `targ` double DEFAULT NULL COMMENT '总资产增长率',
  `epsg` double DEFAULT NULL COMMENT '每股收益增长率',
  `seg` double DEFAULT NULL COMMENT '股东权益增长率',
  PRIMARY KEY (`code`,`period`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_list`;
CREATE TABLE `pdtb_stock_list` (
  `CODE` varchar(10) NOT NULL,
  `NAME` varchar(20) DEFAULT NULL,
  `INDUSTRY` varchar(10) DEFAULT NULL,
  `AREA` varchar(10) DEFAULT NULL,
  `PE` double DEFAULT NULL,
  `OUTSTANDING` double DEFAULT NULL,
  `TOTALS` double DEFAULT NULL,
  `TOTALASSETS` double DEFAULT NULL,
  `LIQUIDASSETS` double DEFAULT NULL,
  `FIXEDASSETS` double DEFAULT NULL,
  `RESERVED` double DEFAULT NULL,
  `RESERVEDPERSHARE` double DEFAULT NULL,
  `ESP` varchar(45) DEFAULT NULL,
  `BVPS` double DEFAULT NULL,
  `PB` double DEFAULT NULL,
  `TIMETOMARKET` date DEFAULT NULL,
  `LASTUPDATEDDATE` date DEFAULT NULL,
  `PINYIN` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_list_bak`;
CREATE TABLE `pdtb_stock_list_bak` (
  `CODE` varchar(10) NOT NULL,
  `NAME` varchar(20) DEFAULT NULL,
  `INDUSTRY` varchar(10) DEFAULT NULL,
  `AREA` varchar(10) DEFAULT NULL,
  `PE` double DEFAULT NULL,
  `OUTSTANDING` double DEFAULT NULL,
  `TOTALS` double DEFAULT NULL,
  `TOTALASSETS` double DEFAULT NULL,
  `LIQUIDASSETS` double DEFAULT NULL,
  `FIXEDASSETS` double DEFAULT NULL,
  `RESERVED` double DEFAULT NULL,
  `RESERVEDPERSHARE` double DEFAULT NULL,
  `ESP` varchar(45) DEFAULT NULL,
  `BVPS` double DEFAULT NULL,
  `PB` double DEFAULT NULL,
  `TIMETOMARKET` date DEFAULT NULL,
  `LASTUPDATEDDATE` date DEFAULT NULL,
  `PINYIN` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_operation_data`;
CREATE TABLE `pdtb_stock_operation_data` (
  `period` varchar(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `arturnover` double DEFAULT NULL COMMENT '应收账款周转率(次)',
  `arturndays` double DEFAULT NULL COMMENT '应收账款周转天数(天)',
  `inventory_turnover` double DEFAULT NULL COMMENT '存货周转率(次)',
  `inventory_days` double DEFAULT NULL COMMENT '存货周转天数(天)',
  `currentasset_turnover` double DEFAULT NULL COMMENT '流动资产周转率(次)',
  `currentasset_days` double DEFAULT NULL COMMENT '流动资产周转天数(天)',
  PRIMARY KEY (`code`,`period`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_profit_data`;
CREATE TABLE `pdtb_stock_profit_data` (
  `period` varchar(5) NOT NULL,
  `code` varchar(10) NOT NULL,
  `roe` double DEFAULT NULL COMMENT '净资产收益率(%)',
  `net_profit_ratio` double DEFAULT NULL COMMENT '净利率(%)',
  `gross_profit_rate` double DEFAULT NULL COMMENT '毛利率(%)',
  `net_profits` double DEFAULT NULL COMMENT '净利润(万元)',
  `eps` double DEFAULT NULL COMMENT '每股收益',
  `business_income` double DEFAULT NULL COMMENT '营业收入(百万元)',
  `bips` double DEFAULT NULL COMMENT '每股主营业务收入(元)',
  PRIMARY KEY (`code`,`period`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_tech_analysis`;
CREATE TABLE `pdtb_stock_tech_analysis` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `BBI` varchar(500) DEFAULT NULL,
  `BIAS` varchar(500) DEFAULT NULL,
  `BOLL` varchar(500) DEFAULT NULL,
  `BRAR` varchar(500) DEFAULT NULL,
  `CCI` varchar(500) DEFAULT NULL,
  `DMA` varchar(500) DEFAULT NULL,
  `DMI` varchar(500) DEFAULT NULL,
  `KDJ` varchar(500) DEFAULT NULL,
  `MA` varchar(500) DEFAULT NULL,
  `PSY` varchar(500) DEFAULT NULL,
  `ROC` varchar(500) DEFAULT NULL,
  `RSI` varchar(500) DEFAULT NULL,
  `VR` varchar(500) DEFAULT NULL,
  `WR` varchar(500) DEFAULT NULL,
  `HIS` varchar(500) DEFAULT NULL,
  `KLINE` varchar(500) DEFAULT NULL,
  `MACD` varchar(500) DEFAULT NULL,
  `TOTAL_SCORE` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_tech_analysis_his`;
CREATE TABLE `pdtb_stock_tech_analysis_his` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `BBI` varchar(500) DEFAULT NULL,
  `BIAS` varchar(500) DEFAULT NULL,
  `BOLL` varchar(500) DEFAULT NULL,
  `BRAR` varchar(500) DEFAULT NULL,
  `CCI` varchar(500) DEFAULT NULL,
  `DMA` varchar(500) DEFAULT NULL,
  `DMI` varchar(500) DEFAULT NULL,
  `KDJ` varchar(500) DEFAULT NULL,
  `MA` varchar(500) DEFAULT NULL,
  `PSY` varchar(500) DEFAULT NULL,
  `ROC` varchar(500) DEFAULT NULL,
  `RSI` varchar(500) DEFAULT NULL,
  `VR` varchar(500) DEFAULT NULL,
  `WR` varchar(500) DEFAULT NULL,
  `HIS` varchar(500) DEFAULT NULL,
  `KLINE` varchar(500) DEFAULT NULL,
  `MACD` varchar(500) DEFAULT NULL,
  `TOTAL_SCORE` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_tech_data`;
CREATE TABLE `pdtb_stock_tech_data` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `EXPMA12` double DEFAULT NULL,
  `EXPMA50` double DEFAULT NULL,
  `KDJ_K` double DEFAULT NULL,
  `KDJ_D` double DEFAULT NULL,
  `KDJ_J` double DEFAULT NULL,
  `RSI` double DEFAULT NULL,
  `WR` double DEFAULT NULL,
  `BIAS6` double DEFAULT NULL,
  `BIAS12` double DEFAULT NULL,
  `BIAS24` double DEFAULT NULL,
  `CCI` double DEFAULT NULL,
  `ROC` double DEFAULT NULL,
  `BBI` double DEFAULT NULL,
  `BRAR_BR` double DEFAULT NULL,
  `BRAR_AR` double DEFAULT NULL,
  `PSY` double DEFAULT NULL,
  `DMA` double DEFAULT NULL,
  `AMA` double DEFAULT NULL,
  `BOLL_MID` double DEFAULT NULL,
  `BOLL_UP` double DEFAULT NULL,
  `BOLL_LOW` double DEFAULT NULL,
  `VR` double DEFAULT NULL,
  `DMI_ADX` double DEFAULT NULL,
  `DMI_ADXR` double DEFAULT NULL,
  `DMI_PDI` double DEFAULT NULL,
  `DMI_MDI` double DEFAULT NULL,
  `MACD_DIF` double DEFAULT NULL,
  `MACD_DEF` double DEFAULT NULL,
  `MACD` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `pdtb_stock_tech_data_his`;
CREATE TABLE `pdtb_stock_tech_data_his` (
  `DATE` date NOT NULL,
  `CODE` varchar(10) NOT NULL,
  `EXPMA12` double DEFAULT NULL,
  `EXPMA50` double DEFAULT NULL,
  `KDJ_K` double DEFAULT NULL,
  `KDJ_D` double DEFAULT NULL,
  `KDJ_J` double DEFAULT NULL,
  `RSI` double DEFAULT NULL,
  `WR` double DEFAULT NULL,
  `BIAS6` double DEFAULT NULL,
  `BIAS12` double DEFAULT NULL,
  `BIAS24` double DEFAULT NULL,
  `CCI` double DEFAULT NULL,
  `ROC` double DEFAULT NULL,
  `BBI` double DEFAULT NULL,
  `BRAR_BR` double DEFAULT NULL,
  `BRAR_AR` double DEFAULT NULL,
  `PSY` double DEFAULT NULL,
  `DMA` double DEFAULT NULL,
  `AMA` double DEFAULT NULL,
  `BOLL_MID` double DEFAULT NULL,
  `BOLL_UP` double DEFAULT NULL,
  `BOLL_LOW` double DEFAULT NULL,
  `VR` double DEFAULT NULL,
  `DMI_ADX` double DEFAULT NULL,
  `DMI_ADXR` double DEFAULT NULL,
  `DMI_PDI` double DEFAULT NULL,
  `DMI_MDI` double DEFAULT NULL,
  `MACD_DIF` double DEFAULT NULL,
  `MACD_DEF` double DEFAULT NULL,
  `MACD` double DEFAULT NULL,
  PRIMARY KEY (`DATE`,`CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_batch_log`;
CREATE TABLE `sdtb_batch_log` (
  `DATE` date NOT NULL,
  `START_TIME` datetime DEFAULT NULL,
  `END_TIME` datetime DEFAULT NULL,
  `STATUS` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`DATE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_batch_schedule`;
CREATE TABLE `sdtb_batch_schedule` (
  `BATCH_NAME` varchar(20) NOT NULL,
  `NEXT_RUN_DATE` date DEFAULT NULL,
  `PARAMETERS` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`BATCH_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_message`;
CREATE TABLE `sdtb_message` (
  `ID` int(11) NOT NULL,
  `TYPE` varchar(10) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  `CONTENT` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_stock_cashflow_data_tmp`;
CREATE TABLE `sdtb_stock_cashflow_data_tmp` (
  `period` varchar(5) DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `cf_sales` double DEFAULT NULL COMMENT '经营现金净流量对销售收入比率',
  `rateofreturn` double DEFAULT NULL COMMENT '资产的经营现金流量回报率',
  `cf_nm` double DEFAULT NULL COMMENT '经营现金净流量与净利润的比率',
  `cf_liabilities` double DEFAULT NULL COMMENT '经营现金净流量对负债比率',
  `cashflowratio` double DEFAULT NULL COMMENT '现金流量比率',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_stock_debtpaying_data_tmp`;
CREATE TABLE `sdtb_stock_debtpaying_data_tmp` (
  `period` varchar(5) DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `currentratio` double DEFAULT NULL COMMENT '流动比率',
  `quickratio` double DEFAULT NULL COMMENT '速动比率',
  `cashratio` double DEFAULT NULL COMMENT '现金比率',
  `icratio` double DEFAULT NULL COMMENT '利息支付倍数',
  `sheqratio` double DEFAULT NULL COMMENT '股东权益比率',
  `adratio` double DEFAULT NULL COMMENT '股东权益增长率',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_stock_growth_data_tmp`;
CREATE TABLE `sdtb_stock_growth_data_tmp` (
  `period` varchar(5) DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `mbrg` double DEFAULT NULL COMMENT '主营业务收入增长率(%)',
  `nprg` double DEFAULT NULL COMMENT '净利润增长率(%)',
  `nav` double DEFAULT NULL COMMENT '净资产增长率',
  `targ` double DEFAULT NULL COMMENT '总资产增长率',
  `epsg` double DEFAULT NULL COMMENT '每股收益增长率',
  `seg` double DEFAULT NULL COMMENT '股东权益增长率',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_stock_list_tmp`;
CREATE TABLE `sdtb_stock_list_tmp` (
  `code` varchar(10) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `industry` varchar(10) DEFAULT NULL,
  `area` varchar(10) DEFAULT NULL,
  `pe` double DEFAULT NULL,
  `outstanding` double DEFAULT NULL,
  `totals` double DEFAULT NULL,
  `totalAssets` double DEFAULT NULL,
  `liquidAssets` double DEFAULT NULL,
  `fixedAssets` double DEFAULT NULL,
  `reserved` double DEFAULT NULL,
  `reservedPerShare` double DEFAULT NULL,
  `esp` varchar(45) DEFAULT NULL,
  `bvps` double DEFAULT NULL,
  `pb` double DEFAULT NULL,
  `timeToMarket` bigint(20) DEFAULT NULL,
  `undp` double DEFAULT NULL,
  `perundp` double DEFAULT NULL,
  `rev` double DEFAULT NULL,
  `profit` double DEFAULT NULL,
  `gpr` double DEFAULT NULL,
  `npr` double DEFAULT NULL,
  `holders` double DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_stock_operation_data_tmp`;
CREATE TABLE `sdtb_stock_operation_data_tmp` (
  `period` varchar(5) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `arturnover` double DEFAULT NULL COMMENT '应收账款周转率(次)',
  `arturndays` double DEFAULT NULL COMMENT '应收账款周转天数(天)',
  `inventory_turnover` double DEFAULT NULL COMMENT '存货周转率(次)',
  `inventory_days` double DEFAULT NULL COMMENT '存货周转天数(天)',
  `currentasset_turnover` double DEFAULT NULL COMMENT '流动资产周转率(次)',
  `currentasset_days` double DEFAULT NULL COMMENT '流动资产周转天数(天)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS  `sdtb_stock_profit_data_tmp`;
CREATE TABLE `sdtb_stock_profit_data_tmp` (
  `period` varchar(5) DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `roe` double DEFAULT NULL COMMENT '净资产收益率(%)',
  `net_profit_ratio` double DEFAULT NULL COMMENT '净利率(%)',
  `gross_profit_rate` double DEFAULT NULL COMMENT '毛利率(%)',
  `net_profits` double DEFAULT NULL COMMENT '净利润(万元)',
  `eps` double DEFAULT NULL COMMENT '每股收益',
  `business_income` double DEFAULT NULL COMMENT '营业收入(百万元)',
  `bips` double DEFAULT NULL COMMENT '每股主营业务收入(元)',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;

/* VIEWS */;
DROP VIEW IF EXISTS `pdvw_stock_basic_data`;
CREATE VIEW `pdvw_stock_basic_data` AS select `b`.`DATE` AS `DATE`,`b`.`CODE` AS `CODE`,`b`.`OPEN` AS `OPEN`,`b`.`HIGH` AS `HIGH`,`b`.`CLOSE` AS `CLOSE`,`b`.`LOW` AS `LOW`,`b`.`VOLUME` AS `VOLUME`,`b`.`PRICE_CHANGE` AS `PRICE_CHANGE`,`b`.`P_CHANGE` AS `P_CHANGE`,`b`.`MA5` AS `MA5`,`b`.`MA10` AS `MA10`,`b`.`MA20` AS `MA20`,`b`.`V_MA5` AS `V_MA5`,`b`.`V_MA10` AS `V_MA10`,`b`.`V_MA20` AS `V_MA20`,`b`.`TURNOVER` AS `TURNOVER`,`f`.`CLOSE` AS `CLOSE_ADJ`,concat(ifnull(`t`.`BBI`,''),ifnull(`t`.`BIAS`,''),ifnull(`t`.`BOLL`,''),ifnull(`t`.`BRAR`,''),ifnull(`t`.`CCI`,''),ifnull(`t`.`DMA`,''),ifnull(`t`.`DMI`,''),ifnull(`t`.`KDJ`,''),ifnull(`t`.`KLINE`,''),ifnull(`t`.`MA`,''),ifnull(`t`.`PSY`,''),ifnull(`t`.`ROC`,''),ifnull(`t`.`RSI`,''),ifnull(`t`.`VR`,''),ifnull(`t`.`WR`,'')) AS `INDICATORS`,`t`.`TOTAL_SCORE` AS `TOTAL_SCORE` from ((`pdtb_stock_basic_data` `b` join `pdtb_stock_tech_analysis` `t`) left join `pdtb_stock_basic_data_fq` `f` on(((`b`.`DATE` = `f`.`DATE`) and (`b`.`CODE` = `f`.`CODE`)))) where ((`b`.`DATE` = `t`.`DATE`) and (`b`.`CODE` = `t`.`CODE`));

/* PROCEDURES */;
DROP PROCEDURE IF EXISTS `prc_check_stock_list`;
DELIMITER $$
CREATE PROCEDURE `prc_check_stock_list`()
BEGIN
	INSERT INTO pdtb_stock_list
    SELECT tmp.code,
		tmp.name,
		tmp.industry,
		tmp.area,
		tmp.pe,
		tmp.outstanding,
		tmp.totals,
		tmp.totalAssets, 
		tmp.liquidAssets,
		tmp.fixedAssets,
		tmp.reserved,
		tmp.reservedPerShare,
		tmp.esp,
		tmp.bvps,
		tmp.pb,
		tmp.timeToMarket, '1991-01-01', '' FROM sdtb_stock_list_tmp tmp
    WHERE tmp.CODE NOT IN (SELECT mst.CODE FROM pdtb_stock_list mst);
    
    UPDATE pdtb_stock_list mst
		SET mst.NAME = (SELECT tmp.NAME FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.INDUSTRY = (SELECT tmp.INDUSTRY FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.AREA = (SELECT tmp.AREA FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE), 
			mst.PE = (SELECT tmp.PE FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE), 
			mst.OUTSTANDING = (SELECT tmp.OUTSTANDING FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.TOTALS = (SELECT tmp.TOTALS FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.TOTALASSETS = (SELECT tmp.TOTALASSETS FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.LIQUIDASSETS = (SELECT tmp.LIQUIDASSETS FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.FIXEDASSETS = (SELECT tmp.FIXEDASSETS FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE), 
			mst.RESERVED = (SELECT tmp.RESERVED FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE), 
			mst.RESERVEDPERSHARE = (SELECT tmp.RESERVEDPERSHARE FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.ESP = (SELECT tmp.ESP FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.BVPS = (SELECT tmp.BVPS FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.PB = (SELECT tmp.PB FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE),
			mst.TIMETOMARKET = (SELECT tmp.TIMETOMARKET FROM sdtb_stock_list_tmp tmp WHERE tmp.CODE = mst.CODE);
    
	DELETE FROM sdtb_stock_list_tmp;
END
$$
DELIMITER ;

DROP PROCEDURE IF EXISTS `prc_purge_data`;
DELIMITER $$
CREATE PROCEDURE `prc_purge_data`(p_date date)
BEGIN
	insert into pdtb_stock_basic_data_his 
    select * from pdtb_stock_basic_data where date < p_date;
    
    insert into pdtb_stock_basic_data_fq_his 
    select * from pdtb_stock_basic_data_fq where date < p_date;
    
    insert into pdtb_stock_tech_data_his
    select * from pdtb_stock_tech_data where date < p_date;
    
    insert into pdtb_stock_tech_analysis_his 
    select * from pdtb_stock_tech_analysis where date < p_date;
    
    delete from pdtb_stock_basic_data where date < p_date;
    delete from pdtb_stock_basic_data_fq where date < p_date;
    delete from pdtb_stock_tech_data where date < p_date;
    delete from pdtb_stock_tech_analysis where date < p_date;
END
$$
DELIMITER ;

DROP PROCEDURE IF EXISTS `prc_refresh_fundamental_data`;
DELIMITER $$
CREATE PROCEDURE `prc_refresh_fundamental_data`(p_period varchar(5))
BEGIN
	DELETE FROM pdtb_stock_cashflow_data WHERE period = p_period;
    DELETE FROM pdtb_stock_debtpaying_data WHERE period = p_period;
    DELETE FROM pdtb_stock_growth_data WHERE period = p_period;
    DELETE FROM pdtb_stock_operation_data WHERE period = p_period;
    DELETE FROM pdtb_stock_profit_data WHERE period = p_period;
    
    INSERT INTO pdtb_stock_cashflow_data 
    SELECT period, code, cf_sales, rateofreturn, cf_nm, cf_liabilities, cashflowratio FROM sdtb_stock_cashflow_data_tmp;
    
    INSERT INTO pdtb_stock_debtpaying_data 
    SELECT period, code, currentratio, quickratio, cashratio, icratio, sheqratio, adratio FROM sdtb_stock_debtpaying_data_tmp;
    
    INSERT INTO pdtb_stock_growth_data 
    SELECT period, code, mbrg, nprg, nav, targ, epsg, seg FROM sdtb_stock_growth_data_tmp;
    
    INSERT INTO pdtb_stock_operation_data 
    SELECT period, code, arturnover, arturndays, inventory_turnover, inventory_days, currentasset_turnover, currentasset_days FROM sdtb_stock_operation_data_tmp;
    
    INSERT INTO pdtb_stock_profit_data
    SELECT period, code, roe, net_profit_ratio, gross_profit_rate, net_profits, eps, business_income, bips FROM sdtb_stock_profit_data_tmp;
    
    DELETE FROM sdtb_stock_cashflow_data_tmp;
	DELETE FROM sdtb_stock_debtpaying_data_tmp;
	DELETE FROM sdtb_stock_growth_data_tmp;
	DELETE FROM sdtb_stock_operation_data_tmp;
	DELETE FROM sdtb_stock_profit_data_tmp;
END
$$
DELIMITER ;

/* FUNCTIONS */;
DROP FUNCTION IF EXISTS `fn_get_last_workingday`;
DELIMITER $$
CREATE FUNCTION `fn_get_last_workingday`(p_date varchar(10)) RETURNS varchar(10) CHARSET utf8
    DETERMINISTIC
BEGIN
	DECLARE v_flag VARCHAR(1);
    DECLARE v_date DATE;
    
    SET v_date := str_to_date(p_date,'%Y-%m-%d');
	SET v_flag := fn_is_holiday(p_date);    
    
    WHILE v_flag <> 'W' DO 
		SET v_date := DATE_ADD(v_date, INTERVAL -1 DAY);
		SET v_flag := fn_is_holiday(DATE_FORMAT(v_date, '%Y-%m-%d'));    
	END WHILE;

RETURN DATE_FORMAT(v_date, '%Y-%m-%d');
END
$$
DELIMITER ;

DROP FUNCTION IF EXISTS `fn_get_next_workingday`;
DELIMITER $$
CREATE FUNCTION `fn_get_next_workingday`(p_date varchar(10)) RETURNS varchar(10) CHARSET utf8
    DETERMINISTIC
BEGIN
	DECLARE v_flag VARCHAR(1);
    DECLARE v_date DATE;
    
    SET v_date := str_to_date(p_date,'%Y-%m-%d');
    SET v_date := DATE_ADD(v_date, INTERVAL 1 DAY);
	SET v_flag := fn_is_holiday(v_date);    
    
    WHILE v_flag <> 'W' DO 
		SET v_date := DATE_ADD(v_date, INTERVAL 1 DAY);
		SET v_flag := fn_is_holiday(DATE_FORMAT(v_date, '%Y-%m-%d'));    
	END WHILE;
RETURN DATE_FORMAT(v_date, '%Y-%m-%d');
END
$$
DELIMITER ;

DROP FUNCTION IF EXISTS `fn_is_holiday`;
DELIMITER $$
CREATE FUNCTION `fn_is_holiday`(p_date varchar(10)) RETURNS varchar(1) CHARSET utf8
    DETERMINISTIC
BEGIN
	DECLARE v_year VARCHAR(4);
    DECLARE v_month VARCHAR(2);
    DECLARE v_day VARCHAR(2);
    DECLARE v_calendar VARCHAR(31);
    
    SET v_year := substr(p_date, 1, 4);
    SET v_month := substr(p_date, 6, 2);
    SET v_day := substr(p_date, 9, 2);
    
    SELECT 
		calendar 
	INTO v_calendar 
    FROM pdtb_stock_calendar
    WHERE month = concat(v_year, v_month);
    
    RETURN substr(v_calendar, convert(v_day, UNSIGNED INTEGER), 1);
END
$$
DELIMITER ;

