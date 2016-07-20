### Description
Spammer detection with no tweets; this is, only user-based features are computed.

### Files
1. **dataset.dat**: the i-th row in the file corresponds to the feature vector computed for the i-th user. Columns are whitespace-separated. The decimal separator character used is the dot (.). Data-type is float with a 10-decimal precision.
2. **labels.dat**: the i-th row in the file corresponds to the user class (i.e., 0 for spammer and 1 for non-spammer) for the i-th row in the dataset.dat file.
3. **unlabeled_dataset.dat**: different from the **dataset.dat** file, the i-th user, whose feature vector corresponds to the i-th row in the file, does not have an user class.

### Features
1. default profile: when 1, "indicates that the user has not altered the theme or background of their user profile."
2. default profile image: when 1, "indicates that the user has not uploaded their own avatar and a default egg avatar is used instead."
3. description: when 1, indicates that the user has entered a profile description.
4. location: when 1, indicates that account's profile has an user-defined location.
5. url: when 1, the user has provided an URL in association with its profile.
6. verified: when 1, "indicates that the user has a verified account."
7. age of the user account (in days).
8. number of followings.
9. number of followers.
10. reputation = (number of followers) / (number of followings + number of followers).
11. number of tweets.
12. publication rate = number of tweets / age of the user account (in days).
13. fofo rate = number of followers / number of followings.
14. following rate = number of followings / age of the user account (in days).

