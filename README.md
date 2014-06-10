mail2todotxt
============

This program can be integrated into Claws-Mail to transfer a mail to a ToDo.txt item with a link back to the original mail. By default it will use the Subject of the mail as task description. If you start the program with the parameter *"-i"* it will ask you for a task description and only fall back to the mail subject if no description is given.

To add the program to Claws-Mail go to *Configuration->Actions...* and create a action which executes following command:

```
/path_to_mail2todotxt/mail2todotxt.py -i %f &
```

Now you can create a task for the selected mail by calling *Tools-&gt;Actions-&gt;&lt;The_name_you_chose_for_the_action&gt;*. Additionally Claws-Mail also allows you to create a short-cut to execute the action.

To go back from the Mail to the ToDo.txt item you need this [ToDo.txt extensions](https://github.com/schiesbn/todotxt).
