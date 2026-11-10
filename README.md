# AMR Lab CSV Content API

FastAPI backend for the existing AMR Lab static website. The CSV files in `data/` are the content source of truth.

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000/ — service status
- http://127.0.0.1:8000/docs — interactive API documentation
- http://127.0.0.1:8000/api/content — all website content

## CSV editing behaviour

CSV files are read from disk on every API request. Edit and save a CSV and the next page load/API request reads the new content. No backend restart is required.

For the public site, push changed CSV files to the backend GitHub repository. Render is configured for automatic deployment on push. Once deployment finishes, reload the public website. Render free instances may sleep when idle, so the first request can take longer.

## Production CORS

The API allows `https://navjotsig.github.io` and common local development origins. Set `CORS_ORIGINS` in Render only if you later use a custom frontend domain.

## Important

- The API is read-only. Do not upload private information or secrets into public CSV files.
- CSV columns are part of the API contract. Keep the header row unchanged; add/edit rows instead.
- Use UTF-8 CSV. Excel may save CSV as UTF-8 (Comma delimited).
- This starter backend has no admin login or public write endpoint. Content changes are made by editing CSVs in the backend repository.
