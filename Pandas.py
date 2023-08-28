import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    cond1 = world['area'] >= 3000000
    cond2 = world['population'] >= 25000000
    world = world[cond1 | cond2]
    return world[['name', 'population', 'area']]


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    cond1 = products["low_fats"] == "Y"
    cond2 = products["recyclable"] == "Y"
    products = products[cond1 & cond2]
    return products[["product_id"]]


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_vs_orders = customers[~customers["id"].isin(orders["customerId"])]
    customers_vs_orders = customers_vs_orders.rename(columns={"name": "Customers"})
    return customers_vs_orders[["Customers"]]


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    cond = views["author_id"] == views["viewer_id"]
    views = views[cond]
    views = views[["author_id"]]
    views = views.rename(columns={"author_id": "id"}).drop_duplicates().sort_values(by="id")
    return views


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_df = tweets.where(tweets["content"].str.len() > 15).dropna()
    invalid_df = invalid_df[["tweet_id"]]
    return invalid_df


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    cond1 = employees["employee_id"] % 2 == 1
    cond2 = employees["name"].str.startswith("M")
    employees["bonus"] = employees["salary"]
    employees[~cond1 | cond2] = 0
    return employees[["employee_id", "bonus"]].sort_values(by="employee_id")


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    to_test = r'^[a-zA-Z][a-zA-Z\d_.-]*@leetcode\.com$'
    # a-z lower character
    # A-Z upper character
    # ^[a-zA-Z] starts with letter
    # /d  digit
    # * can be repeated, place after
    # [a-zA-Z\d_.-] list of matching characters
    # $ position at the end of string
    # leetcode\.com before dot place \
    cond = users["mail"].str.contains(to_test)
    users = users[cond]
    return users


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    to_test1 = r' DIAB1'
    to_test2 = r'^DIAB1'
    cond1 = patients["conditions"].str.contains(to_test1)
    cond2 = patients["conditions"].str.contains(to_test2)
    patients = patients[cond1 | cond2]
    return patients


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    store1 = products.pivot_table(index="product_id", values="store1").rename(columns={"store1": "price"})
    store1["store"] = "store1"
    store1.reset_index(inplace=True)
    store2 = products.pivot_table(index="product_id", values="store2").rename(columns={"store2": "price"})
    store2["store"] = "store2"
    store2.reset_index(inplace=True)
    store3 = products.pivot_table(index="product_id", values="store3").rename(columns={"store3": "price"})
    store3["store"] = "store3"
    store3.reset_index(inplace=True)
    return pd.concat([store1, store2, store3])[["product_id", "store", "price"]]


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    cond1 = store["amount"] > 500
    qty = store[cond1]["customer_id"].nunique()
    return pd.DataFrame({"rich_count": [qty]})


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    cond = delivery["order_date"] == delivery["customer_pref_delivery_date"]
    immediate = delivery[cond]
    calc = round((len(immediate) / len(delivery)) * 100, 2)
    return pd.DataFrame({"immediate_percentage": [calc]})


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts["income"] < 20000]
    cond1 = accounts["income"] <= 50000
    cond2 = accounts["income"] >= 20000
    average_salary = accounts[cond1 & cond2]
    high_salary = accounts[accounts["income"] > 50000]
    return pd.DataFrame({"category": ["Low Salary", "Average Salary", "High Salary"],
                         "accounts_count": [len(low_salary), len(average_salary), len(high_salary)]})


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[["score", "rank"]].sort_values(by="rank")


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    employees.rename(columns={"event_day": "day"}, inplace=True)
    employees = employees.groupby(by=["day", "emp_id"]).agg(func="sum")
    employees.reset_index(inplace=True)
    return employees[["day", "emp_id", "total_time"]]


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.rename(columns={"event_date": "first_login"}, inplace=True)
    first_activity = activity.groupby(by="player_id", as_index=False).min()
    return first_activity[["player_id", "first_login"]]


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby(by="class", as_index=False).count()
    moreThan5Student = courses[courses["student"] >= 5]
    return moreThan5Student[["class"]]


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby(by="customer_number", as_index=False).count()
    orders.sort_values(by="order_number", ascending=False, inplace=True)
    if len(orders) > 0:
        max_qty = orders["customer_number"].iloc[0]
        return pd.DataFrame({"customer_number": [max_qty]})
    else:
        return orders[["customer_number"]]


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    different_sold = activities.groupby("sell_date").agg(num_sold=("product", "nunique"),
                                              products=(
                                              "product", lambda x: ','.join(sorted(x.unique())))).reset_index()

    return different_sold


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_lp = daily_sales.groupby(["date_id", "make_name"]).agg(unique_leads=("lead_id", "nunique"),
                                                                 unique_partners=("partner_id", "nunique")).reset_index()
    return daily_lp


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cooperating = actor_director.groupby(["actor_id", "director_id"]).agg(qty=("actor_id", "count")).reset_index()
    return cooperating[["actor_id", "director_id"]][cooperating["qty"] >= 3]


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    empl_merged = pd.merge(employees, employee_uni, how="left", on="id")
    return empl_merged[["unique_id", "name"]]


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by="user_id")


def sales_person1(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_table1 = pd.merge(orders, company, how="left", on="com_id")
    cond1 = merged_table1["name"] == "RED"
    merged_table1 = merged_table1[cond1]
    merged_table2 = pd.merge(merged_table1, sales_person, how="right", on="sales_id")
    cond2 = merged_table2["order_id"].isna()
    result = pd.DataFrame(merged_table2[cond2]["name_y"]).rename(columns={"name_y": "name"})
    return result


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    grouped_employee = employee.groupby(by="salary", as_index=False).count()
    sorted_employee_df = grouped_employee.sort_values(ascending=False, by="salary")
    col_name = "getNthHighestSalary("+str(N)+")"
    if len(sorted_employee_df) <= N - 1:
        return pd.DataFrame({col_name: [None]})
    else:
        nth_highest_salary = sorted_employee_df["salary"].iloc[N - 1]
        return pd.DataFrame({col_name: [nth_highest_salary]})


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    grouped_employee = employee.groupby(by="salary", as_index=False).count()
    sorted_employee_df = grouped_employee["salary"].sort_values(ascending=False)
    if len(sorted_employee_df) <= 1:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        second_highest_salary = sorted_employee_df.iloc[1]
        return pd.DataFrame({"SecondHighestSalary": [second_highest_salary]})


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_table = employee2.merge(department, left_on="departmentId", right_on="id", suffixes=("", "_x"))
    merged_table.drop(columns=["id_x", "departmentId", "id"], inplace=True)
    max_salary = merged_table.groupby(by="name_x")["salary"].transform("max")
    cond = merged_table["salary"] == max_salary
    max_salary_table = merged_table[cond]
    return max_salary_table[["name_x", "name", "salary"]].rename(columns={"name_x": "Department", "name": "Employee", "salary": "Salary"})


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    unique_subjects = teacher.groupby(by="teacher_id", as_index=False).agg(cnt=("subject_id", "nunique"))
    return unique_subjects


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee_agg = employee.groupby(by="managerId").agg(qty_reports=("name", "count")).reset_index()
    merged_table = employee_agg.merge(employee, left_on="managerId", right_on="id")
    cond1 = merged_table["qty_reports"] >= 5
    cond2 = merged_table["managerId_x"] == merged_table["id"]
    return merged_table[["name"]][cond1 & cond2]


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged_table1 = pd.merge(students, subjects, how='cross')
    merged_table2 = pd.merge(merged_table1, examinations, on=["student_id", "subject_name"], how="left", indicator=True)
    merged_table2['_merge'] = merged_table2['_merge'].map({'left_only': 0, 'both': 1})
    merged_table2 = merged_table2.groupby(['student_id', 'student_name', 'subject_name']
                                          )['_merge'].sum().reset_index(name='attended_exams')
    return merged_table2.sort_values(by=['student_id', 'subject_name'])


if __name__ == '__main__':
    print("Leetcode 1280")
    students = pd.DataFrame(
        {"student_id": [1, 2, 13, 6],
         "student_name": ["Alice", "Bob", "John", "Alex"]}
    )
    subjects = pd.DataFrame(
        {"subject_name": ["Math", "Physics", "Programming"]}
    )
    examinations = pd.DataFrame(
        {"student_id": [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
         "subject_name": ["Math", "Physics", "Programming", "Programming", "Physics", "Math", "Math", "Programming",
                          "Physics", "Math", "Math"]}
    )
    print(students_and_examinations(students=students, subjects=subjects, examinations=examinations))
    print("Leetcode 570")
    employee5 = pd.DataFrame(
        {"id": [101, 102, 103, 104, 105, 106],
         "name": ["John", "Dan", "James", "Amy", "Anne", "Ron"],
         "department": ["A", "A", "A", "A", "A", "B"],
         "managerId": [None, 101, 101, 101, 101, 101]}
    )
    employee6 = pd.DataFrame(
        {"id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
         "name": ["John", "Dan", "James", "Amy", "Anne", "Ron", "Tom", "Tommy", "Peter", "Dong", "DIDI"],
         "department": ["A", "A", "A", "A", "A", "B", "A", "A", "C", "A", "D"],
         "managerId": [None, 101, 101, 101, 101, 101, 102, 102, 102, 102, 102]}
    )
    print(find_managers(employee=employee5))
    print(find_managers(employee=employee6))
    print("Leetcode 2356")
    teacher = pd.DataFrame(
        {"teacher_id": [1, 1, 1, 2, 2, 2, 2],
         "subject_id": [2, 2, 3, 1, 2, 3, 4],
         "dept_id": [3, 4, 3, 1, 1, 1, 1]}
    )
    print(count_unique_subjects(teacher=teacher))
    print("Leetcode 184")
    department = pd.DataFrame(
        {"id": [1, 2],
         "name": ["IT", "Sales"]}
    )
    employee2 = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5],
         "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
         "salary": [70000, 90000, 80000, 60000, 90000],
         "departmentId": [1, 1, 2, 2, 1]}
    )
    print(department_highest_salary(employee=employee2, department=department))
    print("Leetcode 196")
    person = pd.DataFrame(
        {"id": [1, 2, 3],
         "email": ["john@example.com", "bob@example.com", "john@example.com"]}
    )
    person1 = pd.DataFrame(
        {"id": [],
         "email": []}
    )
    print(delete_duplicate_emails(person=person))
    print(delete_duplicate_emails(person=person1))
    print("Leetcode 177")
    employee = pd.DataFrame(
        {"id": [1, 2, 3],
         "salary": [100, 200, 300]}
    )
    employee4 = pd.DataFrame(
        {"id": [1, 2],
         "salary": [100, 100]}
    )
    print(nth_highest_salary(employee=employee, N=2))
    print(nth_highest_salary(employee=employee4, N=2))
    print("Leetcode 176")
    print(second_highest_salary(employee=employee))
    print(second_highest_salary(employee=employee2))
    print("Leetcode 607")
    sales_person = pd.DataFrame(
        {"sales_id": [1, 2, 3, 4, 5],
         "name": ["John", "Amy", "Mark", "Pam", "Alex"],
         "salary": [100000, 12000, 65000, 25000, 5000],
         "commission_rate": [6, 5, 12, 25, 10],
         "hire_date": ["4/1/2006", "5/1/2010", "12/25/2008", "1/1/2005", "2/3/2007"]}
    )
    company = pd.DataFrame(
        {"com_id": [1, 2, 3, 4],
         "name": ["RED", "ORANGE", "YELLOW", "GREEN"],
         "city": ["Boston", "New York", "Boston", "Austin"]}
    )
    orders = pd.DataFrame(
        {"order_id": [1, 2, 3, 4],
         "order_date": ["1/1/2014", "2/1/2014", "3/1/2014", "4/1/2014"],
         "com_id": [3, 4, 1, 1],
         "sales_id": [4, 5, 1, 4],
         "amount": [10000, 5000, 50000, 25000]}
    )
    print(sales_person1(sales_person=sales_person, company=company, orders=orders))
    print("Leetcode 1667")
    users = pd.DataFrame(
        {"user_id": [1, 2],
         "name": ["aLice", "bOB"]}
    )
    print(fix_names(users=users))
    print("Leetcode 1667")
    users1 = pd.DataFrame(
        {"user_id": [593, 944, 222],
         "name": ["DAlia", "FREIda", "MaRRy aNN"]}
    )
    print(fix_names(users=users1))
    print("Leetcode 1378")
    employees = pd.DataFrame(
        {"id": [1, 7, 11, 90, 3],
         "name": ["Alice", "Bob", "Meir", "Winston", "Jonathan"]}
    )
    employee_uni = pd.DataFrame(
        {"id": [3, 11, 90],
         "unique_id": [1, 2, 3]}
    )
    print(replace_employee_id(employees=employees, employee_uni=employee_uni))
    print("Leetcode 1050")
    actor_director = pd.DataFrame(
        {"actor_id": [1, 1, 1, 1, 1, 2, 2],
         "director_id": [1, 1, 1, 2, 2, 1, 1],
         "timestamp": [0, 1, 2, 3, 4, 5, 6]}
    )
    print(actors_and_directors(actor_director=actor_director))
    print("Leetcode 1693")
    daily_sales = pd.DataFrame(
        {"date_id": ["2020-12-8", "2020-12-8", "2020-12-8", "2020-12-7", "2020-12-7", "2020-12-8", "2020-12-8",
                    "2020-12-7", "2020-12-7", "2020-12-7"],
         "make_name": ["toyota", "toyota", "toyota", "toyota", "toyota", "honda", "honda", "honda", "honda", "honda"],
         "lead_id": [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
         "partner_id": [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]}
    )
    print(daily_leads_and_partners(daily_sales=daily_sales))
    print("Leetcode 1484")
    activities = pd.DataFrame(
        {"sell_date": ["2020-05-30", "2020-06-01", "2020-06-02", "2020-05-30", "2020-06-01", "2020-06-02", "2020-05-30"],
         "product": ["Headphone", "Pencil", "Mask", "Basketball", "Bible", "Mask", "T-Shirt"]}
    )
    print(categorize_products(activities=activities))
    print("Leetcode 586")
    orders1 = pd.DataFrame(
        {"order_number": [1, 2, 3, 4],
         "customer_number": [1, 2, 3, 3]}
    )
    print(largest_orders(orders=orders1))
    orders2 = pd.DataFrame(
        {"order_number": [],
         "customer_number": []}
    )
    print(largest_orders(orders=orders2))
    print("Leetcode 596")
    courses = pd.DataFrame(
        {"student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
         "class": ["Math", "English", "Math", "Biology", "Math", "Computer", "Math", "Math", "Math"]}
    )
    print(find_classes(courses=courses))
    print("Leetcode 511")
    activity = pd.DataFrame(
        {"player_id": [1, 1, 2, 3, 3],
         "device_id": [2, 2, 3, 1, 4],
         "event_date": ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"],
         "games_played": [5, 6, 1, 0, 5]}
    )
    print(game_analysis(activity=activity))
    print("Leetcode 1741")
    employees1 = pd.DataFrame(
        {"emp_id": [1, 1, 1, 2, 2],
         "event_day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"],
         "in_time": [4, 55, 1, 3, 47],
         "out_time": [32, 200, 42, 33, 74]}
    )
    print(total_time(employees=employees1))
    print("Leetcode 178")
    scores = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5, 6],
         "score": [3.5, 3.65, 4.00, 3.85, 4.00, 3.65]}
    )
    print(order_scores(scores=scores))
    print("Leetcode 1907")
    accounts = pd.DataFrame(
        {"accounts_id": [3, 2, 8, 6],
         "income": [108939, 12747, 87709, 91796]}
    )
    print(count_salary_categories(accounts=accounts))
    print("Leetcode 1173")
    delivery = pd.DataFrame(
        {"delivery_id": [1, 2, 3, 4, 5, 6],
         "customer_id": [1, 5, 1, 3, 4, 2],
         "order_date": ["2019-08-01", "2019-08-02", "2019-08-11", "2019-08-24", "2019-08-21", "2019-08-11"],
         "customer_pref_delivery_date": ["2019-08-02", "2019-08-02", "2019-08-11", "2019-08-26", "2019-08-22",
                                         "2019-08-13"]}
    )
    print(food_delivery(delivery=delivery))
    print("Leetcode 2082")
    store = pd.DataFrame(
        {"bill_id": [6, 8, 4, 11, 13],
         "customer_id": [1, 1, 2, 3, 3],
         "amount": [549, 834, 394, 657, 257]}
    )
    print(count_rich_customers(store=store))
    print("Leetcode 1795")
    products = pd.DataFrame(
        {"product_id": [0, 1],
         "store1": [95, 70],
         "store2": [100, None],
         "store3": [105, 80]}
    )
    print(rearrange_products_table(products=products))
    print("Leetcode 1527")
    patients = pd.DataFrame(
        {"patient_id": [1, 2, 3, 4, 5],
         "patient_name": ["Daniel", "Alice", "Bob", "George", "Alain"],
         "conditions": ["YFEV COUGH", "", "DIAB100 MYOP", "ACNE DIAB100", "DIAB201"]}
    )
    print(find_patients(patients=patients))
    print("Leetcode 1517")
    users2 = pd.DataFrame(
        {"user_id": [1, 2, 3, 4, 5, 6, 7],
         "name": ["Winston", "Jonathan", "Annabelle", "Sally", "Marwan", "David", "Shapiro"],
         "mail": ["winston@leetcode.com", "jonathanisgreat", "bella-@leetcode.com", "sally.come@leetcode.com",
                  "quarz#2020@leetcode.com", "david69@gmail.com", ".shapo@leetcode.com"]}
    )
    print(valid_emails(users=users2))
    print("Leetcode 1873")
    employees3 = pd.DataFrame(
        {"employee_id": [2, 3, 7, 8, 9],
         "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
         "salary": [3000, 3800, 7400, 6100, 7700]}
    )
    print(calculate_special_bonus(employees=employees3))
    print("Leetcode 1683")
    tweets = pd.DataFrame(
        {"tweet_id": [1, 2],
         "content": ["Vote for Biden", "Let us make America great again!"]}
    )
    print(invalid_tweets(tweets=tweets))
    print("Leetcode 595")
    world = pd.DataFrame(
        {"name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
         "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
         "area": [652230, 28748, 2381741, 468, 1246700],
         "population": [25500100, 2831741, 37100000, 78115, 20609294],
         "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]}
    )
    print(big_countries(world=world))
    print("Leetcode 1757")
    products2 = pd.DataFrame(
        {"product_id": [0, 1, 2, 3, 4],
         "low_fats": ["Y", "Y", "N", "Y", "N"],
         "recyclable": ["N", "Y", "Y", "Y", "N"]}
    )
    print(find_products(products=products2))
    print("Leetcode 183")
    customers = pd.DataFrame(
        {"id": [1, 2, 3, 4],
         "name": ["Joe", "Henry", "Sam", "Max"]}
    )
    orders3 = pd.DataFrame(
        {"id": [1, 2],
         "customerId": [3, 1]}
    )
    print(find_customers(customers=customers, orders=orders3))
    print("Leetcode 1148")
    views = pd.DataFrame(
        {"article_id": [1, 1, 2, 2, 4, 3, 3],
         "author_id": [3, 3, 7, 7, 7, 4, 4],
         "viewer_id": [5, 6, 7, 6, 1, 4, 4],
         "view_date": ["2019-08-01", "2019-08-02", "2019-08-01", "2019-08-02", "2019-07-22", "2019-07-21", "2019-07-21"]}
    )
    print(article_views(views=views))
