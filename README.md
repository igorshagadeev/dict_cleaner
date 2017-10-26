# dict_cleaner
dict cleaner features:<br />
    recursively cut empty nested dicts<br />
    cut every nested dict with specified fields<br />

usage:
    dc = DictCleaner(['field1', 'field2', ...])<br />
    cleaned_dict = dc.clean_empty(mydict_to_be_cleaned)<br />
    
example<br />
{key1: stop_value,<br />
 key2: normal_value,<br />
 deprecated_key: value1,<br />
 normal_key: value2}<br />
<br />
->
<br />
{key2: normal_value,<br />
normal_key: value2}<br />
