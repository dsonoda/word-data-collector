# word-data-collector
It's a tool that allows you to collect related information of input text in various media formats, such as dictionaries, images and voice.

# Requirement

see: https://github.com/dsonoda/word-data-collector/blob/master/Pipfile

# Installation

```bash
$ git clone git@github.com:dsonoda/word-data-collector.git
$ pipenv install
```

# Usage
### 1. Account and credit and subscription registration  
This tool uses several APIs of [RapidAPI](https://rapidapi.com/). To get the common API keys available within RapidAPI, you must first register for a RapidAPI account. After registering, you should be able to go to the appropriate API page and see the common API key.  
  
Also, the API you use must be registered with a credit card and a subscription. The APIs you use by default have a free quota, so you won't be charged unless you run a huge number of APIs.  

#### Create an account and register your credit card.  
https://rapidapi.com/developer/billing/billing-information  

#### words api  
https://rapidapi.com/dpventures/api/wordsapi/pricing  

#### google translate api  
https://rapidapi.com/googlecloud/api/google-translate1/pricing  

#### HiBrainy text-to-speech api  
https://rapidapi.com/HiBrainy/api/text-to-speech5/pricing  

#### bing image search api  
https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/bing-image-search1/pricing  


### 2. Set the environment variable.  

```bash
$ export WORDDATACOLLECTOR_API_KEY=[rapid-api-key]
$ export WORDDATACOLLECTOR_SAVE_DIR=[/path/to/data save dir]
```

|environment variable|description|
|:---|:---|
|WORDDATACOLLECTOR_API_KEY|Specify the obtained API key.|
|WORDDATACOLLECTOR_SAVE_DIR|Specifies the path to the directory where data is saved when the tool is executed.|

### 3. Let's run the [sample code](https://github.com/dsonoda/word-data-collector/blob/master/word_data_collector/examples.py).  

```bash
$ cd path/to/word_data_collector
$ pipenv shell
(word-data-collector) bash-3.2$ python examples.py
```

Make sure the data file is downloaded to the designated storage directory.

```
path/to/save_dir
    ├── image
    │   └── mountain
    │       ├── ea708ac3419ed8b77056c6f485b4a693.jpg
    │       └── f096e023377fb5c0dea1d5bc776e1946.jpg
    ├── translation
    │   └── mountain
    │       └── translation.json
    ├── voice
    │   └── mountain
    │       └── voice.mp3
    └── word
        └── mountain
            └── word.json
```

# Note
Please note that you will be charged automatically if you exceed the free limit of the API.  
 
# Author
* [Daisuke Sonoda](https://daisukesonoda.com/) / Freelance Software Engineer  
* [mail@daisukesonoda.com](mail@daisukesonoda.com)  
* [@d5onoda](https://twitter.com/d5onoda)  
 
# License
**word-data-collector** is under [GPL-3.0 License](https://github.com/dsonoda/word-data-collector/blob/master/LICENSE).
