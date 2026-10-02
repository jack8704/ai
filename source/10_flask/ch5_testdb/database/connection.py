import cx_Oracle
import pandas as pd
conn = cx_Oracle.connect("scott",
                        "tiger",
                        "localhost:1521/xe")
