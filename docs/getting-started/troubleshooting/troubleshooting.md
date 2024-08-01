#Troubleshooting Guide for momentum.sh


If your repository is not being parsed by app.momentum.sh or is stuck in an error state, follow these troubleshooting steps in order:

## 1. Verify GitHub App Installation
- **Check**: Is the GetMomentum GitHub app installed successfully on your repository?
- **Solution**: If not, link the repo again from the [app](https://app.momentum.sh) dashboard or from the app [listing](https://github.com/apps/getmomentum)

## 2. Confirm Repository Language Support
- **Check**: Is your repository primarily Python (>50% of codebase)?
- **Solution**: Ensure your main codebase is in Python. momentum.sh currently supports Python repositories.

## 3. Validate HTTP API Presence
- **Check**: Does your repo contain HTTP APIs defined using FastAPI, Sanic, Django, or Flask?
- **Solution**: Implement or update your APIs using one of these supported frameworks.

## 4. Check CLI Installation and Execution
- **Check**: Is the momentum.sh CLI installed and running?
- **Solution**: 
  - Install the CLI if not already done. Install the python package from [PyPi](https://pypi.org/project/momentum-cli/).
  - Ensure the CLI is running in your IDE for local testing and debugging.

## 5. Verify CLI Configuration
- **Check**: Is the CLI app configured correctly?
- **Solution**: 
  - Review your CLI configuration.
  - Refer to momentum-cli [documentation](https://docs.momentum.sh/using-momentum-cli) for correct setup.

## Additional Notes
- If all above checks pass and issues persist, it may be an issue with parsing your particular repository.
- Report persistent issues to [momentum.sh Core Issues](https://github.com/getmomentum/momentum-core/issues).
- For further assistance, you can get real time support by joining our [Discord server](https://discord.gg/3ns29mEJMg)