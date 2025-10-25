import psycopg2

# cnx = psycopg2.connect(
#     host="mailr-poc-db-do-user-27465760-0.d.db.ondigitalocean.com",
#     port=25060,
#     database="defaultdb",
#     user="doadmin",
#     password="AVNS_5TyvMuMtbA2cPSSglgE",
# )


cnx = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="root",
)


print(cnx)
print(cnx.status)

