import requests



def search_for_businesses(*args, **kwargs) -> str:
    """Search for businesses in the chosen location.
    Provide 'text' arg with chosen location."""
    url: str = "https://search-maps.yandex.ru/v1/?"
    r = requests.get(url, headers = {'User-agent': 'your bot 0.1'}, data={**kwargs}).text
    # requests.post(url=url, *args, **kwargs).text
    return r



print(search_for_businesses
    (
    apikey="pdct.1.1.20220306T104924Z.984ff829c71cc5d3.9f4187e0d018ecc1ea32cf94244b1df8941f2908",
    text="Auto repair,Moscow, Smolenskaya ulitsa",
    lang="ru_RU",
    type="biz",
    verify=False
))



# requests.exceptions.SSLError: HTTPSConnectionPool(host='search-maps.yandex.ru', port=443): Max retries exceeded with url: /v1/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)')))