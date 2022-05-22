#https://www.postgresqltutorial.com/postgresql-python/connect/
#!/usr/bin/python

import psycopg2
import sql

conntxt = "dbname=postgres user=postgres password=hiromi host=localhost"

def create_table_perform():
    conn = psycopg2.connect(
        database = 'CIFO', user='postgres', password = 'hiromi',
        host = 'localhost', port = '5432'
    )

    cursor = conn.cursor()
    sql = "DROP TABLE IF EXISTS PERFORM; CREATE TABLE PERFORM (COMBINATION VARCHAR(25), TEST_NUMBER VARCHAR(25),TIME VARCHAR(25), POP_SIZE VARCHAR(25), SELECTION VARCHAR(25), CROSSOVER VARCHAR(25), CROSSOVER_PERCENT VARCHAR(25), MUT_PERCENT VARCHAR(25))"

    cursor.execute(sql)
    print('Table create sucessfully')
    conn.commit()
    conn.close()

def insere_perform(selection, co_option, test_number, time, pop_size, crossover_percent, mut1, mut2, mut_percent):
    conn = psycopg2.connect(
        database='CIFO', user='postgres', password='hiromi',
        host='localhost', port='5432'
    )

    conn.autocommit = True

    n_combination = selection.__name__+'_'+co_option.__name__
    n_selection = str(selection.__name__)
    n_co_option = str(co_option.__name__)
    # n_mut1 = str(mut1)
    # n_mut2 = str(mut2)


    cursor = conn.cursor()

    cursor.execute("INSERT INTO PERFORM (COMBINATION, TEST_NUMBER, TIME, POP_SIZE, SELECTION, CROSSOVER, CROSSOVER_PERCENT, MUT_PERCENT) VALUES('"+n_combination+"',"+str(test_number)+","+str(time)+","+str(pop_size)+",'"+n_selection+"','"+n_co_option+"',"+str(crossover_percent)+","+str(mut_percent)+")")

    conn.commit()
    conn.close()

def create_table_analysis(selection, co_option):
    conn = psycopg2.connect(
        database = 'CIFO', user='postgres', password = 'hiromi',
        host = 'localhost', port = '5432'
    )
    nome = selection.__name__+"_"+ co_option.__name__

    cursor = conn.cursor()

    query = "DROP TABLE IF EXISTS " + nome + "; CREATE TABLE " + nome + " (TEST_NUMBER VARCHAR(25), COUNT VARCHAR(25),FITNESS VARCHAR(25),DIVERSITY VARCHAR(25))"

    sql = query

    cursor.execute(sql)
    print('Table create sucessfully')
    conn.commit()
    conn.close()

def insere_teste (test_number,selection, co_option,count, fitness, diversidade):
    conn = psycopg2.connect(
        database='CIFO', user='postgres', password='hiromi',
        host='localhost', port='5432'
    )

    nome = selection.__name__ + "_" + co_option.__name__

    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute("INSERT INTO "+nome+" (TEST_NUMBER, COUNT,FITNESS,DIVERSITY) VALUES ("+str(test_number)+","+str(count)+","+str(fitness)+","+str(diversidade)+")")

    conn.commit()
    conn.close()


