def get_value(data, key, default, lookup=None, mapper=None):
    return_value = data.get(key, default)
    if lookup and return_value in lookup:
        return_value = lookup[return_value]
    if mapper:
        return_value = mapper(return_value)
    return return_value

def ftp_file_prefix(namespace):
    return ".".join(namespace.split(".")[:-1]) + '.ftp'

def string_to_bool(string):
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')

def config_from_dict(dict):
    namespace = dict['Namespace']
    return (dict['Airflow DAG'],
            {
                "earliest_available_delta_days": 0,
                "lif_encoding": 'json',
                "earliest_available_time": get_value(dict, 'Available Start Time', '07:00'),
                "latest_available_time": get_value(dict, 'Available End Time', '08:00'),
                "require_schema_match": get_value(dict, 'Requires Schema Match', 'True', mapper=string_to_bool),
                "schedule_interval": get_value(dict, 'Schedule', '1 7 * * *'),
                "delta_days": get_value(dict, 'Delta Days', 'DAY_BEFORE', lookup=DeltaDays),
                "ftp_file_wildcard": get_value(dict, 'File Naming Pattern', None),
                "ftp_file_prefix": get_value(dict, 'FTP File Prefix', ftp_file_prefix(namespace)),
                "namespace": namespace
            })
