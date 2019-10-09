SHELL:=/bin/bash

# install Rustup if you dont already have it
rustup:
	curl https://sh.rustup.rs -sSf | sh

# update Rustup if you already have it
update:
	rustup update
	rustup self update

# compile and run the project
run:
	cargo build 
	target/debug/fasta-counter hg19.snippet.fasta
