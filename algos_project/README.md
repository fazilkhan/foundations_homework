#Algos Project

I came across this dataset that collected all the newsletters sent out by House representatives to their constituents (those who had subscribed). The people who had collated this massive dataset had started the project back in 2010.

I specifically looked at newsletters sent out between February 2020 and December 2020 to see how often the newsletter mentioned coronavirus/COVID-19 during this period. I had more than 17,000 newsletters which I downloaded as .csvs and imported to the Jupyter notebook.

Then I scraped the names of the representatives associated with the IDs that were assigned to the newsletters and merged the two dataframes. Then I labeled a little over 100 of the newsletters based on whether it mentioned anything related to COVID-19. I Used a bunch of classifers and DecisionTree gave me the best results.

I applied the model to my main dataframe and found that out of over 17,000 nesletters sent out by these representatives between February 2020 and December 2020, a little more than 12,000 mentioned coronavirus and and the COVID-19 pandemic in some way or the other.

I might do an additional analysis and look at this data on party and state lines.