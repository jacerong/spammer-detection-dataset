### Description
Spammer detection with 5, 10, 20, and 40 tweets; this is, features are computed from the 5, 10, 20 and 40 most recent tweets from each user.

### Files
1. **%i-tweets/dataset.dat**: the i-th row in the file corresponds to the feature vector computed for the i-th user. Columns are whitespace-separated. The decimal separator character used is the dot (.). Data-type is float with a 10-decimal precision.
2. **%i-tweets/labels.dat**: the i-th row in the file corresponds to the user class (i.e., 0 for spammer and 1 for non-spammer) for the i-th row in the dataset.dat file.
3. **%i-tweets/unlabeled_dataset.dat**: different from the **%i-tweets/dataset.dat** file, the i-th user, whose feature vector corresponds to the i-th row in the file, does not have an user class.

Where,
* _%i_ is the number of most recent tweets used to compute the features.

### Features
1. description: when 1, indicates that the user has entered a profile description.
2. verified: when 1, "indicates that the user has a verified account."
3. age of the user account (in days).
4. number of followings.
5. number of followers.
6. reputation = (number of followers) / (number of followings + number of followers).
7. user mention (@) ratio.
8. unique user mention (@) ratio.
9. URL ratio.
10. hashtag (#) ratio.
11. average of tweet content similarity.
12. retweet rate.
13. reply rate.
14. number of tweets.
15. mean of inter-tweeting delay.
16. standard deviation of inter-tweeting delay.
17. average of tweets per day.
18. average of tweets per week.
19. number of tweets from manual devices (see note 1).
20. number of tweets from automated devices (see note 1).
21. fofo rate = number of followers / number of followings.
22. following rate = number of followings / age of the user account (in days).
23. percentage of tweets posted during the 00:00:00 at 02:59:59 hours period.
24. percentage of tweets posted during the 03:00:00 at 05:59:59 hours period.
25. percentage of tweets posted during the 06:00:00 at 08:59:59 hours period.
26. percentage of tweets posted during the 09:00:00 at 11:59:59 hours period.
27. percentage of tweets posted during the 12:00:00 at 14:59:59 hours period.
28. percentage of tweets posted during the 15:00:00 at 17:59:59 hours period.
29. percentage of tweets posted during the 18:00:00 at 20:59:59 hours period.
30. percentage of tweets posted during the 21:00:00 at 23:59:59 hours period.

#### Notes

1. A python script (utils/source_classification.py) was developed to classify tweeting sources into manual and automated.

