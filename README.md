# word-data-collector
It's a tool that allows you to collect related information of input text in various media formats, such as dictionaries, images and voice.

# Requirement

see: https://github.com/dsonoda/word-data-collector/blob/master/Pipfile

# Installation

```bash
$ git clone git@github.com:dsonoda/word-data-collector.git
$ cd path/to/word-data-collector
$ pipenv install
```

# Usage
1. The tool uses several of RapidAPI's APIs; to get a common API key that can be used within RapidAPI, you must first register for a RapidAPI account. After registering, go to the appropriate API page and you should see the common API key.  
You will also need to register a credit card for some of the API subscriptions. The APIs you use by default have free quotas, so you won't be charged unless you run a huge number of APIs.  

    Create an account and register your credit card.  
    https://rapidapi.com/developer/billing/billing-information  

    words api  
    https://rapidapi.com/dpventures/api/wordsapi/pricing  

    google translate api  
    https://rapidapi.com/googlecloud/api/google-translate1/pricing  

    HiBrainy text-to-speech api  
    https://rapidapi.com/HiBrainy/api/text-to-speech5/pricing  

    bing image search api  
    https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/bing-image-search1/pricing  


2. Set the following environment variables.  

    ```bash
    $ export WORDDATACOLLECTOR_API_KEY=[rapid-api-key]
    $ export WORDDATACOLLECTOR_SAVE_DIR=[/path/to/data save dir]
    ```

    ```WORDDATACOLLECTOR_API_KEY```: Specify the obtained API key.  
    ```WORDDATACOLLECTOR_API_KEY```: Specifies the path to the directory where data is saved when the tool is executed.   

3. Let's run the [sample code](https://github.com/dsonoda/word-data-collector/blob/master/word-data-collector/examples.py).  

    ```bash
    $ cd path/to/word-data-collector
    $ pipenv shell
    (word-data-collector) bash-3.2$ python examples.py
    ```

    Make sure the data file is downloaded to the designated storage directory.

    ```
    path/to/save directory
        +/image
            +/mountain
                 +/6cb7b02f124563ed2caad342f52043ac.jpg
                 +/a4facbd4d80a9b1c6bc0f9ce7ed87e78.jpg
        +/translation
            +/mountain
                 +/translation.json
        +/voice
            +/mountain
                 +/voice.mp3
        +/word
            +/mountain
                 +/word.json
    ```


# Note
Please note that you will be charged automatically if you exceed the free limit of the API.  
 
# Author
* [Daisuke Sonoda](https://daisukesonoda.com/) / Freelance Software Engineer  
* [mail@daisukesonoda.com](mail@daisukesonoda.com)  
* [@d5onoda](https://twitter.com/d5onoda)  
 
# License
"word-data-collector" is under [GNU GENERAL PUBLIC LICENSE](https://github.com/dsonoda/word-data-collector/blob/master/LICENSE).
