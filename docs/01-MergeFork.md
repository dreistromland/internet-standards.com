# Update from internetstandards/Internet.nl.git  


```sh
git remote add upstream https://github.com/internetstandards/Internet.nl.git
git fetch --all
git checkout main
git rebase upstream/main
git push origin main -ff

git checkout version/1.x.x/adaptive_apollo
git rebase main
git push -f origin version/1.x.x/adaptive_apollo -ff
```

# install dev

Create file `docker/local.env` with this content:

```
INTERNETNL_BRANDING=False
LANGUAGES=de
```

```sh
sudo apt-get install inotify-tools
GIT_LFS_SKIP_SMUDGE=1 git submodule update --init
make build
```

# start dev

```sh
make up env=develop
# the wait for the services, then laucnh the frontend
bin/watch
xdg-open http://localhost:8080
```

# shutdown dev

```sh
make stop env=develop
# or if you want to remove persisted data
# make down-remove-volumes env=develop
```
