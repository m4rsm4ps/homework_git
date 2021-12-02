def parse(query: str) -> dict:
    parsed = dict()
    query = query.partition('?')[-1]
    for bits in query.split('&'):
        try:
            key, val = bits.partition('=')[0], bits.partition('=')[-1]
        except ValueError:
            continue
        else:
            if key and val:
                parsed[key] = val

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


def parse_cookie(query: str) -> dict:
    parsed = dict()
    for bit in query.split(';'):
        try:
            key, val = bit.partition('=')[0], bit.partition('=')[-1]
        except ValueError:
            continue
        else:
            if key and val:
                parsed[key] = val

    return parsed


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User') == {'name': 'Dima=User'}
    assert parse_cookie('hello') == {}
    assert parse_cookie('name;age') == {}
    assert parse_cookie(';') == {}
    assert parse_cookie('=') == {}
    assert parse_cookie('=????;****') == {}
    assert parse_cookie('????=****') == {'????': '****'}
    assert parse_cookie(';Dima=name;;;;;') == {'Dima': 'name'}
    assert parse_cookie('0==0;1;;1') == {'0': '=0'}
    assert parse_cookie('=;=;=;=;=;spam=eggs') == {'spam': 'eggs'}
