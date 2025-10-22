import psycopg2

def save_to_postgres(df, db_params):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS linkedin_jobs (
                id SERIAL PRIMARY KEY,
                job_title TEXT,
                company_name TEXT,
                time_posted INT,
                num_applicants INT
            );
        """)
        conn.commit()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO linkedin_jobs (
                    job_title, company_name, time_posted, num_applicants
                ) VALUES (%s, %s, %s, %s)
            """, (
                row["job_title"],
                row["company_name"],
                int(row["time_posted"]) if row["time_posted"] is not None else None,
                int(row["num_applicants"]) if row["num_applicants"] is not None else None
            ))

        conn.commit()
        print("💾 Données insérées avec succès dans PostgreSQL !")

    except Exception as e:
        print("❌ Erreur PostgreSQL :", e)

    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()
            print("🔒 Connexion PostgreSQL fermée.")
