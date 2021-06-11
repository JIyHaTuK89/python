# вроде все сделал, по крайней мере что явно требовали в условии. Надеюсь выгружать обратно json-объект не подразумевалось
import json

with open("text_7.txt", "r", encoding="utf-8") as f:
    profit_list = []
    companies_info = [{}, {}]
    successful_company_amount = 0
    string_number = 0
    for string in f:
        string_number += 1
        string_as_list = string.split()
        company_name = f"{string_as_list[1]} {string_as_list[0]}"
        income = string_as_list[2]
        costs = string_as_list[3]
        profit = float(string_as_list[2]) - float(string_as_list[3])
        companies_info[0][company_name] = profit
        if profit <= 0:
            continue
        else:
            profit_list.append(profit)
            successful_company_amount += 1
    average_profit = sum(profit_list) / successful_company_amount
    companies_info[1][
        "average_profit"] = average_profit  # здесь точно не знаю, с учетом фирмы с убытками или без, сделал без
    print(f"Средняя выручка успешных компаний: {average_profit}")
    print(companies_info)
    with open("text_7.json", "w", encoding="utf-8") as f2:
        json.dump(companies_info, f2)
