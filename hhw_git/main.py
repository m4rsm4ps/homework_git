def parse(query: str) -> dict:
    parsed = {}
    if '?' in query and not query.endswith('?'):
        toparse = query[query.find('?') + 1:]
        items = toparse.strip('&').split('&')
        for i in items:
            key, val = i.split("=")
            parsed[key] = val

    return parsed


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

