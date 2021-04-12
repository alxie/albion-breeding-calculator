# albion-breeding-calculator

Very hacky script that queries the markets across Albion online citites and calculates the profitability of breeding mounts, based on recipes.

## Current implementation
- The recipes are defined in the recipes_horizontal.json file
- The script queries dependencies for a recipe individually at the albion online data project, using its JSON API
- You have to hack the code to manually set the mount's ID. The current implementation queries the Moose mount: T6_MOUNT_GIANTSTAG_MOOSE
- You have to define which cities to search. The current implementation queries martlock, lymhurst, bridgewatch, fortsterling and caerleon

## Possible improvements
There are many places to improve:
- Pass the mount as cmd option.
- If this is implemented inside the Google App Engine using Flask (the current plan), foreach the list of recipes and create buttons for each, for example. 
- Options to choose which cities to query
- Add mastery to focus return rate
- Add option to select focus and without focus
- Instead of parsing the recipes json everytime, properly initialise the program using instantiated classes
- Query the albion online data project with all the required items just once, instead of one time per item
- Etc, etc, etc ...
