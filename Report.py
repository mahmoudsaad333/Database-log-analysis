#!/usr/bin/env python

import psycopg2

# connect to psql database and return connection


def db_query(query):
    dbconn = psycopg2.connect(database="news")
    cursor = dbconn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    dbconn.close()
    return results


def print_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' = ' + str(result[1]) + ' views')


def print_query3_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' = ' + str(result[1]) + ' %')

# task 1
task_1 = "select title,views from article_view limit 3"

# task 2
task_2 = """select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""

# task 3
task_3 = "select * from error_view where \"Percent Error\" > 1"

# using dict() hash table
task1_result = dict()
task1_result['title'] = "\n Task 1:\n"

task2_result = dict()
task2_result['title'] = """\n Task 2:\n"""

task3_result = dict()
task3_result['title'] = """\n Task 3:\n"""


# stores result
task1_result['results'] = db_query(task_1)
task2_result['results'] = db_query(task_2)
task3_result['results'] = db_query(task_3)

# print output
print_results(task1_result)
print_results(task2_result)
print_query3_results(task3_result)
