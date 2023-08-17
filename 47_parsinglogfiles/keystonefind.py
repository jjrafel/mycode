loginfail=0
with open("keystone.common.wsgi") as keyfile:
    for line in keyfile:
        if "- - - - -] Authorization" in line:
            loginfail += 1
            print(line.split(" ")[-1])

print(f"Failed logins number: {loginfail}")
