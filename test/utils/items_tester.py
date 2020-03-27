import pytest
import requests
import json
from typing import Any, Dict


class ItemsTester:
    def __init__(
            self,
            host: str,
            label: str,
            default_payload: Dict[str, str]
    ):
        self.host = host
        self.label = label
        self.default_payload = default_payload
        self.items = []

    def find_item(
            self,
            name
    ) -> Dict[str, Any]:
        url = self.host + "/" + self.label

        url += "?name[$like]={}".format(name)
        response = requests.request("GET", url)
        return response.json()

    def find_item_by_id(self, item_id):
        url = self.host + "/" + self.label
        url += "?id=" + str(item_id)
        response = requests.request("GET", url)
        return response.json()

    def find_item_like(self, pattern:str):
        url = self.host + "/" + self.label
        url += '?name[$like]='+pattern
        response = requests.request("GET", url)
        return response.json()

    def create_item(
            self,
            name: str,
            payload: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        if payload is None:
            payload = self.default_payload
        url = self.host + "/" + self.label
        payload['name'] = name
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
        self.items.append(response['id'])
        return response

    def delete_item_by_id(self, item_id: int):
        url = self.host + "/" + self.label + '?id=' + str(item_id)
        requests.request("DELETE", url)

    def delete_all_items(self):
        for item_id in self.items:
            url = self.host + "/" + self.label + '?id=' + str(item_id)
            requests.request("DELETE", url)
