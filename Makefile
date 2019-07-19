install:
	cp remind.py /usr/local/bin/remind
	chmod u+x /usr/local/bin/remind
	touch ~/.config/.remind

uninstall:
	rm /usr/local/bin/remind
