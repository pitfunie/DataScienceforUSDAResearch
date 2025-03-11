def run_analysis():
    """Run complete analysis"""
    # Print starting message for the analysis
    print("=== Starting Lactose Free Milk Analysis ===")
    # Initialize the LactoseFreeMilkAnalysis class
    analyzer = LactoseFreeMilkAnalysis()
    # Create test data
    if not analyzer.create_test_data():
        return None
    # Smooth the data
    analyzer.smooth_data()
    # Identify structures using machine learning (Random Forest method)
    analyzer.identify_structures_ml(method="random_forest")
    # Print the analysis results
    analyzer.print_analysis_results()
    # Create comprehensive visualizations
    analyzer.create_comprehensive_visualization()
    # Return the analyzer object
    return analyzer


if __name__ == "__main__":
    analyzer = run_analysis()