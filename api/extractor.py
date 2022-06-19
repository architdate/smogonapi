import requests, json

def get_dex_settings(url):
    r = requests.get(url, timeout=90)
    j = r.text.split('dexSettings = ')[1].split('</script>')[0].strip()
    data = json.loads(j)
    return data

def pokemon_data(url):
    data = get_dex_settings(url)
    return data['injectRpcs'][-1][-1]