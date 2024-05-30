from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

# Set up environment variables
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
