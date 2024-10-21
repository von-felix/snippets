import pandas as pd

def create_dataframe(in_dict):
    
    map_dict = {}
    
    # calculate headers
    for e in in_dict:
        for i in in_dict[e]:
            map_dict.update({i: []})
    
    
    for e in in_dict:
        data = in_dict[e]
        for i in data: 
            loc_list = map_dict[i]
            loc_list.append(data[i])
            map_dict[i] = loc_list
    
    return pd.DataFrame(map_dict)

def join_data(df1, df2, key_alias, join_type):
    # using merge function by setting how='inner' 
    output1 = pd.merge(df1, 
                       df2,  
                        on=key_alias,  
                        how=join_type)

    return output1

if __name__ == "__main__":

    dict1 = {
        'host1': {'hostname': 'host1', 'ip': '192.168.1.1', 'enabled': True},
        'host2': {'hostname': 'host2', 'ip': '192.168.1.2', 'enabled': False},
        'host3': {'hostname': 'host3', 'ip': '192.168.1.3', 'enabled': False},
        'host4': {'hostname': 'host4', 'ip': '192.168.1.3', 'enabled': False},
        'host5': {'hostname': 'host5', 'ip': '192.168.1.3', 'enabled': False},
        }

    dict2 = {
        'host1': {'hostname': 'host1', 'install_date': '2024-08-31', 'os': 'Windows'},
        'host2': {'hostname': 'host2', 'os': 'Windows','install_date': 'Calib-date-2024-08-31'},
        'host5': {'hostname': 'host5', 'install_date': '2024-05-31', 'os': 'Linux'},
        }

    data1 = create_dataframe(dict1)
    data2 = create_dataframe(dict2)
    
    output1 = join_data(data1, data2, 'hostname', 'outer')

    # generate a final joined dictionary
    output2 = output1.to_dict('records')

    with pd.ExcelWriter('output.xlsx', engine='openpyxl', mode='a') as writer:  

        output1.to_excel(writer, index=False, sheet_name='merged_data2')

    print(f'Process completed.')