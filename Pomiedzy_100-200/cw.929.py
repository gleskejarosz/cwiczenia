def numUniqueEmails(emails: list) -> int:
    addresses = set()
    new_local_name = ""

    for email in emails:
        email_list = email.split("@")
        local_name = list(email_list[0])
        domain_name = email_list[1]
        for idx, elem in enumerate(local_name):
            if elem == ".":
                local_name.pop(idx)
            if elem == "+":
                local_name = local_name[:idx]
                break
        for elem in local_name:
            new_local_name += elem
        address = new_local_name + "@" + domain_name
        addresses.add(address)
        new_local_name = ""

    return len(addresses)


if __name__ == '__main__':
    assert (numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])) == 2
    assert (numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])) == 3
