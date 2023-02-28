# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform mytable.
# Uses st.cache_data to only rerun when the mytable changes or after 10 min.
@st.cache_data(ttl=600)
def run_mytable(mytable):
    with conn.cursor() as cur:
        cur.execute(mytable)
        return cur.fetchall()

rows = run_mytable("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
