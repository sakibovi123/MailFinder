from linkedin import linkedin

API_KEY = '866i0ftyjtp1d9'
API_SECRET = 'U4UblCcylJWnNRNs'
RETURN_URL = 'http://127.0.0.1:8000'

authentication = linkedin.LinkedInAuthentication(
    API_KEY,
    API_SECRET,
    RETURN_URL,
    linkedin.PERMISSIONS.enums.values()
)

print(authentication.authorization_url)

