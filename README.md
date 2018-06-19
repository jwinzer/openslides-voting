# openslides-voting
Voting plugin for OpenSlides. Successor of `openslides-votecollector`.

## Features

- Supports the [VoteCollector](http://www.voteworks.de/en/ARS-Applications/General-Assembly/VoteCollector-OpenSlides-oxid-6.html)
- Named voting for all delegates
- Token based anonymous voting
- Old-style analog voting
- Vote for motions and elections
- Voting shares, mandates and absentee votes

## Voting modes

On creation of any poll (motions and election) you will be ask which voting mode
this poll has. You can choose between four modes:

1. **analog voting**: Just enter the offline counted votes, so the assembly can
   see the result.
2. **named electronic voting**: Every delegate can vote inside of OpenSlides.
   The name is saved to the vote. This can be pseudo-anonymized later (delete
   the association between user and the vote, but remember, there might be ways
   to reconstruct it later)
3. **token based electronic voting**: This is a mode for polling booths. There
   have to be a few voting machines, where a delegate can vote, if he enters a
   valid token. The tokens can be randomly generated by a voting manager and
   after authenticating the delegate, he give him the active token, so he can
   vote. To check the vote, the delegate get a result number. It is easy to
   remember and shortly after a voting one manager should print out the list of
   all votes, so one can validate his vote.
4. **votecollector**: If you have voting devices that supports the
   votecollector, you can enable the otecollector mode in the settings. Note
   that not all voting methods (like yes/no/abstain for multiple candidates) are
   supported by the votecollector. See more below.

## Hint for the token based voting
The voting machine has to have a user logged in, so OpenSlides can validate, if
a vote comes from an authorized computer. The user should only have three
permissions: `Can see motions`, `Can see assignments` and `Can see the token
voting interface`. Do not give any delegate the last permission. If a user has
this one, his interface will change, so he just can vote but not user
OpenSlides.

If anyone should be allowed to vote at their own computer, please make a voting
user with a simple password and distribute that, so a user has to login
seperatly to vote. Note, that this may reveal the users vote, because one can
check from which computer did come the vote and check, if a user was logged in
on the computer before.

## Votecollector supported voting modes
- YNA for motions
- YN(A) for an election with just one candidate
- Choose one from many candidates from an election

Not supported is YN(A) for multiple candidates.

## Settings

`VOTING_RESULT_TOKEN_TIMEOUT`: The timeout in seconds until vote success view is
closed dureng token voting. This is important, so the next one cannot get the
result token, if the user didn't click on continue. This can be disabled, when
setting the timeout to 0.

## Development
For development the easiest way is to set up Openslides as described for
development. Then fork this repository and clone it next to OpenSlides. Create a
symlink from the `openslides_voting` folder into the `OpenSlides` folder from
the main OpenSlides repo:
```
ls -s /<full path>/openslides-voting/openslides_voting /<full path>/OpenSlides/openslides_voting
```
Add `openslides_voting` in your `settings.py` to `INSTALLED_PLUGINS`.

Then, from the `openslides-voting` directory, run `yarn` and for further
development a watcher:
```
node_modules/.bin/gulp watch
```

Happy Contributing!
