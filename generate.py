import folium
import sys

try:
    target = sys.argv[1]
except:
    print("Please add a city name argument to generate a map from.")
    print("For example: python generate.py lisbon")
    print("It will then look into the lisbon folder and generate your coordinates in there.")
    sys.exit()

# Parse coords.txt to a list of coordinates
# coordinate = [latitude, longitude]
coordinates = []
with open(target + "/coords.txt") as coordinates_file:
    for line in coordinates_file:
        line_list = line.split(", ")
        coord = [float(i) for i in line_list[:-3]]
        icon = line_list[-3]
        color = line_list[-2]
        description = line_list[-1].strip("\n").strip("\"")
        coordinates.append({"coordinate":coord, "icon":icon, "color":color,
                            "description":description})

# Create map object
map = folium.Map(location=coordinates[0]["coordinate"], zoom_start=12)

for coord_info in coordinates:
    description = coord_info["description"]
    folium.Marker(coord_info["coordinate"],
                  icon=folium.Icon(icon=coord_info["icon"], color=coord_info["color"]),
                  tooltip=description).add_to(map)

# Generate map
map.save(target + f"/{target}.html")
print(f"{target}.html was successfully generated!")