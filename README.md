Submission for Springboard Data Wrangling assignment:

Program :sliderule_dsi_json_exercise.py

The program reads JSON file world_bank_projects.json and converts it to a Dataframe.

To find the 10 countries with most projects the data is grouped by countries and unique projects counted.

To find the top 10 major project themes the JSON data is normalized as mjtheme_namecode field is nested.

Finally to remove the blank indexes from the data the index, column is read and index updated and stored in another dataframe with no blank index value.
