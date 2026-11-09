from json_dict_processing import *
from laureates_configs import person_processor, process_year

assert extract_nested_value({'a': {'b': 1}}, ['a', 'b']) == 1
assert extract_nested_value({'a': {}}, ['a', 'b']) is None
assert process_year('1943-05-12') == 1943

cfg = {'x': ['a', 'b'], 'y': (['a', 'c'], int)}
assert create_processor(cfg)({'a': {'b': 5, 'c': '7'}}) == {'x': 5, 'y': 7}

raw = {'id': '745', 'knownName': {'en': 'A. Michael Spence'}, 'gender': 'male',
       'birth': {'date': '1943-11-07'},
       'nobelPrizes': [{'awardYear': '2001', 'category': {'en': 'Economic Sciences'}}]}
res = person_processor()(raw)
assert res['id'] == 745 and res['birth_year'] == 1943
assert res['prizes_relevant'][0]['award_year'] == 2001