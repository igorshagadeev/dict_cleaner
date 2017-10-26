# dict_cleaner
dict cleaner features:
    recursively cut empty nested dicts
    cut every nested dict with specified fields

usage:
    dc = DictCleaner(['field1', 'field2', ...])
    cleaned_dict = dc.clean_empty(mydict_to_be_cleaned)
    
example
{key1: stop_value,
 key2: normal_value,
 deprecated_key: value1,
 normal_key: value2}

->

{key2: normal_value,
normal_key: value2}
