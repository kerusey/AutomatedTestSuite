import shodan
import json


def requestDomainInformation(host: str) -> dict:
    try:
        host = api.host(host)
    except shodan.exception.APIError:
        return {"Shodan": "The requested host is not valid or there is no information available for that IP."}
    domainInformation, products = {}, []
    headers = ['country_code', 'city', 'last_update', 'latitude', 'longitude', 'tags', 'org', 'ports', 'vulns']
    
    for header in headers:
        try:
            domainInformation[header] = host[header]
        except KeyError:
            domainInformation[header] = None
    
    for item in host['data']:
        try:
            products.append({item['product']:
                                  {
                                    "port": item['port'],
                                    "transport": item['transport'],
                                    "version": item['version']
                                  }
                             })
        except KeyError:
            continue
    
    domainInformation["products"] = products if len(products) > 0 else None
    
    return domainInformation


if __name__ == '__main__':
    api = shodan.Shodan(json.load(open("../config.json"))['shodanKey'])
    #  open("dumps.json", 'w').write(json.dumps(requestDomainInformation("host here"), indent=4))

else:
    api = shodan.Shodan(json.load(open("config.json"))['shodanKey'])