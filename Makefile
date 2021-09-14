all: commit push

commit :
	git add -A
	git commit -m "Automatic Commit Message"

push:
	git push

pull:
	git pull
