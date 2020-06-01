import json

original = input('Original json file: ')
client_id = input('Client name: ')

o = json.loads(open(original, 'r').read())
o['id'] = client_id


def remove_error_info(d, lstK):
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [remove_error_info(v, lstK) for v in d]
    return {k: remove_error_info(v, lstK) for k, v in d.items()
            if k not in lstK}


r = remove_error_info(o, ['downloads'])

print('Writing to ' + client_id + '.json...')
open(client_id + '.json', 'w').write(json.dumps(r))
print('Done.')
