# AMR Lab CSV editing guide

Edit the CSV files in `backend/data/`. The first row contains column headers; keep those headers unchanged.

| File | Columns | Website section |
|---|---|---|
| `research.csv` | `number,title,text,tags` | Research themes |
| `projects.csv` | `title,sponsor,period,status,kind` | Sponsored and consultancy projects |
| `news.csv` | `title,venue,note` | Homepage news |
| `journals.csv` | `year,title,citation,doi` | Journal publications |
| `conferences.csv` | `year,title,citation` | Conference publications |
| `patents_granted.csv` | `year,title,detail` | Granted patents |
| `patents_filed.csv` | `year,title,detail` | Filed patents |
| `current_people.csv` | `name,role,group,detail` | Current team |
| `alumni.csv` | `name,role,detail` | Alumni |
| `student_projects.csv` | `item` | Student/project archive |
| `activities.csv` | `year,title,items` | Academic activities |
| `awards.csv` | `year,title,detail` | Awards |

## Editing rules

- Add one new record per row.
- In `research.csv`, separate multiple tags with a semicolon, for example `Antenna arrays; RF systems`.
- In `activities.csv`, separate multiple bullet items in the `items` cell with ` || `.
- In `projects.csv`, use `ongoing` or `completed` for `status`; use `sponsored` or `consultancy` for `kind`.
- In publications, put the DOI identifier only in the `doi` column, without `https://doi.org/`.
- Use UTF-8 CSV. Excel's **CSV UTF-8 (Comma delimited)** option is recommended.
- If a cell contains commas, Excel will quote it automatically. Do not manually delete those quotes.
- Do not rename columns or CSV files unless the API code is updated too.

## Publishing an update

For local testing, save the CSV and refresh the frontend page; the API reads the file on every request.

For the public website, commit and push the changed CSV to the backend repository. Render automatically deploys the new commit. Once the Render deployment is live, refresh the GitHub Pages site. The frontend URL does not change.

## Content accuracy

The initial CSVs were exported from the supplied website project. Check names, titles, publication details, dates, award claims, roles, and statuses with the lab before treating the migrated content as the final official record.
