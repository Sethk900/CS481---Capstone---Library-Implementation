#!/usr/bin/bash
# Run the linters on the current library code: if the formatting fails any of the tests, exit 1.
# This will cause a build to fail if the script is run as part of an automated build solution (as long as you run the script as part of that solution!)
status=0
black --check scripts || status=1
pydocstyle || status=1
cd scripts && flake8 || status=1
cd .. && flake8 --ignore=E501 || status=1
exit $status

