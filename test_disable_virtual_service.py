from framework.logger import log

def find_vs_by_name(vs_list, target_name):
    for vs in vs_list:
        if vs["name"] == target_name:
            return vs
    return None

def run_test(api_client, endpoints, test_case):
    log("Pre-Fetcher Stage Started")

    tenants = api_client.get(endpoints["tenants"]).json()["results"]
    vs_list = api_client.get(endpoints["virtual_services"]).json()["results"]
    ses = api_client.get(endpoints["service_engines"]).json()["results"]


    log(f"Tenants Count: {len(tenants)}")
    log(f"Virtual Services Count: {len(vs_list)}")
    log(f"Service Engines Count: {len(ses)}")

    log("Pre-Validation Stage Started")

    target_vs = find_vs_by_name(vs_list, test_case["target_vs_name"])
    assert target_vs is not None, "Target Virtual Service not found"

    vs_uuid = target_vs["uuid"]

    vs_detail = api_client.get(f"{endpoints['virtual_services']}/{vs_uuid}").json()

    assert vs_detail["enabled"] is True, "Virtual Service already disabled"

    log("Task / Trigger Stage Started")

    api_client.put(
        f"{endpoints['virtual_services']}/{vs_uuid}",
        test_case["action"]["payload"]
    )

    log("Post-Validation Stage Started")

    updated_vs = api_client.get(f"{endpoints['virtual_services']}/{vs_uuid}").json()
    assert updated_vs["enabled"] is False, "Failed to disable Virtual Service"

    log("TEST PASSED ✅")
