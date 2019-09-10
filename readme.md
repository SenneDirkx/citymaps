# Citymaps
A python script that will generate an html file containing an interactive map with markers of your choice based on a simple txt file containing coordinates.

Dependencies: folium (python implementation of leaflet.js)

## Getting started
1. Create a folder (example name 'Citymaps') and add *generate.py* to this folder.
2. Create a subfolder with the name of the city you desire
3. In this subfolder, add a file named *coords.txt*
4. In this file you can add the landmarks you would like to visit during your citytrip.
5. Use the following format: *latitude*, *longitude*, *(glyph)icon*, *marker color*, *title (in double quotes)*
Example for Lisbon below:
`38.691659, -9.216031, tower, red, "Torre de Belém"
38.715619, -9.137032, road, red, "Tram 28"
38.712049, -9.131531, picture, purple, "Alfama District"`

The available (glyph)icons are listed here: https://getbootstrap.com/docs/3.3/components/#glyphicons-glyphs

The available colors are: *lightgreen, beige, purple, gray, darkpurple, orange, pink, black, lightred, darkred, cadetblue, white, lightgray, blue, darkblue, red, darkgreen, green, lightblue*