import casbin
e = casbin.Enforcer("./model.conf", "./policy.csv")

def test_permission():

    sub = "b8b1294c-04b2-4245-9d4d-0ac60a7804b7"  # the user that wants to access a resource.
    obj = "3f70632a-2168-11ec-9621-0242ac130002"  # the resource that is going to be accessed.
    act = "read"  # the operation that the user performs on the resource.
    # e.add_policy("bob", "data2", "read")
    # e.update_policy(["bob", "data2", "read"], ["kelly", "data2", "read"])
    # e.remove_policy(["kelly", "data2", "read"])

    print(f'User, {sub} gets the permissions', e.get_permissions_for_user(sub))
    print(f'User, {sub} gets the permissions for resource {obj}', e.get_filtered_policy(0, sub, obj))

    if e.enforce(sub, obj, act):
        print(f'Hi, {sub} is authorized to {act} resource {obj}')

        pass
    else:
        print(f'Hi, {sub} is not authorized to {act} resource {obj}')
        pass


if __name__ == '__main__':
    test_permission()