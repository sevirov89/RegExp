import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Задача 1
for row in contacts_list[1:]:
    full_name = " ".join(row[:2]).strip()
    parts = full_name.split(" ")
    if len(parts) >= 1:
        row[0] = parts[0]
    if len(parts) >= 2:
        row[1] = parts[1]
    if len(parts) >= 3:
        row[2] = parts[2]

# Задача 2
def format_phone(phone):
    if not phone:
        return ""
    extension_match = re.search(r'доб\.?\s*(\d+)', phone, re.IGNORECASE)
    extension = extension_match.group(1) if extension_match else None
    if extension:
        phone = re.sub(r'доб\.?\s*\d+', '', phone, flags=re.IGNORECASE).strip()
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 11:
        formatted_phone = f"+7({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:]}"
    elif len(digits) == 10:
        formatted_phone = f"+7({digits[0:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    else:
        formatted_phone = phone
    if extension:
        formatted_phone += f" доб.{extension}"
    return formatted_phone
for row in contacts_list[1:]:
    row[5] = format_phone(row[5])

# Задача 3
general_dict = {}
for row in contacts_list[1:]:
    key = (row[0], row[1])
    if key in general_dict:
        existing_row = general_dict[key]
        for i in range(2, len(row)):
            if not existing_row[i] and row[i]:
                existing_row[i] = row[i]
    else:
        general_dict[key] = row
result = [contacts_list[0]] + list(general_dict.values())

# Запись файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result)