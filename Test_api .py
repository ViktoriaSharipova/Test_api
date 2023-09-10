import pytest
import requests
from pytest_check import check
import schema
from jsonschema import validate


    # 200 ;1
    def test_get1():
        url = 'https://reqres.in/api/users?page=2'
        response = requests.get('url')
        message = response.text
        validate(message, schema.schemaget1())


    # 200 ;2
    def test_get2():
        url = 'https://reqres.in/api/users/2'
        response = requests.get('url')
        message = response.text
        validate(message, schema.schemaget2())

    # 404 ;3
    def test_get3(self):
        url = 'https://reqres.in/api/users/23'
        response = requests.get('url')
        message = response.text
        if response.status_code == 200:
            validate(message, schema.schemaget2())
        elif response.status_code == 404:
            assert True

    # 200 ;4
    def test_get4(self):
        self.response = requests.get('https://reqres.in/api/unknown')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    # 200 ;5
    def test_get5(self):
        self.response = requests.get('https://reqres.in/api/unknown/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200

    # 404 ;6
    def test_get6(self):
        self.response = requests.get('https://reqres.in/api/unknown/23')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 404

    # 201; 7

    @pytest.mark.parametrize("name,job", [("morpheus", "leader")])
    def test_eval(self, name, job):
        url = 'https://reqres.in/api/users'
        json = {
            "name": name,
            "job": job
        }
        self.response = requests.post(url, json=json)
        assert self.response.status_code == 201

    # 200; 8

    @pytest.mark.parametrize("name,job", [("morpheus", "zion resident")])
    def test_eval(self, name, job):
        url = 'https://reqres.in/api/users/2'
        json = {
            "name": name,
            "job": job
        }
        self.response = requests.put(url, json=json)
        assert self.response.status_code == 200

    # 200 ;9

    @pytest.mark.parametrize("name,job", [("morpheus", "zion resident")])
    def test_eval(self, name, job):
        url = 'https://reqres.in/api/users/2'
        json = {
            "name": name,
            "job": job
        }
        self.response = requests.patch(url, json=json)
        assert self.response.status_code == 200

    # 204 ;10
    def test_delete10(self):
        self.response = requests.delete('https://reqres.in/api/users/2')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 204

    # 200 ; 11,12
    @pytest.mark.parametrize("email,password", [("eve.holt@reqres.in", "pistol"), ("sydney@fife", "")])
    def test_eval(self,email, password):
        url = 'https://reqres.in/api/register'
        json = {
            "email": email,
            "password": password
        }
        self.response = requests.post(url, json=json)
        assert self.response.status_code == 200

    # 400 ;13/14

    @pytest.mark.parametrize("email,password", [("eve.holt@reqres.in", "cityslicka"), ("peter@klaven", "")])
    def test_post1314(self, email, password):
        url = 'https://reqres.in/api/login'
        json = {
            "email": email,
            "password": password
        }
        self.response = requests.post(url, json=json)
        assert self.response.status_code == 200

    # 200 ;15
    def test_get15(self):
        self.response = requests.get('https://reqres.in/api/users?delay=3')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
