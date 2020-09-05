import requests
import json


class TokenOperation:

    def __init__(self):
        self.tenant = ''
        self.token_provider = 'https://login.microsoftonline.com/' + \
            tenant + '/oauth2/v2.0/token'
        self.scope = 'openid offline_access'
        self.grant_type = 'authorization_code'
        self.redirect_uri = 'http://localhost:4200/home'
        self.token_req_headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}

    def fetch_Access_Token(self, auth_code, client_id):
        form_encoded_body = self.create_x_www_form_urlencoded_body(
            auth_code, client_id)
        response = requests.post(
            self.token_provider, data=form_encoded_body, headers=self.token_req_headers)
        if response.status_code == 200:
            body = json.loads(response.content)
            access_token = body['access_token']
            refresh_token = body['refresh_token']
        else:
            return False

    def create_x_www_form_urlencoded_body(self, auth_code, client_id):
        return (
            'client_id={0}&code={1}&redirect_uri={2}&grant_type={3}&scope={4}'
        ).format(client_id, auth_code, self.redirect_uri, self.grant_type, self.scope)

    def generate_session(**kwargs):
        