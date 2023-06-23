
---

# Maven Build Script

This script is designed to build and test a Maven project. It automates the process of cleaning the project, building the project, and running tests. It also provides feedback on the success or failure of each step.

## Prerequisites

Before running this script, ensure that you have the following prerequisites installed:

- [Maven](https://maven.apache.org/) - The Apache Maven build tool.
- [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) - The Java development kit required for building and running the project.

## Usage

To use this script, follow the steps below:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Make the script executable, if necessary, using the command: `chmod +x build.sh`
4. Run the script using the command: `./build.sh`

## Script Explanation

The script performs the following steps:

1. **Clean the Project**: The command `mvn clean` is executed to clean the project directory by removing any previously compiled files or artifacts.

2. **Build the Project**: The command `mvn package` is executed to build the project. This step compiles the source code, runs any necessary tests, and packages the application into an executable artifact (e.g., JAR file).

3. **Check Build Status**: The script checks the exit code of the previous command using `$?`. If the exit code is `0`, it indicates a successful build. The script displays the message "Build completed successfully." Otherwise, it displays the message "Build failed." and exits with status `1`.

4. **Run Tests**: The command `mvn test` is executed to run any defined tests for the project.

5. **Check Test Results**: Similar to the previous step, the script checks the exit code of the previous command. If the exit code is `0`, it indicates that all tests passed. The script displays the message "All tests passed." Otherwise, it displays the message "Some tests failed." and exits with status `1`.

