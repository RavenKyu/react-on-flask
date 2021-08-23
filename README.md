# React On Flask
This project is for user who wants to use `React` on `Python Flask`.

## Work Process
### Install and Build React Project
```sh
cd web
yarn install
yarn build
```

### Run Flask 
```sh
# default option
python -m app 

# with options
python -m app -a 0.0.0.0 -p 5000 --debug
```

## Docker
### Build
```sh
docker build -t react-flask:latest .               
```
### Run
```sh
docker run -it --rm -p 5000:5000 react-flask:latest
```

### Run for Development
```sh
docker run -it --rm -p 5000:5000 -v $(pwd)/app:/root/app react-flask:latest
```