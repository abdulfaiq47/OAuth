from flask import Flask, render_template, request, url_for, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

user={"admin":"1234"}

@app.route('/')
def index():
    return render_template("login.html")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username= request.form["username"]
        password = request.form["password"]

        if username in user and user[username] == password:
            session["user"] = username
            
            return redirect(url_for("chat"))
        else: 
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))
        

    return render_template("login.html")

@app.route("/chat" , methods=["GET","POST"])
def chat():
    if "user"  not in session:    
        return redirect(url_for("login"))
        
    response = ""
    if request.method == "POST":
        msg = request.form["message"]

        response = get_reply(msg)
    

        # Debug print statements here:
        print("Bot replied:", response)
    else:
        response = 'Hi! 👋 Type "info" to get more information.'
   

    return render_template("chat.html", username=session["user"], response=response)
    
def get_reply(msg):
    msg = msg.lower()  # lowercase for easy matching
    
# starting ai 
    if "info" in msg:
        return """  About This Bot <br>
This Python Assistant is an AI-driven tool that help you in learning, concept clarification and becoming proficient in Python programming. From a beginner trying to explore Python basics to a skilled programmer sharpening your expertise, this assistant is available to help you. <br> <br>
<h4>I will do my best to clarify the concepts of all these topics.</h4> 
<ol>
<li>String Concatenation</li>
<li>Variable</li>
<li>Datatype</li>
<li>Operators</li>
<li>If and Nested If</li>
<li>list</li>
<li>Dictionary</li>
<li>Try except</li>

</ol> <br><br><br>
<u></b>(Note: Simply type any of the topics listed above to get more details.)</b></u>"""
    elif "name" in msg:
        return "I'm PyBot, your chatbot friend."
    elif "how are you" in msg:
        return "I'm just a bunch of code, but I'm doing great!"
    elif "bye" in msg:
        return "Goodbye! Have a nice day."
    # try except
    elif "try except" in msg:
        return """<h3>try and except in Python (Definition):</h3>
The 'try' and 'except' block in Python is used for error handling. It lets you try to run code that might cause an error and catch the error with 'except' so the program doesn't crash. This is useful for managing unexpected situations like dividing by zero or accessing missing files.
<div class="code-block">
<pre><code id="codeBox">
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")
</code></pre>
<button onclick="copyCode()">Copy</button>
</div>"""
    # Dictionary
    elif "dictionary" in msg:
        return """<h3>Dictionary in Python (Definition):</h3>
A dictionary in Python is a collection of key-value pairs. Each item has a key and a value, and the keys must be unique. Dictionaries are unordered (before Python 3.7), changeable (mutable), and use curly braces '{}'.
<div class="code-block">
<code id="codeBox">
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])   # Output: Alice

person["age"] = 26      # Update value
person["email"] = "alice@example.com"  # Add new key-value pair

print(person)
</code>
<button onclick="copyCode()">Copy</button>

</div> 
<h3>Key Features of Dictionaries:</h3>
<ul>
<li>Use curly braces {} and colons : between keys and values</li>
<li>Keys must be unique and immutable (like strings or numbers)</li>
<li>Values can be of any type</li>"""
    # list
    elif "list" in msg:
        return """<h3>List in Python (Definition):</h3>
A list in Python is a collection of items that is ordered, changeable (mutable), and allows duplicate values. Lists can hold items of any data type, such as numbers, strings, or even other lists.
<div class="code-block">
<code id="codeBox">
fruits = ["apple", "banana", "mango"]
print(fruits[0])        # Output: apple
fruits.append("orange") # Adds "orange" to the list
print(fruits)           # Output: ['apple', 'banana', 'mango', 'orange']
</code>
<button onclick="copyCode()">Copy</button>

</div>
<h3>Key Features of Lists:</h3>
<ul>
<li>Use square brackets []</li>
<li>Items are indexed (starting from 0)</li>
<li>You can add, remove, or change items</li>
</ul>"""
    # If and nested if
    elif "if and nested if" in msg:
        return """<h3>If</h3>
        The 'if' statement in Python is used to check a condition and run a block of code only if the condition is true. It helps control what the program does based on certain situations.
<div class="code-block">
<code id="codeBox">
age = 18
if age >= 18:
print("You are eligible to vote.")

Output # you are eligible to vote

<button onclick="copyCode()">Copy</button>
</code>
</div>
<h3>Nested if</h3>
A nested if statement means placing one if statement inside another. It is used when one condition depends on another. The inner if only runs if the outer condition is also true.
<div class="code-block">
<code id="codeBox">
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote in the election.")

Output # You can vote in the election.
</code>
<button onclick="copyCode()">Copy</button>

</div>
"""

    # Datatype
    elif "datatype" in msg:
        return """<h3>Datatype</h3>
        Datatype in Python (Definition):
A datatype in Python defines the type of data a variable can hold. It tells Python what kind of value is stored, such as a number, text, list, or something else.
<div class="code-block"><pre>
<b>Built-in Datatypes in Python:</b>
Datatype	Description	                     Example
int	        Integer numbers	                 x = 10
float	    Decimal (floating-point) number  price = 19.99
str	        String (text) values	         name = "Alice"
bool	    Boolean (True or False)	         is_active = True
list	    Ordered, changeable collection	 fruits = ["apple", "mango"]
tuple	    Ordered, unchangeable collection coordinates = (10, 20)
dict	    Key-value pairs	                 user = {"name": "Bob"}
set	        Unordered, unique items	         colors = {"red", "blue"}
NoneType	Represents a null or no value	 x = None
<button onclick="copyCode()">Copy</button>
</pre>
</div>
"""
    # Variable
    elif "variable" in msg:
        return """<h3>Variable</h3>
        In Python, a variable is a named storage location in memory used to hold data values. It acts as a container for information that a program can use and manipulate.
        <div class="code-block">
        <code id="codeBox">
# Variable
name="Abdul Faiq"
print(name)
output # :Abdul Faiq

age="111"
class_="10"
field="Computer Science"

print(f'''     About Myself
Name:{name}
age:{age}
Class:{class_}
Field:{field}''')

output  #      About Myself

Name:Abdul Faiq
age:111
Class:10
Field:Computer Science

x=5
y=6
z=(x+y)
print(x+y)
print(z)

Output # 11
11
        <button onclick="copyCode()">Copy</button>
        </code>
        </div>


<b>Legal Variable in Python (Definition):</b>
A legal variable in Python is a name used to store data that follows all the rules of Python’s variable naming convention
<ul>

<li>Starts with a letter (A–Z or a–z) or an underscore (_)</li>
<li>Followed by letters, digits (0–9), or underscores</li>
<li>Does not use spaces or special characters (like @, -, #, etc.)</li>
<li>Is not a reserved keyword (like if, class, def, etc.)</li>
</ul>
<div class="code-block"><code>
username = "john"
_age = 30
user123 = "alice"
<button onclick="copyCode()">Copy</button>
</code>
</div>
<b>Illegal Variable in Python (Definition):</b>
An illegal variable in Python is a name that violates one or more of the naming rules, such as:
<ul>
<li>Starts with a number</li>

<li>Includes spaces or special characters</li>

<li>Uses a reserved keyword as its name</li>
</ul>
<div class="code-block"><code>
1name = "wrong"       # starts with a digit
first-name = "error"  # hyphen is not allowed
class = "test"        # 'class' is a reserved keyword
my var = "oops"       # space is not allowed
</code>
<button onclick="copyCode()">Copy</button>

</div>"""
    # String Concatenation
    elif "string concatenation" in msg:
        return """<h3>String Concatenation</h3>
        String concatenation in Python refers to the process of combining two or more strings into a single string. This operation is fundamental for manipulating textual data.
        <div class="code-block">
        <code id="codeBox">
first_name="abdul"
last_name="Faiq"

print(f'''my name is  {first_name} {last_name}''')

output # my name is  abdul Faiq

first_name="abdul"

last_name="Faiq"

print(f'''{first_name} {last_name}''')

output # abdul Faiq
first_name="Abdul"
last_name="Faiq"


print(first_name+" "+last_name)
output # Abdul Faiq
First_Name=input("Enter your First Name: ")
Last_Name=input("Enter your Last Name: ")
print(f'''My name is {First_Name} {Last_Name}.''')
output #  My name is Abdul Faiq.
</code>
        <button onclick="copyCode()">Copy</button>
        
        </di>"""
         
    # operators
    elif "identity operators" in msg:
        return """In Python, identity operators are used to check if two variables refer to the same object in memory, rather than if they have the same value. They don't compare the values of the variables, but rather their memory addresses. Python has two identity operators: 'is' and 'is not'<br><br>
        <b>'is' operator:</b>
        <br>
        <ul>
        <li>Evaluates to 'True' if the variables on either side of the operator point to the same object in memory.</li>
        <li>Evaluates to 'False' otherwise. </li>
        <div class="code-block">
        <code id="codeBox">
x = 5
y = 5
z = 7

print(x is y)  # Output: True (both x and y refer to the same object in memory)
v
print(x is z)  # Output: False (x and z refer to different objects)

print(x is not y) # Output: False

print(x is not z) # Output: True
</code>
        <button onclick="copyCode()">Copy</button>
        
        </div>"""
    
    elif "logical operators" in msg:
        return """Here is information about Python logical operators.
Python has three logical operators: and, or, and not. They are used to combine or modify Boolean expressions (expressions that evaluate to either True or False).
<ul>
<li>'and': Returns True if both operands are True, otherwise returns False.</li>
<div class="code-block">
<code id="codeBox">
    x = 5
    print(x > 0 and x < 10) # Output: True
    print(x > 0 and x > 10) # Output: False
    <button onclick="copyCode()">Copy</button>
    </code>
    </div>
<li> or: Returns True if at least one operand is True, otherwise returns False.</li>  
<div class="code-block"><code>
    x = 5
    print(x < 0 or x < 10) # Output: True
    print(x < 0 or x > 10) # Output: False
    <button onclick="copyCode()">Copy</button>
    </code>
    </div>
<li> not: Returns the opposite Boolean value of the operand. If the operand is True, it returns False, and vice versa.</li> 
<div class="code-block"><code>
    x = 5
    print(not(x < 0)) # Output: True
    print(not(x > 0)) # Output: False
    </code>
    <button onclick="copyCode()">Copy</button>
    
    </div>


"""

    elif "comparison operators" in msg:
        return """<h3>Comparison Operators:</h3> 
        Comparison operators in Python are used to compare values. They return a Boolean value (True or False) based on the comparison result. Here's a breakdown of the common comparison operators
        <div class="code-block"><ul>
 <li>== (Equal to): Checks if two values are equal.</li>
 <li>!= (Not equal to): Checks if two values are not equal.</li>
 <li>> (Greater than): Checks if the left value is greater than the right value. </li>
 <li>< (Less than): Checks if the left value is less than the right value.</li>
 <li>>= (Greater than or equal to): Checks if the left value is greater than or equal to the right value. </li>
 <li><= (Less than or equal to): Checks if the left value is less than or equal to the right value.</li>  </ul>
<button onclick="copyCode()">Copy</button>
    </div>"""
    elif "assignment operators" in msg:
        return """Assignment operators are used to assign values to variables <br> 
        <div class="code-block">
        <pre>
Operator|	  Meaning	                                Equivalent to
=	    |    Assign value	                            x = 5
+=	    |    Add and assign	                            x += 3 → x = x + 3
-=	    |    Subtract and assign	                    x -= 3 → x = x - 3
*=	    |    Multiply and assign	                    x *= 3 → x = x * 3
/=	    |    Divide and assign	                        x /= 3 → x = x / 3
%=	    |    Modulus and assign	                        x %= 3 → x = x % 3
//=	    |    Floor divide and assign	                x //= 3 → x = x // 3
**=	    |    Power and assign	                        x **= 3 → x = x ** 3
&=	    |    Bitwise AND and assign	                    x &= 3 → x = x & 3
^=	    |    Bitwise XOR and assign	                    x ^= 3 → x = x ^ 3
>>=	    |    Bitwise right shift and assign	            x >>= 3 → x = x >> 3
<<=	    |    Bitwise left shift and assign	            x <<= 3 → x = x << 3
:=	    |    Walrus operator – Assign inside expression	print(x := 3) (assigns and prints)
 
</pre> 
<button onclick="copyCode()">Copy</button>
    </div> """
    elif "arithmetic operators" in msg:
        return """Arithmetic operators in Python programming are used to perform basic mathematical calculations of two operands. They include addition, subtraction, division, multiplication, and more.
        <h3>  1. Addition</h3>
        <div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Addition
# Addition – Adds two values
x = 5
y = 3
print(x + y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div> 
 <br>
 <h3>   2. Subtraction </h3>
 <div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Subtraction
# Subtraction – Subtracts right from left
x = 5
y = 3
print(x - y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div>
 <h3>   3. Multiplication </h3>
 <div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Multiplication
# Multiplication – Multiplies two values
x = 5
y = 3
print(x * y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div>
<h3>   4. Division </h3>
<div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Division
# Division – Divides left by right (float result
x = 5
y = 3
print(x / y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div>
 <h3>   5. Modulus </h3>
 <div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Modulus
# Modulus – Returns the remainder
x = 5
y = 3
print(x % y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div>
 <h3>   6. Exponentiation </h3>
 <div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Exponentiation
# Exponentiation – Raises left to the power of right
x = 5
y = 3
print(x ** y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div>
 <h3>   7. Floor division </h3>
 <div class="code-block">
         <pre><code id="codeBox"> 
#  Python Arithmetic Floor division
# Floor Division – Divides and rounds down to nearest whole number
x = 5
y = 3
print(x - y)</code></pre>
<button onclick="copyCode()">Copy</button>
 </div>
 """
    elif "operators" in msg:
        return """ Python Operators       
<pre>Operators are used to perform operations 
on variables and values.

In the example
below, we use the + operator 
to add together two values:

Example:
print(10 + 5)
Python divides the operators in the 
following groups:

Arithmetic operators (type'Arithmetic
operators')
Assignment operators (type'Assignment
operators')
Comparison operators (type'Comparison
operators')
Logical operators (type' Logical
operators')
Identity operators(type' Identity
operators')

</pre>
"""
    
    else:
        return "Sorry, I didn't understand that."
    



# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=3000)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

