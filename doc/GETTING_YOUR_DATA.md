Once you have a Shareabouts map collecting data, you can explore it via the Django admin interface, and via the web-based RESTful API browser.

## Viewing data via the Django admin interface

Shareabouts data is accessible via the regular Django interface, at 

        https://SERVER/admin/

e.g. 

        http://data.shareabouts.org/admin/

### What can I do with the Django admin interface?

Using the Django interface, you can
* create new datasets
* view places by date
* view places in a particular dataset
* hide or show places with the Visibility checkbox in list view
* edit place data via the json blob editor

You cannot
* download data in a csv
* easily browse through data

## Viewing and downloading data via the API

You can explore your datasets here:

        https://SERVER/api/v2/USER/datasets/

e.g. 

        http://data.shareabouts.org/api/v2/openplans/datasets
        
At that URL, you'll see a list of datasets, with links to each dataset's places, supports, and surveys (which are comments).

### Where's my private data?

Private data in Shareabouts can only be accessed by an authenticated user. 
If you have fields prefixed with `private-` in your config, those fields aren't 
accessible unless you log in to the Django admin interface before using the API browser.

Use your admin account for `https://SERVER/admin/` (e.g. `http://data.shareabouts.org/admin/`) 
to add yourself as a superuser OR to set a password for the dataset owner. 

Then, log in via `https://SERVER/admin/`, then use the API browser in another tab. Private data shows up if you include `?include_private` in the url, e.g.

       http://data.shareabouts.org/api/v2/openplans/datasets/test-data/places?include_private

### Downloading snapshots

Data from the API can be paginated (using the `page_size` and `page` parameters), but it's tedious to assemble files offline, and if you make the page size too large, the page won't get generated before the server times out. 

Instead, use the `/snapshots` endpoint. This will queue up the process of generating an entire file on request, which you can download once it has been created.

To generate a snapshot, visit `server/api/v2/user/datasets/datasets/places/snapshots?new` e.g. 

          https://data.shareabouts.org/api/v2/openplans/datasets/test-data/places/snapshots?new

Swap `surveys` for `places` to download comments.

Refresh the provided link, if the file isn't ready you'll see 'You can download the data at the given URL when it is done being generated'.

Once you have the download link, you most likely want it as a csv. Add `.csv` to the end of the url, and then do a "Save Page As" from your browser. E.g.
* generate a snapshot
* load the provided URL, like `https://data.shareabouts.org/api/v2/openplans/datasets/test-data/places/snapshots/dac284a6-734a-0b31314e3505`
* reload it with `.csv` on the end, `https://data.shareabouts.org/api/v2/openplans/datasets/test-data/places/snapshots/dac284a6-734a-0b31314e3505.csv`
* save the file (copying it out to a file will give you something with weird line breaks)