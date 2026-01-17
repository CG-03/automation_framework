from concurrent.futures import ThreadPoolExecutor
from tests.test_disable_virtual_service import run_test

def execute_tests(api_client, endpoints, test_cases):
    with ThreadPoolExecutor(max_workers=2) as executor:
        for tc in test_cases:
            executor.submit(run_test, api_client, endpoints, tc)
