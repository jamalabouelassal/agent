from scraping import scrape_jobs
from cleaning import clean_jobs
from save_postgres import save_to_postgres

# Paramètres PostgreSQL
db_params = {
    "host": "localhost",
    "dbname": "linkedin_jobs",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}

if __name__ == "__main__":
    # 1️⃣ Scraping
    df_raw = scrape_jobs()

    # 2️⃣ Cleaning
    df_clean = clean_jobs(df_raw)

    # 3️⃣ Sauvegarde
    save_to_postgres(df_clean, db_params)
