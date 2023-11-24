# filename: solar_panel_monitoring/main.py
import sys
from solar_panel_monitoring.orchestration_service import orchestrate_pipeline

def main():
    """
    Main function to start the orchestration of the solar panel monitoring services.
    """
    try:
        # Start the orchestration of the data pipeline
        orchestrate_pipeline()
    except Exception as e:
        print(f"An error occurred during the orchestration process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()