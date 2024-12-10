### 3 December 2024
1. Some terminologies
   1. **Method**: A function that is associated with a certain class
   2. **Object**: A concept of some sort which holds data about itself, or has attributes, and defines functions (methods) for data manipulation
   2. **Attributes**: Data of oneself
   3. **Constructor**: It is a special function or a method used in creation or initialization of an object in a class. It holds the initial state of the object. Read [here](https://www.geeksforgeeks.org/constructors-in-python/)
2. Why do we need object-oriented programming (OOP)? Read more [here](https://www.coursera.org/articles/object-oriented-programming-languages).
   1. OOP is necessary in achieving four elements in programming, which are (i) abstraction, (ii) polymorphism, and (iii) inheritance, and (iv) encapsulation.
   2. Abstraction: OOP hides the implementation part by only showing essential information to interact with it. Reduces code complexity.
   3. Polymorphism: From combination of two Greek words ("poly" as in many) and ("morphe" as in form), it refers to the concept of code which can take many forms. Or in other words, this would mean to coding flexibility. Discussion on Stack Overflow [here](https://stackoverflow.com/questions/2438695/where-did-the-term-polymorphism-come-from)
   4. Inheritance: From root word "inherit", which is to have the characteristic of some parent code. This refers to the ability to extend the code characteristics as however we desire without necessitating for ground-up re-coding.
   5. Encapsulation: From root word "encapsulate", this term refers to the technique of bundling the data and codes into a singular block. Although it helps in reducing the clutter and code complexity, the difference between encapsulation and abstraction is that it refers to the coding structure that protects the data from tampering. We shall see that we can use decorator to utilise write-protected property for some variables/lists. Read more [here](https://stackify.com/oop-concept-for-beginners-what-is-encapsulation/)
   6. OOP is important in order to achieve code reusability, better test and debugging, and flexibility.
2. Comparison between public and private class.
   1. Public class: The methods or fields of the class are accessible from any part of the program. 
   2. Private class: The methods or fields of the class can only be accessed within the same class of which they are declared.
   3. Additional access modifier, protected access: Similar to private class, methods and fields are only accessible in the same class which it is being declared. However, on top of that, they are also protected.
3. What are the magic method?
   1. __init__
      1. This magic method uses is used to initialise new instance for a class which it is nested in.
      2. This is also known as constructor 
   2. __call__
      1. 
   3. __str__
4. class method, static method, property
   1. @classmethod
      1. Declared using decorator @classmethod .
      2. This inbuilt function is used to elevate a method within a class, which is usually bounded to an instance inside the class, to the whole class.
      3. Invocation syntax is **class.classmethod()**
   2. @staticmethod
      1. Similar to @classmethod, it is also used to declare a method that belongs to the class rather to an instance within the class.
   3. @property (Read more [here](https://www.freecodecamp.org/news/python-property-decorator/))
      1. This decorator is used to give certain methods the ability to behave as setters, getters, or deleters. 
   4. @setter
      1. This decorator sets the value of an attribute.
      2. When a protected attribute is declared as an attribute, it is supposed to be accessed using getter.
5. Declaration of private instance using "_" prefix
6. Inheritance, or subclass, or child-class
7. How can we copy parent attribute?