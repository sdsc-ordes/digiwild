from requests_oauthlib import OAuth1Session
from typing import Optional, Dict, Any, Tuple, Union, List

class APIRequester(object):
    """Class for making API requests"""

    def __init__(
        self,
        consumer_key: Optional[str] = None,
        consumer_secret: Optional[str] = None,
        user_email: Optional[str] = None,
        user_pw: Optional[str] = None,
        api_base: Optional[str] = None,
    ) -> None:
        """API requester constructor
        :param consumer_key: Optional Consumer Key, overrides field from ornitho module (ornitho.consumer_key)
        :param consumer_secret: Optional Consumer Secret, overrides field from ornitho module (ornitho.consumer_secret)
        :param user_email: Optional User Mail, overrides field from ornitho module (ornitho.user_email)
        :param user_pw: Optional User Password, overrides field from ornitho module (ornitho.user_pw)
        :param api_base: Optional API base url, overrides field from ornitho module (ornitho.api_base)
        :type consumer_key: Optional[str]
        :type consumer_secret: Optional[str]
        :type user_email: Optional[str]
        :type user_pw: Optional[str]
        :type api_base: Optional[str]
        """
        self.consumer_key: Optional[str] = consumer_key
        self.consumer_secret: Optional[str] = consumer_secret
        self.user_email: Optional[str] = user_email
        self.user_pw: Optional[str] = user_pw
        self.api_base: Optional[str] = api_base
        if not self.consumer_key:
            raise RuntimeError("consumer_key missing!")
        if not self.consumer_secret:
            raise RuntimeError("consumer_secret missing!")
        if not self.user_email:
            raise RuntimeError("user_email missing!")
        if not self.user_pw:
            raise RuntimeError("user_pw missing!")
        if not self.api_base:
            raise RuntimeError("api_base missing!")

        # Initialize OAuth1 session
        self.session = OAuth1Session(
            client_key=self.consumer_key,
            client_secret=self.consumer_secret
        )

    def __enter__(self):
        """Used by a with-statement"""
        return self

    def __exit__(self, *args):
        """Used by a with-statement"""
        self.close()

    def close(self):
        """Close an OAuth1 Session"""
        self.session.close()

    def request(
        self,
        method: str,
        endpoint: str,
        pagination_key: Optional[str] = None,
        short_version: bool = False,
        request_all: bool = False,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        retries: int = 0,
    ) -> Tuple[Union[bytes, List[Dict[str, str]]], Optional[str]]:
        """Make requests to the API
        If request_all ist set, several requests calls to the API can be made, until all data is retrieved. Else a
        pagination key will be returned, which can be used to get the next data set.
        :param method: HTTP Method e.g. 'GET'
        :param endpoint: API endpoint to call
        :param pagination_key: Additional pagination key, to get the next page
        :param short_version: Indicates, if a short version with foreign keys should be returned by the API.
            Default: 'False'
        :param request_all:  Indicates, if all pages should be returned. May result in many API calls. Default: 'False'
        :param params: Additional URL parameters.
        :param body: Request body
        :param retries: Indicates how many retries should be performed
        :type method: str
        :type endpoint: str
        :type pagination_key: str
        :type short_version: bool
        :type request_all: bool
        :type params: Dict[str, Any]
        :type body: Dict[str, Any]
        :type retries: int
        :return: Tuple of raw data list and pagination key
        :rtype: Tuple[List[Dict[str, str]], Optional[str]]
        """
        url = f"{self.api_base}{endpoint}"
        params = params or {}
        params.update({'user_email': self.user_email, 'user_pw': self.user_pw})
        
        for attempt in range(retries + 1):
            response = self.session.request(method, url, params=params, json=body)
            if response.status_code == 200:
                try:
                    return response.json(), None
                except ValueError:
                    return response.content, None
            elif attempt < retries:
                continue
            else:
                response.raise_for_status()
        
        return None, None

