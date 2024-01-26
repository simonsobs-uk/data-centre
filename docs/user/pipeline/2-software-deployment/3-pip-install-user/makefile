NAME=pip-install-user

.PHONY: submit tail clean
submit:
	condor_submit $(NAME).ini
tail:
	tail -F $(NAME).log $(NAME).out $(NAME).err
clean:
	rm -f $(NAME).log $(NAME).out $(NAME).err
