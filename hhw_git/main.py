def parse(query: str) -> dict:
    parsed = {}
    query = query.partition('?')[-1]
    for bits in query.split('&'):
        try:
            key, lol, val = bits.partition("=")
        except ValueError:
            continue
        else:
            if key and val: parsed[key] = val
    return parsed


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?me=f*rr*t=fe??et&color=?') == {'me': 'f*rr*t=fe??et', 'color': '?'}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=Dima==Dima') == {'name': 'Dima==Dima'}
    assert parse('https://example.com/path/to/page??=?') == {'?': '?'}
    assert parse('https://example.com/path/to/page?=========3') == {}
    assert parse('https://example.com/path/to/page?name=') == {}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?=&=') == {}
    assert parse('https://example.com/path/to/page?&&&&&&&&&&&&&&&&&&&&&&') == {}
    assert parse('http://example.com/path/to/page?zd@røväzæbáł') == {}
    assert parse('') == {}
