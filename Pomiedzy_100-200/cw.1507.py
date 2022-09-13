def reformatDate(date: str) -> str:
    date_list = date.split()
    month_dict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = date_list[0][:-2]
    if len(date) == 1:
        date = "0" + date

    new_format = f"{date_list[2]}-{month_dict[date_list[1]]}-{date}"

    return new_format


if __name__ == '__main__':
    assert (reformatDate("20th Oct 2052")) == "2052-10-20"
    assert (reformatDate("6th Jun 1933")) == "1933-06-06"
    assert (reformatDate("26th May 1960")) == "1960-05-26"
