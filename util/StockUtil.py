import DatabaseUtil as dbu
import pandas as pd
import numpy as np
import urllib2
import time

DAY_PRICE_COLUMNS = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                     'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']


def is_working_day(date):
    sql = "SELECT fn_is_holiday('" + date + "')"
    flag = dbu.get_data(sql)[0][0]
    if flag == 'W':
        return True
    else:
        return False


def get_basic_data(stock_code, date, time_period):
    sql = 'select * from pdtb_stock_basic_data t where t.code =\'' + stock_code + '\' and t.date <= \'' + date + '\' order by t.date desc limit 0,' + str(
        time_period)
    #print sql
    return dbu.get_pd_data(sql)


def get_tech_data(stock_code, date, time_period=1):
    sql = 'select * from pdtb_stock_tech_data t where code =\'' + stock_code + '\' and t.date <= \'' + date + '\' order by t.date desc limit 0,' + str(
        time_period)
    return dbu.save_pd_data(sql)

'''
def get_highest_price(real):
    return real.max()


def get_backteting_data(stock_code, strategy):
    sql = "select * from bktb_strategy_ratio where CODE='" + stock_code + "' and STRATEGY_ID LIKE '%" + strategy + "%' and STATUS='Y'"
    return dbu.save_pd_data(sql)


def get_backtest_ratio(dataframe, strategy_id):
    df = dataframe.set_index("STRATEGY_ID")
    try:
        value = 1.0 + df.loc[strategy_id]['RATIO'] / 100.0
    except:
        value = 1.0
    #print strategy_id + ":" + str(value)
    return round(value, 2)


def get_lowest_price(real):
    return real.min()
'''

def get_hist_data(stock_code, start_date, end_date, retry_count=10, pause=0.001):
    symbol = _code_to_symbol(stock_code)
    url_base = "http://quotes.money.163.com/service/chddata.html?"
    url_par_code = "code=" + symbol + "&"
    url_par_start = "start=" + start_date.replace("-","") + "&"
    url_par_end = "end=" + end_date.replace("-","") + "&"
    url_par_field = "fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"

    url = url_base + url_par_code + url_par_start + url_par_end + url_par_field
    print(url)

    cols = ['date','code','name','tclose','high','low','topen','lclose','chg','pchg','turnover','voturnover','vaturnover','tcap','mcap']
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request).read()
            lines = response.split("\n")[1:-1]
            if len(lines) < 2:
                raise Exception("No data received")
        except Exception as e:
            print e.message
            pass
        else:
            data = []
            for each in lines:
                data.append(each.split(","))
            df = pd.DataFrame(data, columns=cols)
            df.insert(loc=2,column="ma5",value=0)
            df.insert(loc=2,column="ma10",value=0)
            df.insert(loc=2,column="ma20",value=0)
            df.insert(loc=2,column="v_ma5",value=0)
            df.insert(loc=2,column="v_ma10",value=0)
            df.insert(loc=2,column="v_ma20",value=0)
            df.drop(["name","lclose","code","tcap","mcap","vaturnover"], axis= 1, inplace=True)
            df.replace(to_replace="None", value=np.NaN, inplace=True)
            df.dropna(axis=0, inplace=True)
            df = df.rename(columns={"tclose":"close","topen":"open","chg":"price_change","pchg":"p_change","voturnover":"volume"})
            for col in DAY_PRICE_COLUMNS[1:]:
                #print col
                df[col] = df[col].astype(float)
            df = df.set_index('date')
            df = df.sort_index(ascending = False)
            return df
    return None


def save_analysis_data(field_name, stock_code, date, analysis):
    sql = "update pdtb_stock_tech_analysis set " + field_name + " = '" + analysis + "' where code = '" + stock_code + "' and date = '" + date+ "'"
    #print sql
    dbu.update(sql)


def _code_to_symbol(stock_code):
    if len(stock_code) != 6:
        return ''
    else:
        return '0%s'%stock_code if stock_code[:1] in ['5', '6', '9'] else '1%s'%stock_code

'''
if __name__ == '__main__':
    #save_analysis_data('BBI','000001','2016-11-15','abc')
    df = get_backteting_data('000002', 'WR')
    print get_backtest_ratio(df, 'WR_S3')
'''