#!/bin/bash

# Clean the project
mvn clean

# Build the project
mvn package

# Check if the build was successful
if [ $? -eq 0 ]; then
  echo "Build completed successfully."
else
  echo "Build failed."
  exit 1
fi

# Run tests
mvn test

# Check if tests passed
if [ $? -eq 0 ]; then
  echo "All tests passed."
else
  echo "Some tests failed."
  exit 1
fi

# Additional steps can be added here, such as generating documentation or creating artifacts

# If everything succeeded, the built artifacts can be found in the target/

#Save this script in a file named build.sh, and make sure to provide the necessary permissions to execute the script by running chmod +x build.sh in the terminal.

#To execute the script, navigate to the directory containing the script file (build.sh) in the terminal and run ./build.sh.

#Make sure you have Maven installed and configured correctly in your environment before running this script. Adjust the script or include additional steps as needed based on your project's requirements.
