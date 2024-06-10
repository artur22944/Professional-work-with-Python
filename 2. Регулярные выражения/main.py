import csv
import re


def format_data(contacts_list):
    headers_list = [contacts_list[0]]

    # Редактирование столбцов с ФИО
    for i in range(1, len(contacts_list)):
        string = " ".join(contacts_list[i][:3]).strip().split(" ")
        string = [i for i in string if i]
        headers_list.append(
            [
                string[0],
                string[1],
                string[2] if len(string) > 2 else "",
                contacts_list[i][3],
                contacts_list[i][4],
                contacts_list[i][5],
                contacts_list[i][6],
            ]
        )

    # Редактирование столбца с телефонами
    phone_pattern = r"(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*([доб\.]*\s*\d{4})?\)*"
    phone_pattern_comp = re.compile(phone_pattern)

    for i in range(1, len(headers_list)):
        result_phone = phone_pattern_comp.sub(
            r"+7 (\2) \3-\4-\5 \6", headers_list[i][5]
        )
        headers_list[i][5] = result_phone

    # Устраненине дубликатов c одинаковыми ФИО
    for i in headers_list:
        last_name_i = i[0]
        first_name_i = i[1]
        surname_i = i[2]
        for j in headers_list:
            last_name_j = j[0]
            first_name_j = j[1]
            surname_j = j[2]
            if (
                last_name_i == last_name_j
                and first_name_i == first_name_j
                and (surname_i == surname_j or surname_i == "")
            ):
                if i[2] == "":
                    i[2] = j[2]
                else:
                    j[2] = i[2]
                if i[3] == "":
                    i[3] = j[3]
                else:
                    j[3] = i[3]
                if i[4] == "":
                    i[4] = j[4]
                else:
                    j[4] = i[4]
                if i[5] == "":
                    i[5] = j[5]
                else:
                    j[5] = i[5]
                if i[6] == "":
                    i[6] = j[6]
                else:
                    j[6] = i[6]
        copy_list = []
        for line in headers_list:
            if line not in copy_list:
                copy_list.append(line)
        headers_list = copy_list
    print(headers_list)
    return headers_list


if __name__ == "__main__":

    with open("phonebook_raw.csv", newline="", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    edited_list = format_data(contacts_list)

    with open("phonebook.csv", "w", newline="", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(edited_list)
