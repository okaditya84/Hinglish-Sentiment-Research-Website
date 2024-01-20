
# Hinglish Sentiment Research

This is a Research project based on procturing unique method to collect and process data on Hinglish text sentences. 
There is a limitation on availability of quality data on the same, so this project focuses to develop a method to gather significant quantity of the data and process it to do sentiment analysis on it.

The method of approach is iterative training and testing of ML models on small chunk of manually corrected sentences and then exponentially integrating the output labels to the original dataset, thus increasing the size for ease in further analysis. 


The initial sentiment labelling is done by 3 pre-trained models hosted at hugging face (RoBerTa, Vader, Beto) and then we apply conditional programming to correctly label the predicted output of the model.

#### Results: We were able to develop more than 18000 rows of Hinglish sentences with the labelling accuracy of 90%.

#### Use case: This can be easily integrated as an embedded module or as an API with many social media platforms like Instagram, Youtube, Facebook, Twitter, Reddit etc. with a purpose of making the platforms cleaner with automation.

#### Further aim: We aim to expand the domain from just Hinglish, to various other indic and foreign languages of which the data availability is less.