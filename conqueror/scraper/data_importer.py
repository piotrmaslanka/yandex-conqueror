import os
import pathlib

import pandas as pd

__all__ = ("DataImporter",)

BASE_FILES_LOC: str = os.path.join(
    pathlib.Path(__file__).parent.parent.parent, "resources"
)


class DataImporter:
    def read_xlsx(self) -> pd.DataFrame:
        """Read data from xlsx file and load the into data frame."""
        xlsx_location_: str = os.path.join(BASE_FILES_LOC, "russian-cities.xlsx")
        raw_df = pd.read_excel(xlsx_location_, engine="openpyxl")
        return raw_df

    def apply_transformations(self, raw_df: pd.DataFrame) -> None:
        """Make columns lower case & snake_case."""
        raw_df.columns = map(str.lower, raw_df.columns)
        df = raw_df.rename(
            columns={
                "city in english": "city_in_english",
                "city in russian": "city_in_russian",
                "radius [km]": "radius_km",
            },
            errors="raise",
        )
        self.save_into_json(df)

    @staticmethod
    def save_into_json(df: pd.DataFrame) -> None:
        """Save prepared data frame into json format."""
        df.to_json("here.json")


d = DataImporter()
raw_df = d.read_xlsx()
d.apply_transformations(raw_df)
