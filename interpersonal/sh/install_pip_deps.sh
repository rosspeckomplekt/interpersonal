#!/usr/bin/env bash

# install_pip_deps.sh
# the bare minimal and simple setup for installing pip dependencies
# used if you are just consuming the traits database we distribute (traits.db)
# if you want to generate the traits database,
#  use build_traits_database/run_populate_traits.sh

echo "Welcome to interpersonal-engine setup!"
echo "This script installs dependencies for interpersonal-engine"

echo "Installing pip dependencies..."
pip3 install --user -U gensim nltk sklearn numpy matplotlib tqdm
