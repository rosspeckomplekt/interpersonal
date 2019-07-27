#!/usr/bin/env bash

# setup_os.sh
# The setup for installing core dependencies based on OS:
# python3 and pip3
# This setup is stored in a separate script
# because it is distinguished by its being
# OS-dependent: eg, Linux and Mac is different

echo "Welcome to setup_os.sh"
echo "Installing OS-dependent dependencies..."

if [[ "$OSTYPE" == "linux-gnu" ]]; then
	# Linux
	echo "Installing dependencies for Linux OS..."
	# setup for Ubuntu
	sudo apt install -y python3 python-pip3


elif [[ "$OSTYPE" == "darwin"* ]]; then
	# Mac OSX
	echo "Installing dependencies for Mac OSX..."

	# Handle the installation or updating of Homebrew
	which -s brew
	if [[ $? != 0 ]] ; then
		echo "Homebrew is not installed"
		echo "Installing Homebrew..."
		# Install Homebrew
		# ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		echo "Downloading Homebrew into ~/.brew"
		mkdir $HOME/.brew && curl -fsSL https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C $HOME/.brew
		mkdir -p /tmp/.$(whoami)-brew-locks
		mkdir -p $HOME/.brew/var/homebrew
		ln -s /tmp/.$(whoami)-brew-locks $HOME/.brew/var/homebrew/locks
		export PATH="$HOME/.brew/bin:$PATH"
		echo "Updating Homebrew..."
		brew update && brew upgrade
	else
		echo "Homebrew is installed"
		echo "Updating Homebrew..."
		brew update
	fi

	# Check whether Python 3 and Pip 3 are installed
	# If they are not installed, we install them

	if command -v python3 &>/dev/null; then
		echo Python 3 is installed
		if command -v pip3 &>/dev/null; then
			echo Pip 3 is installed
		else
			echo Pip 3 is not installed
			brew install python3
		fi
	else
		echo Python 3 is not installed
		brew install python3;
	fi


elif [[ "$OSTYPE" == "cygwin" ]]; then
	# POSIX compatibility layer and Linux environment emulation for Windows
	echo "cygwin setup is not supported"
elif [[ "$OSTYPE" == "msys" ]]; then
	# Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
	echo "MinGW setup is not supported"
elif [[ "$OSTYPE" == "win32" ]]; then
	# I'm not sure this can happen.
	echo "win32 setup is not supported"

elif [[ "$OSTYPE" == "freebsd"* ]]; then
	# FreeBSD
	echo "freebsd setup is not supported"
else
	# Unknown.
	echo "unknown operating system setup is not supported"
fi

