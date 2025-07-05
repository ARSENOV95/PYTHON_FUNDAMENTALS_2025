company_ids = {}

while (company_entry := input()) != "End":
    company, id_ = company_entry.split(" -> ")

    if company not in company_ids.keys():
        company_ids[company] = []

    if id_ not in company_ids[company]:
        company_ids[company].append(id_)

print(company_ids)