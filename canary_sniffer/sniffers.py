import requests
from flask import current_app


def _get_nested_dictionary_value(data, keys):
    current_dict_layer = data
    for key in keys:
        if current_dict_layer is None:
            break
        else:
            current_dict_layer = current_dict_layer.get(key)

    return current_dict_layer


class BaseSniffer:
    domain_name = ""
    mock_domain_name = ""
    protocol = ""

    def _build_base_url(self):
        return self.protocol + "://" + self._get_domain_name()

    def _get_additional_request_headers(self):
        if current_app.config["ENV"] == "production":
            return None
        else:
            return {"x-api-key": current_app.config["CANARYSNIFFER_API_KEY"]}

    def _get_domain_name(self):
        if current_app.config["ENV"] == "production":
            return self.domain_name
        else:
            return self.mock_domain_name

    def _send_get_request(self, url, params=None):
        raise NotImplementedError

    def has_septic(self, address, zipcode):
        raise NotImplementedError


class CanarySniffer(BaseSniffer):
    domain_name = "api.housecanary.com"
    mock_domain_name = "9afd7477-dbac-4ce7-98fc-db92448f520a.mock.pstmn.io"
    property_details_path = "/v2/property/details"
    protocol = "https"

    def _send_get_request(self, url, params=None):
        return requests.get(url,
                            params=params,
                            auth=(current_app.config["HOUSECANARY_MOCK_API_USER"],
                                  current_app.config["HOUSECANARY_MOCK_API_PASS"]),
                            headers=self._get_additional_request_headers())

    def has_septic(self, address, zipcode):
        url = self._build_base_url() + self.property_details_path

        params = {"address": address,
                  "zipcode": zipcode}

        response = self._send_get_request(url, params)

        if response.ok:
            value = _get_nested_dictionary_value(response.json(),
                                                 ["property/details", "result", "property", "sewer"])
            if type(value) is str:
                return value.lower() == "septic"
        else:
            # Handle HouseCanary api errors here.
            pass

        return "unknown"
