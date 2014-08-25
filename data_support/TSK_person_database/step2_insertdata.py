from person import *
import faker
import sqlite3

def prt_all(c):
    for row in c.fetchall():
        print row

def main():
    conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
    c = conn.cursor()
    fake = faker.Factory.create() # create faker generator
    records = list() #
    for person in person_generator(1000):
        lastname, firstname = fake.last_name(), fake.first_name()
        records.append((lastname, firstname, '',
                        person['International_Terrorist_Watch_List'],
                        person['National_Terrorist_Watch_List'],
                        person['National_Law_Enforcement'],
                        person['Local_Law_Enforcement'],
                        person['IRS_or_other_Federal_Finance_Company'],
                        person['Face_Match_with_Picture_DB'],
                        person['Cash_Payment_Same_Day'],
                        person['Immediate_Family'],
                        person['Extented_Family'],
                        person['Place_of_Worship'],
                        score1_base(person), 0, 0))
     
    c.executemany("INSERT INTO person VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", records)
    c.execute("SELECT * FROM person")
#     for row in c.fetchall():
#         print row
    conn.commit()
    
        
if __name__ == '__main__':
    for i in xrange(1000):
        main()
        print i