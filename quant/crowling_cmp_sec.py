import qconfig
import requests
from pandas import DataFrame
 
if __name__=='__main__':
    df = DataFrame(columns=['code', 'name', 'ls', 'ms'])
    date = '20200715'
    # there is no data in the stock market closed day and before market open. 
    # weekends, Jan 1, Dec 31 etc
    
    for wics_code in qconfig.wics_mc.keys():
        response = requests.get(qconfig.wics_url(date, wics_code))
    
        if(response.status_code == 200): # request success
            json_list = response.json() # dictionary
            # response.text -> return str type
            for json in json_list['list']:
                ls = json['SEC_NM_KOR'] # Large sector
                ms = json['IDX_NM_KOR'][5:] # Medium sector
                code = json['CMP_CD'] # Company code
                name = json['CMP_KOR'] # Company korean name
                df = df.append({'code':code, 'name':name, 'ls':ls, 'ms':ms}, 
                          ignore_index=True)
        else:
            print('Error:' + response.status_code)
            print('WICS code:' + str(wics_code))