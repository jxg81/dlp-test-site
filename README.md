## DLP Test Site

Simple web page which accepts text input and/or file uploads for the purpose of testing inline data loss prevention (DLP).

Nothing is done with the data uploaded which will be discarded at the conclusion of each transaction. After submission if the content is not blocked by the inline DLP a simple page will be displayed that lists the filename provided and/or the text entered into the text box.

Site is written using python/flask and can be easily deployed to any serverless hosting provider. Code includes config for turnkey deployment to Vercel (vercel.json).

The site also includes a random data generation tool to generate test data sets for dlp testing