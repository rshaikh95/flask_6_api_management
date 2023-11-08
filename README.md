# flask_6_api_management

Link for Azure Deployment

![azuredeployapp](https://github.com/rshaikh95/flask_6_api_management/assets/141374132/26b7557d-9773-4a31-9a98-4209a671b11a)

Was not able to show app on website

![error](https://github.com/rshaikh95/flask_6_api_management/assets/141374132/db18ba85-cb67-4116-906b-379082282907)

1. First created function_app.py on Google Shell with code for a Get request using Azure Deployment

![Screenshot 2023-11-07 183801](https://github.com/rshaikh95/flask_6_api_management/assets/141374132/e05dc723-8f78-4d1c-bec8-3b9c0f909e82)

2. In the Google Shell terminal, you will need to install AZURE CLI with this: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash.
  Type in az login --use-device-code and wait for a link and a code to appear in the terminal. Copy the code and press the link to log in to your Azure account. 
  Install sudo apt-get install azure-functions-core-tools-4 in the terminal for azure functions core tools.
  Now to deploy the app, you will need to create a resource group, storage account, and a function app.
  For Resource group:  az group create --name <put the resource group name here that you want to create>-rg --location <insert location>

![Screenshot 2023-11-06 152405](https://github.com/rshaikh95/flask_6_api_management/assets/141374132/b75e74ac-3231-43bf-99ba-fb8c5d2d6004)

![Screenshot 2023-11-06 153117](https://github.com/rshaikh95/flask_6_api_management/assets/141374132/a6214bf5-bc5b-4363-a788-1e09135b64ac)

