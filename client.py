
import my_api


if __name__ == "__main__":
    print(my_api.coalesce_providers(member_id = "alice"))
    print(my_api.coalesce_providers(member_id = "alice", strategy = "maximum"))
    print(my_api.coalesce_providers(member_id = "bob", strategy = "minimum"))
    print(my_api.coalesce_providers(member_id = "bob", strategy = "majority-vote"))

