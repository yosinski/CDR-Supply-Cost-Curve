# Welcome

Hi there. This is a repo for work on the Air Miners CDR Supply Cost Curve problem pack.



# Setup

```
pip install -r requirements.txt
```



# JSON and Python and Google, oh my

The data pipeline:

 1. Run `210406_carbonplan_json_to_google.ipynb` manually once to load data from `carbonplan_projects.json` and export to Google Sheets in the proper format.
 2. Manually copy data from Google Sheet to the common sheet used by all.
 3. Pull data (including projections for the future, filled in by the team) from Google using `pull_from_google.py`. It will be saved to `data/...`
 4. Analyze that data using `210412_carbonplan.ipynb`, ...
