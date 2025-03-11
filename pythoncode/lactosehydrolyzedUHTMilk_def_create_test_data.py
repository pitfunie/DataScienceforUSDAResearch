 def create_test_data(self):
     """
     Create test data using pure lists Function Purpose: The create_test_data
     method is designed to generate synthetic test data using pure lists.
     Wavelength Range Creation:

     It generates a list of wavelengths ranging from 200 nm to 800 nm, with a
     step of 10 nm, which means you'll get wavelengths like 200, 210, 220, ...,
     800.
     Intensity Values Creation:
     For each wavelength, it calculates an intensity value based on a simple model.
     The base intensity is set to 0.5, which serves as a constant background level.
     The alpha_contribution represents an intensity peak centered around 400 nm,
     following a Gaussian-like distribution.  The beta_contribution represents
     another intensity peak centered around 600 nm, also following a Gaussian-like
     distribution.  The total intensity for each wavelength is the sum of the base,
     alpha, and beta contributions.
     """
     try:
         # Create wavelength range from 200 to 800 nm
         wavelengths = list(range(200, 801, 10))
         # Create synthetic intensity values
         intensities = []
         for w in wavelengths:
             # Create a more realistic intensity pattern
             base = 0.5
             # Contribution of an alpha component centered at 400 nm
             alpha_contribution = 0.3 * np.exp(-((w - 400) ** 2) / 2000)
             # Contribution of a beta component centered at 600 nm
             beta_contribution = 0.2 * np.exp(-((w - 600) ** 2) / 2000)
             # Total intensity is the sum of base, alpha, and beta contributions
             intensity = base + alpha_contribution + beta_contribution
             intensities.append(intensity)
         # Create DataFrame from the wavelengths and intensities
         self.data = pd.DataFrame(
             {"Wavelength": wavelengths, "Intensity": intensities}
         )
         # Print success message and number of data points created
         print("Test data created successfully")
         print(f"Created {len(self.data)} data points")
         return True
     except Exception as e:
         # Print error message if there is an issue creating test data
         print(f"Error creating test data: {str(e)}")
         return False
 def smooth_data(self):