# Sample of how to deploy from Circle CI and run an end-to-end test

<img src="https://circleci.com/gh/GoogleCloudPlatform/continuous-deployment-circle.png?circle-token=73d9769ac94a3e1aebc919b1f32dcfff6e02f688"></img>

This repo demonstrates how to deploy to Google Cloud from a
Circle CI file and run an end to end test (in e2e_test.py) against
a staging environment.

See the [managed_vms](https://github.com/googlecloudplatform/continuous-deployment-circle/tree/managed_vms) branch for a similar repo and Circle deployment using Managed VMs.

## Prerequisites

First, you must create a Cloud project. Two types of credentials are required. The first is a service account to authorize the gcloud command line tool in the Circle CI environment, which is used to deploy the project. The second is an API key used to access the Books API.

* Create a Cloud project using the [Google Cloud Console](https://console.developer.google.com)
* Under API Manager -> Google APIs, search and enable the Books API and the App Engine Admin APIs
* Under Api Manager -> Credentials, click New Credentials -> API Key -> Server Key. Copy the key into api_key.py , see api_key.py.sample as a reference. Don't check api_key.py into the repository (it's already in the .gitignore).
* Under Api Manager -> Credentials -> Service Account key, create a JSON key and download it.

Both of the credentials need to be base64 encoded and added to the Circle CI project as an environment variable.

* Go to [Circle CI](https://circleci.com). If you haven't already done so, create an account and enable your project.
* On the top right, click `Project Settings`, then on the left click `Environment Variables`.
* Base64 encode the client secret JSON file

    `base64 <your_secret.json>`

* Copy the output of the base64 command into the 'Value' form, with the name CLIENT_SECRET, then click `Save Variable`.
* Base64 encdode the api_key.py file

    `base64 api_key.py`
*  Copy the output of the base64 command into the 'Value' form, with the Name field set to API_KEY. Click `Save Variable`.
* In the circle.yaml file, replace the <your-project-id> in `gcloud config set project` with your project id.
* In e2e_test.py, replace the <your-project-id> in the HOST variable with the URL your project will be deployed to `https://your-project-id.appspot.com`.
* Commit and push your changes. The circle project should run the local tests, then use the gcloud SDK (authenticated with the client-secret) to deploy to the appspot URL, then run the e2e tests against that URL.

## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)


## Licensing

* See LICENSE

Copyright (C) 2015 Google Inc.
