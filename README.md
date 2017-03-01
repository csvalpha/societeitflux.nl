# How to deploy
1. Add the 'fatima' remote to the git config. Go to the .git/config file and add the following:
```
[remote "fatima"]
	url = ict@csvalpha.nl:/opt/projects/flux-website
	fetch = +refs/heads/*:refs/remotes/fatima/*
```

1. Push your changes to the fatima remote using: `git push fatima master:live` 
1. Push your changes to bitbucket using:  `git push origin master`
