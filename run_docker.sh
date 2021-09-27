JEKYLL_VERSION=4.0 docker run --rm -e "JEKYLL_ENV=docker" --name Simulationstechniken --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll jekyll serve --config _config.yml,_config.docker.yml
