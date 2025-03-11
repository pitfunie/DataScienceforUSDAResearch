 def create_comprehensive_visualization(self):
     """Create comprehensive visualization"""
     # Check if data is available
     if self.data is not None:
         try:
             # Create a 2x2 grid of subplots with a specified figure size
             fig, axes = plt.subplots(2, 2, figsize=(15, 10))
             # Raw vs Smoothed Data
             axes[0, 0].plot(
                 self.data["Wavelength"],
                 self.data["Intensity"],
                 label="Raw",
                 alpha=0.5,
             )
             # Check if smoothed data exists and plot it
             if "Smoothed_Intensity" in self.data.columns:
                 axes[0, 0].plot(
                     self.data["Wavelength"],
                     self.data["Smoothed_Intensity"],
                     label="Smoothed",
                     alpha=0.5,
                 )
             # Set the title and legend for the first subplot
             axes[0, 0].set_title("Raw vs Smoothed Data")
             axes[0, 0].legend()
             # Structure Identification
             if "ML_Alpha_Helices" in self.data.columns:
                 axes[0, 1].plot(
                     self.data["Wavelength"],
                     self.data["Smoothed_Intensity"],
                     "k-",
                     label="Data",
                     alpha=0.3,
                 )
                 # Plot ML predictions for Alpha Helices and Beta Sheets
                 alpha_data = self.data[self.data["ML_Alpha_Helices"]]
                 beta_data = self.data[self.data["ML_Beta_Sheets"]]
                 if not alpha_data.empty:
                     axes[0, 1].scatter(
                         alpha_data["Wavelength"],
                         alpha_data["Smoothed_Intensity"],
                         color="red",
                         label="Alpha Helix",
                         alpha=0.5,
                     )
                 if not beta_data.empty:
                     axes[0, 1].scatter(
                         beta_data["Wavelength"],
                         beta_data["Smoothed_Intensity"],
                         color="blue",
                         label="Beta Sheet",
                         alpha=0.5,
                     )
                 # Set the title and legend for the second subplot
                 axes[0, 1].set_title("Structure Identification")
                 axes[0, 1].legend()
             # Intensity Distribution
             axes[1, 0].hist(self.data["Intensity"], bins=30, alpha=0.5, label="Raw")
             if "Smoothed_Intensity" in self.data.columns:
                 axes[1, 0].hist(
                     self.data["Smoothed_Intensity"],
                     bins=30,
                     alpha=0.5,
                     label="Smoothed",
                 )
             # Set the title and legend for the third subplot
             axes[1, 0].set_title("Intensity Distribution")
             axes[1, 0].legend()
             # Structure Distribution
             if "ML_Alpha_Helices" in self.data.columns:
                 structure_counts = [
                     sum(self.data["ML_Alpha_Helices"]),
                     sum(self.data["ML_Beta_Sheets"]),
                     len(self.data)
                     - sum(self.data["ML_Alpha_Helices"])
                     - sum(self.data["ML_Beta_Sheets"]),
                 ]
                 labels = ["Alpha Helices", "Beta Sheets", "Other"]
                 axes[1, 1].pie(structure_counts, labels=labels, autopct="%1.1f%%")
                 axes[1, 1].set_title("Structure Distribution")
             # Adjust layout for better spacing and display the plots
             plt.tight_layout()
             plt.show()
             return True
         except Exception as e:
             print(f"Error creating visualization: {str(e)}")
             return False
     else:
         print("No data available")
         return False