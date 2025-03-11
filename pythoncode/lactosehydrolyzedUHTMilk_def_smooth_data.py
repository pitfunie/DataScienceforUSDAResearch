def smooth_data(self):
    if self.data is not None:
        try:
            # Apply Savitzky-Golay filter
            intensity_values = self.data["Intensity"]
            smoothed_values = savgol_filter(
                intensity_values, window_length=11, polyorder=3
            )
            # Add smoothed data to DataFrame
            """_summary_
               Create DataFrame:
               self.data = pd.DataFrame( supercharged Excel spreadsheet rows and columns
               {"Wavelength": wavelengths, "Intensity": intensities})::
               This line creates a Pandas DataFrame from the wavelengths and intensities lists,
               storing it in the self.data attribute.
               Returns:
                _type_: _description_
            """
            self.data["Smoothed_Intensity"] = smoothed_values
            print("Data smoothing completed successfully")
            return True
        except Exception as e:
            print(f"Error in smoothing: {str(e)}")
            return False
    else:
        print("No data available to smooth")
        return False
