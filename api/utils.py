import datetime
import shutil

import geopandas as gpd
from django.templatetags.static import static


def convert_to_format(file, convert_to="shp"):
    data = gpd.read_file(file)
    file_type = "folder"
    kwargs = {}
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if convert_to == "json":
        file_type = "json"
        kwargs["driver"] = "GeoJSON"

    name = f"{current_datetime}." + file_type
    full_name = "api/static/" + name
    data.to_file(full_name, **kwargs)
    if file_type == "folder":
        name = f"{current_datetime}.zip"
        shutil.make_archive(
            f"api/static/{current_datetime}", 'zip', full_name)
        # Delete a folder after it's been zipped
        shutil.rmtree(f"{full_name}")
    return static(name)
