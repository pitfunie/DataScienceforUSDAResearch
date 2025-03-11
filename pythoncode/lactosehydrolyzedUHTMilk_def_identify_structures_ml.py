def identify_structures_ml(self, method="random_forest"):
    """Identify protein structures using machine learning"""
    if self.data is not None and "Smoothed_Intensity" in self.data.columns:
        try:
            # Prepare features
            features = pd.DataFrame(
                {
                    "Intensity": self.data["Intensity"],
                    "Smoothed_Intensity": self.data["Smoothed_Intensity"],
                    "Wavelength": self.data["Wavelength"],
                }
            )
            # Scale features
            scaled_features = self.scaler.fit_transform(features)
            """
            _summary_
            analyze_structures method to analyze protein structures using the specified machine
            learning method Checks if the data has been smoothed.. If not, it prints a message
            and returns False creates synthetic labels based on the Smoothed_Intensity values.
            Labels are assigned as "Alpha" if Smoothed_Intensity is greater than 0.5, "Beta"
            if less than 0.3, and "Other" otherwise.
            Returns:
                Applies KMeans clustering to the scaled features, Determines the centroids and
                assigns clusters based on the intensity and predicted structures
            """
            # Apply specified machine learning method
            if method == "random_forest":
                # Create synthetic labels based on Smoothed_Intensity values
                labels = np.where(
                    self.data["Smoothed_Intensity"] > 0.5,
                    "Alpha",
                    np.where(
                        self.data["Smoothed_Intensity"] < 0.3, "Beta", "Other"
                    ),
                )
                # Split data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(
                    scaled_features, labels, test_size=0.2, random_state=42
                )
                # Initialize and train the Random Forest classifier
                self.ml_model = RandomForestClassifier(
                    n_estimators=100, max_depth=5, random_state=42
                )
                self.ml_model.fit(X_train, y_train)
                # Predict structures using the trained model
                predictions = self.ml_model.predict(scaled_features)
                # Update DataFrame with predicted structures
                self.data["ML_Alpha_Helices"] = predictions == "Alpha"
                self.data["ML_Beta_Sheets"] = predictions == "Beta"
                # Add traditional method results for comparison
                self.data["Alpha_Helices"] = self.data["Smoothed_Intensity"] > 0.8
                self.data["Beta_Sheets"] = self.data["Smoothed_Intensity"] < 0.3
                # Print machine learning model performance
                print("\nMachine Learning Model Performance:")
                print(classification_report(y_test, self.ml_model.predict(X_test)))
            elif method == "kmeans":
                # KMeans clustering
                kmeans = KMeans(n_clusters=3, random_state=42)
                clusters = kmeans.fit_predict(scaled_features)
                # Assign clusters
                centroids = kmeans.cluster_centers_
                cluster_intensities = centroids[:, 1]
                # Determine centroids and assign clusters
                alpha_cluster = np.argmax(cluster_intensities)
                beta_cluster = np.argmin(cluster_intensities)
                self.data["ML_Alpha_Helices"] = clusters == alpha_cluster
                self.data["ML_Beta_Sheets"] = clusters == beta_cluster
            # Calculate statistics and prints
            ml_alpha_count = sum(self.data["ML_Alpha_Helices"])
            ml_beta_count = sum(self.data["ML_Beta_Sheets"])
            print(f"\nStructures identified:")
            print(f"Alpha Helices: {ml_alpha_count}")
            print(f"Beta Sheets: {ml_beta_count}")
            return True
        except Exception as e:
            print(f"Error in ML structure identification: {str(e)}")
            return False
    else:
        print("Please smooth data first")
        return False
