class DictCleaner(object):
    """
        dict cleaner features:
            recursively cut empty nested dicts
            cut every nested dict with specified fields

        usage:
            dc = DictCleaner(['field1', 'field2', ...])
            cleaned_dict = dc.clean_empty(mydict_to_be_cleaned)

    """
    # list of stop VALUES to be cut as 'key: value' pair
    # {key1: stop_value, key2: normal_value} ->  {key2: normal_value}
    stop_values = [None, '']
    # list of deprecated fields or 'path.to.field's to be cut as nested node
    # {deprec_key: value1, normal_key: value2} -> { normal_key: value2}
    deprec_fields = []

    def __init__(self, fields=[]):
        # list of deprecated fields to be cut
        self.deprec_fields = fields

    def clean_empty(self, d, path=''):
        cd = {}
        cl = []
        if not isinstance(d, (dict, list)):
            return d
        elif isinstance(d, list):
            for i in d:
                if not (i in self.stop_values):
                    r = self.clean_empty(i, path)
                    cl.append(r)

        elif isinstance(d, dict):
            for k, v in d.items():
                _path = '.'.join([path, k]).strip('.')

                if not (k in self.deprec_fields) and \
                        not any([field in _path for field in self.deprec_fields]) and \
                        not (v in self.stop_values):

                    r = self.clean_empty(v, _path)
                    if not r in self.stop_values:
                        cd[k] = r
                        # else:
                        # print('skip', k, v)
        if cd:
            return cd
        if cl:
            return cl


if __name__ == '__main__':

    sample = {
        'bid': {
            'type': 'cpm',
            'current': 60.0,
            'max': None,
            'min': None
        },
        'budget': {
            'lifetime': '',
            'daily': '6000.0'
        },
        'campaign': {
            'name': '13_10_andYandex_sport_CPM_VK_sport',
            'status': 'archived',
            'created': '2016-10-13 13:09:34'
        },
        'client': {
            'id': 2671152
        },
        'date': {
            'start': None,
            'stop': None
        },
        'network': 'mt',
        'statistics': {
            'overall': {
                'cr': None,
                'cpa': 2.3,
                'roi': 2942.51
            },
            'daily': OrderedDict([('2016-10-14', {
                'general': {
                    'spend': 2578.28
                }
            }), ('2016-10-15', {
                'general': {
                    'spend': 2487.95
                }
            }), ('2016-10-16', {
                'general': {
                    'spend': 3429.52
                }
            }), ('2016-10-17', {
                'general': {
                    'spend': 5999.98
                }
            }), ('2016-10-18', {
                'general': {
                    'spend': 6000.0
                }
            }), ('2016-10-19', {
                'general': {
                    'spend': 1135.69
                }
            }), ('2016-10-20', {
                'general': {

                }
            }), ('2016-10-21', {
                'general': {
                    'spend': 373.2
                }
            }), ('2016-10-22', {
                'general': {
                    'spend': 623.78
                }
            }), ('2016-10-25', {
                'general': {
                    'spend': 604.57
                }
            }), ('2016-10-26', {
                'general': {
                    'spend': 2339.2
                }
            }), ('2016-10-27', {
                'general': {
                    'spend': 824.95
                }
            }), ('2016-10-13', {
                'general': {
                    'spend': 2316.84
                }
            }), ('2016-11-01', {
                'pb': {
                    'g1': {
                        'count': 615
                    }
                }
            }), ('2016-12-01', {
                'pb': {
                    'g1': {
                        'count': {}
                    }
                }
            })])
        }
    }

    dc = DictCleaner(['count', 'roi'])
    empted = dc.clean_empty(sample)
