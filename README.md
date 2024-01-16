0x00. AirBnB clone - The console

__________Brief____________

| This README file will contain description, all informations, materials...
used in this project and i'll do my best to explain this project in details |

______________Description_______________

- By: Guillaume
- Weight: 5
- Project to be done in teams of 2 people (your team: Yasser CHOUHAD, khawla Hili)

______________General_______________

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

_______________Packages__________________

- Dotted method :
We use the doted notation to do the import.
import my_math.abs
my_math.abs.my_abs(89)
Let's say the structure of our folder is the following: script.py
model/
|__ add.py
in order to import our function from the add.py file, we need to do the following statements. import model.add In this case we need to use our function like this :
model.add.add(9)
But the best way to do it is the following :
from model.add import add add(9)
- Import *   It is considered a bad practice, In that case __ init __ .py shouldn't be empty but must contain the list of modules to load.
The reason for that being the conflict that may emerge in that case, especially in cases where the code base is large. Keep in mind that readability and maintainability will be difficult, for anyone reading the code it will be hard to figure out where do the symbols come from.


CMD MODEL

It's a way to create an interactive shell that allows users to interact with the program using commands. In order to use this model we need to create a subclass for it.

import cmd
class MyCmd(cmd.Cmd):
	prompt = ">>"
	#commad methods.
if __name__= "__main__":
	MyCmd().cmdloop()

- Inside the class we want to define methods for each command we want to use.
Example : command_name = ls;   method_name = do_ls
- In order to keep the looping in the interactive mode, we need to override the cmdloop method.
- Quitting is set by default in the Cmd framework. But we can make our own quit function.

SERIALIZATION AND DESERIALIZATION
Meaning to transform an object or a data to a format that can be easily stored and back. Meaning to transform an object to a dictionary. We do that by following several methods.

- The pickle model :
It is a model that we can use to perform serialization by using the method dumps().
serialized = pickle.dumps(obj)
And we do the opposite with the help of the loads() method.
deserialized = pickle.loads(serialized)
Note : When using pickle to serialize an object, the object will be serialized into a non human readable code, not the same as what happens with JSON. This model transforms the object into something like the following : b'\x80\x04\x95.\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x07MyClass\x94\x93\x94)\x81\x94}\x94\x8c\x04data\x94\x8c\x05Hello\x94sb.'
When we call for pickle.loads to deserialize, we get the following :
<__main__.MyClass object at 0x7f8eed56a6d0>
- Xml, YAML or JSON :
In our case we will be using JSON, which goes the same as the pickle model. serialized = json.dumps(obj.__dict__) deserialized = json.loads(serialized) Keep in mind the _ _ dict _ _ Dunder is used to access the attributes and the properties of a given object. That way we will be able to convert the object into a dictionary. But a better approach would be to define a method within the class that returns a dictionary. In serialization the object will be transformed to a dictionary and it'll look like this : {"data": "Hello"}.

The importancy of this process shows in cases where we want to exchange data and communicate between different systems.
It is efficient for data storage, take for example the case where we want to keep our objects saved in a file, that way it will be important to serialize them and save them.
Another case is when we want to send data across a network, serialization transforms the data into a format that can be transmitted efficiently.
Data persistence is also one of the reason, it is basically keeping a state of data stored so that it can be restored later when the program reopens. And an example of that would be game.
Portability meaning that serialized data in a programming language x, can be deserialized using another y.
Add to that the quick retrieval of data when needed.

EXAMPLES :

- Databases_ : We can use this process of serialization and deserialization as a way to manipulate databases (files).
- Game state saving_ : Our game has to have the option of saving the current state, where we save the level that the player reached and the positioning of the characters.
- Data exchange between languages_ : Given a case of two incompatible languages but we want to use the objects we created in the first language with in a program created with another language.
- Configuration files_ : These types of files require a state saving, where we save the last modification done, and it makes perfect sense to use serialization and deserialization to do this.

HANDLING ARGUMENTS
When we talk about names arguments we simply mean **kwargs, while when we talk about positional arguments we are describing *args.

- Named arguments * kwargs / They are arguments given in the function call with the names of the attributes.
func(name: "Person", age: 11)
The * kwargs are given as a dictionary. They can have a default value if none was given.
def fun(kwarg1=None, kwarg2=60)
- Positional arguments * args / They are arguments given without specifying the names of the attributes. func("Person", 11) They must be provided before the named arguments if they were both mixed in a function call or in a function declaration. And different to named arguments they can not have a default value.

DATETIME MODEL
This model is very beneficial as it can be used to include the date and the time in our program. we can use import datetime but what is even better as we said in the import section is from datetime import datetime with that we import the exact class we need. datetime class unable us to work with the date and the time. But we can chose to specify further.
from datetime import date Or from datetime import time
What we can do with that is to display the time or the date or both in the wanted format. We can go a few steps further and perform arithmetics on the date and the time. In order to do that we're required to import the following :
from datetime import datetime, timedelta, and with that we can perform things such as :
future_datetime = datetime.now() + timedelta(days=7)
Notice how the timedelta constructor method uses * kwargs, we can also use them to define time components such as days, seconds, microseconds, milliseconds....