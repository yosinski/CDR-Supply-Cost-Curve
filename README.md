# Welcome

Hi there. This is a repo for work on the Air Miners CDR Supply Cost Curve problem pack.



# Setup

```
pip install -r requirements.txt
```



# Python and Google sheets and Jupyter, oh my

Initial setup of the data (already done now):

 1. Run `210406_carbonplan_json_to_google.ipynb` manually once to load data from `carbonplan_projects.json` and export to Google Sheets in the proper format.
 2. Manually copy data from Google Sheet to the common sheet used by all.

Pull fresh data from Google sheets:

 1. Pull data (including projections for the future, filled in by the team) from Google using `pull_from_google.py`. The last line will overwrite the current version of `Supply_Cost_Projections_df.csv` saved in the repo.

     cd CDR-Supply-Cost-Curve
     python/pull_from_google.py
     mv -f output.csv data/Supply_Cost_Projections_df.csv
     
 2. Analyze that data using the `210412_carbonplan.ipynb` Jupyter notebook.




# Setting up Google credentials for gspread

Follow [these instructions](https://pypi.org/project/gspread-pandas/). You'll have to do that once to set up the authentication, and then you might have to redo it again if your tokens expire (happened to me after one week).

If you get this error:

    google.auth.exceptions.RefreshError: ('invalid_grant: Token has been expired or revoked.', '{\n  "error": "invalid_grant",\n  "error_description": "Token has been expired or revoked."\n}')
    
Then remove this file and it should force a re-authorization when you run the `pull_from_google.py` script:

    rm ~/.config/gspread/authorized_user.json




