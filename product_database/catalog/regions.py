def get_regions(data_dict):
    return [data_dict['Results'][region_data]['Name'] for region_data in data_dict['Results']]

