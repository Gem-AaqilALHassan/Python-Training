# Logging is useful to track the error or exception or information. It also helps in debugging.
# Basically logging se ek log file bnta hai (Log file) jisme error and exception ki details rehti hai taaki hm future referenece ke liye use kr skte hai
# We use Logging Module to log the error in python

# basicConfig(**kwargs) -- This method is used to configure the logging system
# getLogger() -- This method returns a logger with specified name, or if no name it returns the root
# info(msg) -- This will log a message with level 'INFO' on this logger -- level btayega ki error kitna bada hai jaise warning hai ya error like that
# error(msg) , warning(msg), critical(msg), exception(msg)

from logging import *

#These all will be show in console
# info("This is information")
# debug("This is debug") 
# warning("this is warning")
# error("This is error")
# critical("This is critical")
# exception("This is exception")

# By default levels below warning will not be visible like info and debug while other than that everything will be displayed.

#Now we hqve to do all these in a file

basicConfig(filename='logfile.log', 
	        level=DEBUG, #level is used to set i.e it will show debug and all i.e. info, debug, error,etc. 
	        filemode='w', #Filemode is by default is append i.e old and new data whereas in r mode i.e read old will go and new will stay  
            format='%(asctime)s -- %(message)s -- %(lineno)d') # Format is used to show the time and date of the following

# The bwlow things will be saved in the file respectively
# info("This is information")
# debug("This is debug") 
# warning("this is warning")
# error("This is error")
# critical("This is critical")
# exception("This is exception")

# logger = getLogger('Geek')

# logger.info("This is information")
# logger.debug("This is debug") 
# logger.warning("this is warning")
# logger.error("This is error")
# logger.critical("This is critical")
# logger.exception("This is exception")