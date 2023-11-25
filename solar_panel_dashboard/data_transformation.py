# filename: solar_panel_dashboard/data_transformation.py
import pandas as pd

class DataTransformation:
    def transform_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Apply business logic to calculate KPIs and transform the data.

        :param data: The pandas DataFrame to transform.
        :return: The transformed pandas DataFrame with KPIs.
        """
        # Example KPI: Calculate the average energy output per panel
        if 'EnergyOutput' in data.columns and 'PanelID' in data.columns:
            data['AverageEnergyOutput'] = data.groupby('PanelID')['EnergyOutput'].transform('mean')
        
        # Additional transformations and KPI calculations can be added here

        return data