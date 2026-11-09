from functools import partial


def extract_nested_value(obj, keys, default=None):
    """Идёт по цепочке ключей; если путь оборван, возвращает default."""
    current = obj
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def process_dictionary_with_config(dictionary, config):
    """Строит плоский словарь {атрибут: значение} по конфигу."""
    result = {}
    for attribute, spec in config.items():
        path, func = spec if isinstance(spec, tuple) else (spec, None)
        value = extract_nested_value(dictionary, path)
        result[attribute] = func(value) if (func and value is not None) else value
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    return [process_dictionary_with_config(d, config) for d in list_of_dicts or []]


def create_processor(config, list_processor=False):
    """Возвращает функцию с уже зашитым конфигом."""
    base = process_list_of_dicts_with_config if list_processor else process_dictionary_with_config
    return partial(base, config=config)