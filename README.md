# DataS cience for USDA Research Machine Learning

tensor([1., 2., 3.])


tensor([1., 2., 3.])

This indicates the conversion of a NumPy array [1.0, 2.0, 3.0] to a PyTorch tensor. The tensor contains three elements with values 1.0, 2.0, and 3.0, and it's of type FloatTensor.

Analysis Messages:

    Starting Lactose Free Milk Analysis: Initiates the analysis process.

    Test data created successfully: Synthetic test data was successfully generated.

    Created 61 data points: A total of 61 data points were created, with wavelengths ranging from 200 to 800 nm.

    Data smoothing completed successfully: The Savitzky-Golay filter was applied to smooth the intensity data.
    

![2025-03-11_00-04-53](https://github.com/user-attachments/assets/6bc83654-fc8c-48ae-9678-96511b2623e0)


Machine Learning Model Performance:

    Precision, Recall, F1-Score, Support:
          precision    recall  f1-score   support

   Alpha       1.00      1.00      1.00        10
   Other       1.00      1.00      1.00         3

he Random Forest classifier identified "Alpha" structures with perfect precision, recall, and F1-score (all 1.00). The support indicates 10 data points for "Alpha" and 3 data points for "Other."

Accuracy: The model achieved 100% accuracy for the test set of 13 data points.

Macro avg and Weighted avg: Both are 1.00, indicating perfect performance across all metrics.

Structures Identified:

    Alpha Helices: 47 data points were identified as Alpha Helices.

    Beta Sheets: No data points were identified as Beta Sheets.

Analysis Results Summary:

    Data Overview:

        Total measurements: 61 data points.

        Wavelength range: From 200 nm to 800 nm.

        
  Intensity Statistics:

  count    61.000000
  mean      0.564973
  std       0.088616
  min       0.500000
  25%       0.500064
  50%       0.512378
  75%       0.627526
  max       0.800000
  Name: Intensity, dtype: float64


  This statistical summary provides insights into the intensity values:

    Mean: Average intensity value is approximately 0.565.

    Standard Deviation (std): Variability in the intensity values is approximately 0.089.

    Min and Max: Minimum intensity is 0.500 and maximum is 0.800.

    Quartiles:

        25% of the data points have intensity values less than approximately 0.500.

        50% (median) have intensity values less than approximately 0.512.

        75% have intensity values less than approximately 0.628.

Structure Counts:

    ML Alpha Helices: 47

    ML Beta Sheets: 0
