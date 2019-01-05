#!/usr/bin/env python

from flask import Flask, flash, redirect, render_template, \
     request, url_for
from pytrends.request import TrendReq
import json
import pandas as pd

pd.set_option('display.max_colwidth', -1)

def get_info_usa(timeframe):
    res_df = []
    all_words = [['ada','altcoin','altcoins','bitcoin','bitconnect'],['bitminter', 'blockchain', 'blockchain%20mining','btc', 'cardano'],['crypto', 'cryptocurrencies','cryptocurrency', 'cryptographic', 'dash'], ['doge', 'dogecoin', 'eos','ethereum', 'hashing'],['hashocean', 'hodl', 'ico', 'iota', 'litecoin'],['localbitcoins', 'ltc', 'ltc', 'mercado', 'mining%20cryptocurrency'], ['montero', 'onecoin', 'satoshi', 'stellar', 'stratis'], ['tron', 'xlm', 'xmr', 'xrp', 'zcash']]
    for k in all_words:
        list_query_top = []
        list_query_top_value = []
        list_query_rising = []
        list_query_rising_value = []
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=k, geo='US',timeframe=timeframe)
        related_queries_dict = pytrend.related_queries()
        for f in k:
            s_top = related_queries_dict[f]['top']
            s_rising = related_queries_dict[f]['rising']
            if s_rising is not None:
                df_rising = s_rising.where(s_rising > 500)
                df_rising = df_rising.dropna()
            list_rising = df_rising['query'].tolist()
            list_rising2 = df_rising['value'].tolist()
            result_rising = zip(list_rising, list_rising2)
            if s_top is not None:
                df_top = s_top.where(s_top > 50)
                df_top = df_top.dropna()
            list_query_top = df_top['query'].tolist()
            list_query_top2 = df_top['value'].tolist()
            result_top = zip(list_query_top, list_query_top2)
            print(list(result_top))
            for j in result_top:
                url = j[0].replace(" ", "+")
                url2 = 'https://trends.'+'google.com/trends/explore?q=' + f + '+' + url + '&date={}'.format(timeframe)
                pytrend.build_payload(kw_list=[j[0]], geo='US',timeframe=timeframe)
                interest_by_region_df = pytrend.interest_by_region()
                s = interest_by_region_df[j[0]]
                df = s.where(s > 50)
                df = df.dropna()
                df = df.sort_values(ascending=False)
                interest_by_region = pd.Series(df.index.values.tolist())
                weight = pd.Series(list(df.values))
                res_df.append(pd.DataFrame({'Location': pd.Series('United States'), 'Keyword': pd.Series(f), 'Related Queries': pd.Series(j[0]), 'Percentage': pd.Series(str(j[1] * 10)), 'Interest by Region':interest_by_region, 'Weight': weight, 'Google Search Link': pd.Series('<a href="{}">{}</a>'.format(url2, url2))}))
     
        
            for j in result_rising:
                url = j[0].replace(" ", "+")
                url2 = 'https://trends.'+'google.com/trends/explore?q=' + f + '+' + url + '&date={}'.format(timeframe)
                pytrend.build_payload(kw_list=[j[0]], geo='US',timeframe='now 1-d')
                interest_by_region_df = pytrend.interest_by_region()
                s = interest_by_region_df[j[0]]
                df = s.where(s > 50)
                df = df.dropna()
                df = df.sort_values(ascending=False)
                interest_by_region = pd.Series(df.index.values.tolist())
                weight = pd.Series(list(df.values))
                res_df.append(pd.DataFrame({'Location': pd.Series('United States'), 'Keyword': pd.Series(f), 'Related Queries': pd.Series(j[0]), 'Percentage': pd.Series('Breakout'), 'Interest by Region':interest_by_region, 'Weight': weight,'Google Search Link': pd.Series('<a href="{}">{}</a>'.format(url2, url2))}))
     
        
    df = pd.concat(res_df)
    return df


def get_info_world(timeframe):
    res_df = []
    all_words = [['ada','altcoin','altcoins','bitcoin','bitconnect'],['bitminter', 'blockchain', 'blockchain%20mining','btc', 'cardano'],['crypto', 'cryptocurrencies','cryptocurrency', 'cryptographic', 'dash'], ['doge', 'dogecoin', 'eos','ethereum', 'hashing'],['hashocean', 'hodl', 'ico', 'iota', 'litecoin'],['localbitcoins', 'ltc', 'ltc', 'mercado', 'mining%20cryptocurrency'], ['montero', 'onecoin', 'satoshi', 'stellar', 'stratis'], ['tron', 'xlm', 'xmr', 'xrp', 'zcash']]
    for k in all_words:
        list_query_top = []
        list_query_top_value = []
        list_query_rising = []
        list_query_rising_value = []
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=k ,timeframe=timeframe)
        related_queries_dict = pytrend.related_queries()
        for f in k:
            s_top = related_queries_dict[f]['top']
            s_rising = related_queries_dict[f]['rising']
            if s_rising is not None:
                df_rising = s_rising.where(s_rising > 500)
                df_rising = df_rising.dropna()
            list_rising = df_rising['query'].tolist()
            list_rising2 = df_rising['value'].tolist()
            result_rising = zip(list_rising, list_rising2)
            if s_top is not None:
                df_top = s_top.where(s_top > 50)
                df_top = df_top.dropna()
            list_query_top = df_top['query'].tolist()
            list_query_top2 = df_top['value'].tolist()
            result_top = zip(list_query_top, list_query_top2)
            print(list(result_top))
            for j in result_top:
                url = j[0].replace(" ", "+")
                url2 = 'https://trends.'+'google.com/trends/explore?q=' + f + '+' + url  + '&date={}'.format(timeframe)
                pytrend.build_payload(kw_list=[j[0]],timeframe='now 1-d')
                interest_by_region_df = pytrend.interest_by_region()
                s = interest_by_region_df[j[0]]
                df = s.where(s > 50)
                df = df.dropna()
                df = df.sort_values(ascending=False)
                interest_by_region = pd.Series(df.index.values.tolist())
                weight = pd.Series(list(df.values))
                res_df.append(pd.DataFrame({'Location': pd.Series('Wordwide'), 'Keyword': pd.Series(f), 'Related Queries': pd.Series(j[0]), 'Percentage': pd.Series(str(j[1] * 10)), 'Interest by Region':interest_by_region, 'Weight': weight, 'Google Search Link': pd.Series('<a href="{}">{}</a>'.format(url2, url2))}))
     
        
            for j in result_rising:
                url = j[0].replace(" ", "+")
                url2 = 'https://trends.'+'google.com/trends/explore?q=' + f + '+' + url + '&date={}'.format(timeframe)
                pytrend.build_payload(kw_list=[j[0]],timeframe=timeframe)
                interest_by_region_df = pytrend.interest_by_region()
                s = interest_by_region_df[j[0]]
                df = s.where(s > 50)
                df = df.dropna()
                df = df.sort_values(ascending=False)
                interest_by_region = pd.Series(df.index.values.tolist())
                weight = pd.Series(list(df.values))
                res_df.append(pd.DataFrame({'Location': pd.Series('Wordwide'), 'Keyword': pd.Series(f), 'Related Queries': pd.Series(j[0]), 'Percentage': pd.Series('Breakout'), 'Interest by Region':interest_by_region, 'Weight': weight, 'Google Search Link': pd.Series('<a href="{}">{}</a>'.format(url2, url2))}))
     
        
    df = pd.concat(res_df)
    return df


app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        time_data = [{'time':'now 1-d'}, {'time':'now 4-H'}, {'time':'now 1-H'}, {'time':'now 7-d'}],
        geo_data = [{'geo':'Worldwide'}, {'geo':'United States'}]
    )
@app.route("/test" , methods=['GET', 'POST'])
def test():
    time = request.form.get('time_select')
    geo = request.form.get('geo_select')
    if geo == 'United States':
        df = get_info_usa(time) 
        df = df.fillna('')

    else:
        df = get_info_world(time)
        df = df.fillna('')
    
    return df.to_html(escape=False)

if __name__=='__main__':
    app.run(debug=True)


