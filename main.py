import requests
from framework.config_loader import load_yaml
from framework.api_client import APIClient
from framework.test_executor import execute_tests

api_cfg = load_yaml("config/api_config.yaml")
creds = load_yaml("config/credentials.yaml")
tests = load_yaml("config/test_cases.yaml")

login_resp = requests.post(
    f"{api_cfg['base_url']}/login",
    auth=(creds["username"], creds["password"])
)

token = login_resp.json()["token"]

client = APIClient(api_cfg["base_url"], token)

execute_tests(
    client,
    api_cfg["endpoints"],
    tests["test_cases"]
)
