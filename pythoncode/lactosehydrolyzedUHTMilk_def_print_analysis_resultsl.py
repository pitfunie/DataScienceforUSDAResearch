
    """
       Explanation:

       Method Definition: def print_analysis_results(self): Defines the print_analysis_results
       method to print a comprehensive summary of the analysis results.

       Check for Data Availability:  Checks if self.data is not None. If data is available, the
       method proceeds. Otherwise, it prints a message indicating no data is available and returns
       False.

       Print Data Overview: Prints a header for the analysis results summary including the total number
       of measurements and the range of wavelengths.

       Print Intensity Statistics: Prints a statistical summary of the intensity values using the
       describe method of the DataFrame.

       Check for ML Analysis Results: Checks if the ML analysis results are available by verifying
       the presence of the 'ML_Alpha_Helices' column.. If available, it prints the counts of identified
       structures (Alpha Helices and Beta Sheets). Returns True to indicate the successful printing
       of results.

       Catches any exceptions that occur during the printing process, prints the error message,
       and returns False.  Prints a message if no data is available and returns False.

    """

    def print_analysis_results(self):
        """Print comprehensive analysis results"""
        if self.data is not None:
            try:
                print("\n=== Analysis Results Summary ===")
                print("\nData Overview:")
                print(f"Total measurements: {len(self.data)}")
                print(
                    f"Wavelength range: {self.data['Wavelength'].min()} - {self.data['Wavelength'].max()} nm"
                )
                # Print statistical summary of the intensity values
                print("\nIntensity Statistics:")
                print(self.data["Intensity"].describe())

                if "ML_Alpha_Helices" in self.data.columns:
                    # Print counts of identified structures (Alpha Helices and Beta Sheets)
                    print("\nStructure Counts:")
                    print(f"ML Alpha Helices: {sum(self.data['ML_Alpha_Helices'])}")
                    print(f"ML Beta Sheets: {sum(self.data['ML_Beta_Sheets'])}")

                return True
            except Exception as e:
                # Print error message if there is an issue printing the results
                print(f"Error printing results: {str(e)}")
                return False
        else:
            print("No data available")
            return False
