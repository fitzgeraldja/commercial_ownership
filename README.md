# commercial_ownership
Investigate public records of commercial ownership in a given place, and draw connections using Companies House data

- Note that an API key must be obtained, and to use code otherwise unchanged should be placed in a _apikey.py file in the utils directory, assigned to the variable `apikey`.
- NB running `data_collection.py` will create a data directory in the working directory if none exists, and download the _full_ CCOD and OCOD datasets, as the API does not allow prior restriction of focus to a particular area.
- This results in around 300MB data, so ensure you have sufficient space, and it may take some time. 
