from django.core.management.base import BaseCommand
from courses.models import Course
from lessons.models import Lesson
from tests.models import Test

class Command(BaseCommand):
    help = 'Seeds the database with initial course data'

    def handle(self, *args, **kwargs):
        # Course.objects.create(
        #     id = 1,
        #     name = "C++",
        #     description = "Dive into the world of C++, a powerful, high-performance language widely used in software development, game programming, and systems programming. This course covers essential concepts from basic syntax to advanced topics like object-oriented programming, memory management, and multi-threading. By the end of this course, you'll be equipped to build robust applications, optimize performance, and tackle complex programming challenges with confidence."
        # )
        # Course.objects.create(
        #     id = 2,
        #     name = "C#",
        #     description = "Unlock the potential of C#, the language of choice for developing Windows applications, games using Unity, and enterprise-level software. This course offers a comprehensive guide from the basics of C# syntax to advanced features like LINQ, asynchronous programming, and .NET framework integration. Whether you're building desktop applications, web services, or games, this course will give you the skills needed to succeed."
        # )
        # Course.objects.create(
        #     id = 3,
        #     name = "Java",
        #     description = "Explore the versatile world of Java, a language that powers millions of devices and applications globally. This course is designed to take you from the fundamentals of Java programming to advanced topics like multithreading, data structures, and web application development. Perfect for aspiring developers, this course will prepare you for building scalable, high-performance applications for desktop, web, and mobile platforms."
        # )
        # Course.objects.create(
        #     id = 4,
        #     name = "Python",
        #     description = "Step into the world of Python, a versatile and beginner-friendly language that's in high demand across various industries. This course provides a solid foundation in Python programming, covering everything from basic syntax to advanced topics like web development, data analysis, and machine learning. Whether you're a novice or an experienced developer, this course will help you harness the full power of Python."
        # )
        # Course.objects.create(
        #     id = 5,
        #     name = "Ruby",
        #     description = "Learn Ruby, the elegant and expressive language that powers web applications like Twitter and GitHub. This course is designed for beginners and experienced programmers alike, guiding you through Ruby's unique syntax and features. From building simple scripts to developing full-fledged web applications with Ruby on Rails, this course will equip you with the skills to write clean, maintainable code."
        # )
        # Course.objects.create(
        #     id = 6,
        #     name = "PHP",
        #     description = "Master PHP, the language that powers over 75% of the web, including platforms like WordPress and Facebook. This course offers a complete guide to PHP, from basic syntax to advanced web development techniques. You'll learn how to build dynamic, database-driven websites, implement security best practices, and integrate with other web technologies. Ideal for aspiring web developers, this course will help you create robust and scalable web applications."
        # )

        # # C++
        # Lesson.objects.create(
        #     id = 1,
        #     title = "Introduction to C++ Syntax and Structure",
        #     info = "C++ is a versatile, high-performance programming language that extends C by adding object-oriented features. The basic structure of a C++ program starts with the #include directive for including libraries, followed by the main() function, which serves as the entry point. Statements end with semicolons, and the language supports various data types like int, float, and char. For handling input and output, C++ uses cin and cout, respectively. Comments can be added using // for single-line or /*...*/ for multi-line.",
        #     course_id = 1
        # )
        # Lesson.objects.create(
        #     id = 2,
        #     title = "Control Structures and Functions",
        #     info = "Control structures in C++ include loops (for, while, do-while), conditional statements (if, else, switch), and branching (break, continue, return). Functions are blocks of reusable code that can take parameters and return values. They help in organizing code and improving reusability. Functions in C++ can be declared before their use or defined inline, and the language supports both pass-by-value and pass-by-reference.",
        #     course_id = 1
        # )
        # Lesson.objects.create(
        #     id = 3,
        #     title = "Pointers, References, and Dynamic Memory",
        #     info = "Pointers are variables that store memory addresses, allowing direct manipulation of memory. They are crucial for dynamic memory management, which is handled through operators like new and delete. References are another way to access variables, similar to pointers but safer and more convenient. C++ supports dynamic memory allocation, enabling the creation of variables during runtime, which is essential for managing resources efficiently in larger applications.",
        #     course_id = 1
        # )
        # Lesson.objects.create(
        #     id = 4,
        #     title = "Object-Oriented Programming with C++",
        #     info = "C++ is known for its strong support for object-oriented programming (OOP), which revolves around concepts like classes and objects. A class is a blueprint for creating objects, encapsulating data, and functions. Key OOP principles in C++ include inheritance (extending classes), polymorphism (using a unified interface), and encapsulation (hiding data). These principles help in creating modular, scalable, and maintainable code.",
        #     course_id = 1
        # )
        # Lesson.objects.create(
        #     id = 5,
        #     title = "Templates and Standard Template Library (STL)",
        #     info = "Templates in C++ allow for generic programming, enabling functions and classes to operate with any data type. This is especially useful for creating flexible and reusable code. The Standard Template Library (STL) is a powerful feature of C++ that provides a collection of generic classes and functions, including containers (like vector, list, map), algorithms (like sorting, searching), and iterators. STL helps in reducing development time and improving code quality.",
        #     course_id = 1
        # )
        # Lesson.objects.create(
        #     id = 6,
        #     title = "Advanced Concepts: Multi-threading, Exception Handling",
        #     info = "C++ also offers advanced features like multi-threading and exception handling. Multi-threading allows for concurrent execution of code, improving performance in multi-core systems. The C++ standard library includes <thread>, <mutex>, and other utilities to manage threads and synchronization. Exception handling in C++ is done using try, catch, and throw blocks, allowing programs to handle errors gracefully without crashing. This ensures that resources are managed properly, even in the face of errors.",
        #     course_id = 1
        # )
        # # C#
        # Lesson.objects.create(
        #     id = 7,
        #     title = "Getting Started with C# and .NET Framework",
        #     info = "C# is a modern, object-oriented programming language developed by Microsoft as part of the .NET framework. It is designed for building a wide range of applications, from desktop to web to mobile. The .NET Framework provides a large library of pre-coded solutions to common programming tasks and manages the execution of programs written in C# through the Common Language Runtime (CLR). A basic C# program begins with the using directive to include necessary namespaces, followed by a namespace declaration, and the Main() method, which serves as the entry point. C# syntax is similar to other C-based languages, making it easy to learn for those familiar with C, C++, or Java.",
        #     course_id = 2
        # )
        # Lesson.objects.create(
        #     id = 8,
        #     title = "Object-Oriented Programming in C#",
        #     info = "C# is a fully object-oriented language, which means it supports key OOP principles like encapsulation, inheritance, and polymorphism. Classes and objects are the core building blocks. A class is a blueprint for creating objects (instances of classes). Encapsulation is achieved by keeping the data (attributes) and the methods (functions) that operate on the data together. Inheritance allows a new class to inherit the members of an existing class, promoting code reuse. Polymorphism enables methods to do different things based on the object they are acting upon, achieved through method overloading and overriding.",
        #     course_id = 2
        # )
        # Lesson.objects.create(
        #     id = 9,
        #     title = "Collections, Generics, and LINQ",
        #     info = "C# provides a robust set of collection classes in the System.Collections and System.Collections.Generic namespaces, including lists, dictionaries, queues, and stacks. These collections allow for the efficient storage and manipulation of groups of objects. Generics enhance collections by allowing them to operate with any data type while ensuring type safety. LINQ (Language Integrated Query) is a powerful feature in C# that allows developers to write queries directly in their code using a SQL-like syntax, making it easier to retrieve and manipulate data from various sources like arrays, collections, XML, and databases.",
        #     course_id = 2
        # )
        # Lesson.objects.create(
        #     id = 10,
        #     title = "Exception Handling and Debugging",
        #     info = "In C#, exception handling is a structured way to handle runtime errors, ensuring that the program can continue to run or fail gracefully. This is done using try, catch, finally, and throw statements. The try block contains the code that might cause an exception, the catch block handles the exception, and finally is used for cleanup code that should run regardless of whether an exception occurred. The throw statement is used to trigger an exception. Debugging tools in Visual Studio, such as breakpoints, watch windows, and step-through debugging, help developers identify and fix issues in their code efficiently.",
        #     course_id = 2
        # )
        # Lesson.objects.create(
        #     id = 11,
        #     title = "Asynchronous Programming with async and await",
        #     info = "Asynchronous programming in C# allows tasks to run concurrently, which improves the responsiveness of applications, especially those with I/O-bound operations like reading files, making web requests, or accessing databases. The async and await keywords are central to writing asynchronous code in C#. An async method runs asynchronously and can contain one or more await expressions that pause the method execution until the awaited task is completed. This approach makes it easier to write, read, and maintain asynchronous code without blocking the main thread, thus keeping the UI responsive.",
        #     course_id = 2
        # )
        # Lesson.objects.create(
        #     id = 12,
        #     title = "Developing Applications with Windows Forms and WPF",
        #     info = "C# is often used to develop desktop applications using Windows Forms or Windows Presentation Foundation (WPF). Windows Forms is a graphical API for creating rich desktop applications with event-driven programming, where controls like buttons, text boxes, and labels can be added to forms. WPF is a more modern and flexible framework that allows for the development of visually rich user interfaces using XAML (Extensible Application Markup Language). WPF supports advanced features like data binding, animation, and styles, making it ideal for creating complex and dynamic applications.",
        #     course_id = 2
        # )
        # # Java
        # Lesson.objects.create(
        #     id = 13,
        #     title = "Java Basics: Syntax, Data Types, and Operators",
        #     info = "Java is a widely-used, platform-independent programming language known for its portability and robustness. The syntax of Java is similar to C and C++, making it familiar to those who have experience with these languages. Java programs start with the public static void main(String[] args) method, which serves as the entry point. Data types in Java are categorized into primitive types (like int, float, char, boolean) and reference types (like arrays and objects). Java supports various operators including arithmetic (+, -, *, /), relational (==, !=, >, <), logical (&&, ||, !), and bitwise operators. Java’s strong typing and automatic memory management via garbage collection contribute to its stability and security.",
        #     course_id = 3
        # )
        # Lesson.objects.create(
        #     id = 14,
        #     title = "Object-Oriented Programming in Java",
        #     info = "Java is an object-oriented programming language, and its OOP features are fundamental to creating reusable and maintainable code. The four main principles of OOP in Java are encapsulation, inheritance, polymorphism, and abstraction. Encapsulation involves bundling the data (fields) and methods (functions) that operate on the data into a single unit, usually a class, and restricting access to some of the object's components. Inheritance allows one class to inherit fields and methods from another, promoting code reuse. Polymorphism enables objects to be treated as instances of their parent class, allowing for flexible code design through method overriding and overloading. Abstraction hides complex implementation details and exposes only the essential features of an object.",
        #     course_id = 3
        # )
        # Lesson.objects.create(
        #     id = 15,
        #     title = "Exception Handling and File I/O",
        #     info = "Java has a robust exception-handling mechanism that helps manage runtime errors, ensuring that programs can handle unexpected situations gracefully. This is done using try, catch, finally, and throw blocks. The try block contains the code that might throw an exception, while the catch block handles specific exceptions. The finally block is executed regardless of whether an exception is thrown, often used for resource cleanup. Java also provides extensive support for file input/output (I/O) operations through classes in the java.io and java.nio packages. These classes allow reading from and writing to files, handling streams, and performing other file operations efficiently.",
        #     course_id = 3
        # )
        # Lesson.objects.create(
        #     id = 16,
        #     title = "Multi-threading and Concurrency",
        #     info = "Java's multi-threading capabilities allow for the concurrent execution of two or more threads (lightweight processes), making programs more efficient, especially on multi-core systems. Java provides built-in support for multi-threading through the Thread class and the Runnable interface. Key concepts in multi-threading include thread creation, synchronization (using synchronized blocks or methods to prevent thread interference), and inter-thread communication. Concurrency utilities in the java.util.concurrent package provide higher-level abstractions like thread pools, executors, and locks, which simplify the development of concurrent applications.",
        #     course_id = 3
        # )
        # Lesson.objects.create(
        #     id = 17,
        #     title = "Data Structures and Algorithms in Java",
        #     info = "Java provides a rich set of data structures and algorithms through its Collections Framework, which includes interfaces like List, Set, Queue, and Map, and their implementations like ArrayList, HashSet, LinkedList, and HashMap. These data structures are essential for efficiently managing and organizing data. Algorithms such as sorting, searching, and iteration are built into the framework, making it easier to implement common operations. Java also supports custom implementations of data structures and algorithms, allowing developers to optimize performance for specific use cases.",
        #     course_id = 3
        # )
        # Lesson.objects.create(
        #     id = 18,
        #     title = "Introduction to Java Web Development: Servlets and JSP",
        #     info = "Java is a popular choice for building web applications, and two key technologies for server-side development are Servlets and JavaServer Pages (JSP). Servlets are Java classes that handle HTTP requests and responses, providing dynamic content to web clients. They are the foundation of Java web applications, and they run on a web server or application server. JSP is a technology that simplifies the creation of dynamic web content by allowing developers to embed Java code directly into HTML pages. JSP is compiled into Servlets by the server, combining the power of Java with the ease of creating web pages. Together, Servlets and JSP form a powerful combination for building robust, scalable web applications.",
        #     course_id = 3
        # )
        # # Python
        # Lesson.objects.create(
        #     id = 19,
        #     title = "Python Fundamentals: Variables, Data Types, and Control Flow",
        #     info = "Python is a high-level, interpreted programming language known for its readability and simplicity. Variables in Python are dynamically typed, meaning you do not need to declare their type explicitly. Common data types include integers, floats, strings, lists, tuples, dictionaries, and sets. Control flow in Python is managed through statements like if, elif, and else for conditional execution, as well as loops such as for and while for iteration. Python’s indentation-based syntax promotes clean and readable code, making it accessible for beginners and experienced programmers alike.",
        #     course_id = 4
        # )
        # Lesson.objects.create(
        #     id = 20,
        #     title = "Functions, Modules, and Packages",
        #     info = "Functions in Python are defined using the def keyword and can take parameters and return values. They promote code reusability and modularity. Python supports first-class functions, allowing functions to be passed as arguments, returned from other functions, and assigned to variables. Modules are Python files that contain definitions and statements, allowing for code organization. You can import modules using the import statement. Packages are collections of related modules, facilitating structured code organization. The Python Standard Library provides a wealth of built-in modules for various tasks, enhancing development efficiency.",
        #     course_id = 4
        # )
        # Lesson.objects.create(
        #     id = 21,
        #     title = "Working with Files and Exception Handling",
        #     info = "Python provides built-in functions for file handling, enabling reading from and writing to files easily using the open() function. File operations include reading, writing, and appending data, and files can be managed in different modes such as text and binary. Exception handling in Python is done using try, except, else, and finally blocks, allowing developers to handle errors gracefully without crashing the program. This mechanism helps in managing runtime errors effectively, ensuring that resources are properly cleaned up, regardless of whether an error occurred.",
        #     course_id = 4
        # )
        # Lesson.objects.create(
        #     id = 22,
        #     title = "Object-Oriented Programming in Python",
        #     info = "Python is an object-oriented language that supports the principles of encapsulation, inheritance, and polymorphism. Classes are defined using the class keyword, and objects are instances of these classes. Encapsulation in Python involves bundling data and methods within classes, restricting access to certain attributes. Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse. Polymorphism enables methods to be defined in a way that they can operate on different types of objects, facilitating flexible code design. Python also supports multiple inheritance, allowing a class to inherit from multiple parent classes.",
        #     course_id = 4
        # )
        # Lesson.objects.create(
        #     id = 23,
        #     title = "Web Development with Django and Flask",
        #     info = "Python is widely used for web development, with Django and Flask being two popular frameworks. Django is a high-level framework that promotes rapid development and clean design, featuring an ORM (Object-Relational Mapping) for database management, an admin interface, and built-in authentication. It follows the MVC (Model-View-Controller) architectural pattern. Flask, on the other hand, is a micro-framework that is lightweight and flexible, making it easy to get started with web applications. It provides the essentials for building web apps, allowing developers to add libraries and extensions as needed, thus giving them control over application design.",
        #     course_id = 4
        # )
        # Lesson.objects.create(
        #     id = 24,
        #     title = "Data Analysis and Visualization with Pandas and Matplotlib",
        #     info = "Python is a powerful tool for data analysis and visualization, with libraries like Pandas and Matplotlib being widely used. Pandas is a library that provides data structures like Series and DataFrames, enabling easy manipulation and analysis of structured data. It offers functions for data cleaning, filtering, aggregation, and merging, making it ideal for data manipulation tasks. Matplotlib is a plotting library that allows for the creation of static, interactive, and animated visualizations in Python. It supports various types of plots, including line charts, bar charts, histograms, and scatter plots, enabling effective data visualization to convey insights clearly.",
        #     course_id = 4
        # )
        # # Ruby
        # Lesson.objects.create(
        #     id = 25,
        #     title = "Introduction to Ruby Syntax and Data Types",
        #     info = "Ruby is a dynamic, object-oriented programming language known for its elegant syntax and flexibility. The basic structure of a Ruby program includes defining classes and methods, with everything being an object. Ruby uses a clear and concise syntax, where statements do not require semicolons at the end. Data types in Ruby include numbers (integers and floats), strings, symbols, arrays, hashes, and booleans. Ruby’s dynamic typing allows variables to change types easily, enhancing flexibility. Comments can be added using # for single-line comments and =begin and =end for multi-line comments.",
        #     course_id = 5
        # )
        # Lesson.objects.create(
        #     id = 26,
        #     title = "Control Structures and Loops",
        #     info = "Ruby provides various control structures to manage the flow of execution. Conditional statements like if, unless, elsif, and case enable branching logic based on conditions. Ruby supports several types of loops, including while, until, and for loops, as well as iterators like .each, which simplify iteration over collections. The break and next keywords allow for exiting loops or skipping to the next iteration, respectively. Ruby's flexible syntax makes it easy to implement complex control flow in a readable manner.",
        #     course_id = 5
        # )
        # Lesson.objects.create(
        #     id = 27,
        #     title = "Working with Arrays, Hashes, and Strings",
        #     info = "Arrays and hashes are fundamental data structures in Ruby. An array is an ordered collection of elements, allowing for easy storage and manipulation of lists. Methods like .push, .pop, .shift, and .map provide powerful tools for working with arrays. A hash is an unordered collection of key-value pairs, ideal for associating related data. Hashes can be created using {} and support various methods for manipulation. Ruby strings are mutable and come with numerous built-in methods for string manipulation, including concatenation, slicing, and formatting. String interpolation is a unique feature that allows for embedding variables directly within string literals.",
        #     course_id = 5
        # )
        # Lesson.objects.create(
        #     id = 28,
        #     title = "Object-Oriented Programming in Ruby",
        #     info = "Ruby is designed with object-oriented programming as a core principle. Classes are defined using the class keyword, and objects are instances of these classes. Ruby supports the four main OOP principles: encapsulation, inheritance, polymorphism, and abstraction. Encapsulation is achieved by using private and protected methods to restrict access to certain data. Inheritance allows a class to inherit methods and attributes from another class, facilitating code reuse. Polymorphism in Ruby enables objects to respond to the same method in different ways, while abstraction hides complex implementation details from the user.",
        #     course_id = 5
        # )
        # Lesson.objects.create(
        #     id = 29,
        #     title = "Metaprogramming and Ruby Gems",
        #     info = "One of Ruby’s standout features is its metaprogramming capabilities, allowing developers to write code that modifies or extends the behavior of classes and methods at runtime. This dynamic feature can be used to create domain-specific languages (DSLs) or to simplify repetitive code. Ruby Gems are packages of Ruby code that can be easily shared and reused across applications. The RubyGems package manager simplifies the process of installing, managing, and distributing these libraries, providing access to a vast ecosystem of pre-built functionality that enhances development productivity.",
        #     course_id = 5
        # )
        # Lesson.objects.create(
        #     id = 30,
        #     title = "Web Development with Ruby on Rails",
        #     info = "Ruby on Rails (often referred to as Rails) is a powerful web application framework written in Ruby that follows the MVC (Model-View-Controller) architectural pattern. Rails promotes convention over configuration, allowing developers to create database-backed web applications quickly and efficiently. Key features of Rails include an integrated ORM called ActiveRecord for database interactions, built-in testing frameworks, and a strong emphasis on RESTful architecture. Rails also provides scaffolding capabilities, enabling rapid prototyping and development of web applications, making it a popular choice for startups and web developers.",
        #     course_id = 5
        # )
        # # PHP
        # Lesson.objects.create(
        #     id = 31,
        #     title = "PHP Basics: Syntax, Variables, and Operators",
        #     info = "PHP (Hypertext Preprocessor) is a widely-used server-side scripting language designed for web development. PHP code is embedded within HTML using <?php ... ?> tags, allowing dynamic content generation. The syntax is similar to C and Java, making it accessible to those familiar with these languages. Variables in PHP are declared using the $ sign, and they are dynamically typed, meaning their types can change at runtime. Common data types include strings, integers, floats, booleans, arrays, and objects. PHP supports a wide range of operators, including arithmetic (+, -, *, /), comparison (==, ===, !=, >), and logical operators (&&, ||, !), facilitating various operations in scripts.",
        #     course_id = 6
        # )
        # Lesson.objects.create(
        #     id = 32,
        #     title = "Control Structures and Functions in PHP",
        #     info = "PHP provides control structures such as conditional statements (if, else, elseif, switch) that allow developers to execute code based on specific conditions. Looping structures, including for, while, and foreach, enable iteration over arrays or other iterable data types. Functions in PHP are defined using the function keyword and can take parameters and return values. PHP also supports variable-length argument lists, allowing functions to accept any number of arguments. Built-in functions cover a wide range of tasks, from string manipulation to array handling and file operations, promoting code reuse and modularity.",
        #     course_id = 6
        # )
        # Lesson.objects.create(
        #     id = 33,
        #     title = "Working with Forms and User Input",
        #     info = "PHP is commonly used for handling form submissions and user input in web applications. Forms are created using HTML, and when submitted, the data can be accessed in PHP via the $_GET, $_POST, or $_REQUEST superglobals, depending on the method used. Input validation and sanitization are crucial for security and data integrity, often performed using built-in functions like filter_var() and htmlspecialchars(). PHP also provides support for file uploads through forms, enabling users to submit files to the server for processing.",
        #     course_id = 6
        # )
        # Lesson.objects.create(
        #     id = 34,
        #     title = "Database Interaction with MySQL and PDO",
        #     info = "PHP excels in database interaction, particularly with MySQL, which is a popular relational database management system. Developers can use the MySQLi extension or PDO (PHP Data Objects) for database connections and queries. PDO offers a consistent interface for accessing various database types and provides prepared statements, enhancing security against SQL injection attacks. Basic operations such as connecting to the database, executing queries, fetching results, and managing transactions are essential skills for building data-driven applications in PHP.",
        #     course_id = 6
        # )
        # Lesson.objects.create(
        #     id = 35,
        #     title = "Building Secure and Scalable Web Applications",
        #     info = "Security is a critical concern in PHP web applications. Best practices include using prepared statements to prevent SQL injection, validating and sanitizing user input, managing sessions securely, and protecting against cross-site scripting (XSS) and cross-site request forgery (CSRF) attacks. PHP’s built-in session management allows developers to maintain user state across requests. For scalability, leveraging caching mechanisms, optimizing database queries, and using load balancers can significantly enhance application performance and user experience.",
        #     course_id = 6
        # )
        # Lesson.objects.create(
        #     id = 36,
        #     title = "Introduction to PHP Frameworks: Laravel and Symfony",
        #     info = "PHP frameworks such as Laravel and Symfony provide powerful tools for building robust web applications. Laravel is known for its elegant syntax, built-in tools for routing, authentication, and session management, and its ORM called Eloquent for database interactions. Laravel follows the MVC (Model-View-Controller) architectural pattern, promoting clean code organization. Symfony, on the other hand, is a highly flexible framework that emphasizes reusable components and best practices, making it suitable for large-scale applications. Both frameworks offer extensive documentation, community support, and a wide array of packages and libraries to extend functionality, significantly accelerating development processes.",
        #     course_id = 6
        # )

        # C++
        # Test.objects.create(
        #     id = 1,
        #     question = "What is the correct way to declare a pointer in C++?",
        #     answer1 = "int ptr;",
        #     answer2 = "int *ptr;",
        #     answer3 = "int &ptr;",
        #     answer4 = "int ptr*",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 2,
        #     question = "Which of the following is a valid constructor for a class named MyClass?",
        #     answer1 = "MyClass();",
        #     answer2 = "void MyClass();",
        #     answer3 = "int MyClass();",
        #     answer4 = "float MyClass();",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 3,
        #     question = "What is the output of cout << 5 + 10;?",
        #     answer1 = "15",
        #     answer2 = "510",
        #     answer3 = "5",
        #     answer4 = "10",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 4,
        #     question = "Which of the following data types can store a decimal number?",
        #     answer1 = "int",
        #     answer2 = "float",
        #     answer3 = "char",
        #     answer4 = "bool",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 5,
        #     question = "Which of the following operators is used to access members of a structure through a pointer?",
        #     answer1 = ".",
        #     answer2 = "->",
        #     answer3 = "*",
        #     answer4 = "&",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 6,
        #     question = "What does #include<iostream> do in a C++ program?",
        #     answer1 = "It includes the iostream library for input/output operations.",
        #     answer2 = "It starts the main function.",
        #     answer3 = "It initializes all variables.",
        #     answer4 = "It creates a header file.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 7,
        #     question = "Which of the following loops is guaranteed to execute at least once?",
        #     answer1 = "for",
        #     answer2 = "while",
        #     answer3 = "do-while",
        #     answer4 = "None of the above",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 8,
        #     question = "Which of the following is a feature of object-oriented programming in C++?",
        #     answer1 = "Encapsulation",
        #     answer2 = "Recursion",
        #     answer3 = "Functions",
        #     answer4 = "Preprocessor directives",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 9,
        #     question = "What is the size of an int data type in most C++ compilers?",
        #     answer1 = "2 bytes",
        #     answer2 = "4 bytes",
        #     answer3 = "8 bytes",
        #     answer4 = "16 bytes",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 10,
        #     question = "Which of the following is used to define a block of code that might throw an exception?",
        #     answer1 = "catch",
        #     answer2 = "throw",
        #     answer3 = "try",
        #     answer4 = "finally",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 11,
        #     question = "What does the return statement do in a C++ function?",
        #     answer1 = "Terminates the program",
        #     answer2 = "Exits the current function and optionally returns a value",
        #     answer3 = "Declares a variable",
        #     answer4 = "None of the above",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 12,
        #     question = "Which of the following is not a valid access specifier in C++?",
        #     answer1 = "public",
        #     answer2 = "private",
        #     answer3 = "protected",
        #     answer4 = "global",
        #     correct_answer = 4,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 13,
        #     question = "In C++, what is a pure virtual function?",
        #     answer1 = "A function with no body",
        #     answer2 = "A function that must be overridden in a derived class",
        #     answer3 = "A function that can be overridden but not necessarily",
        #     answer4 = "A function that only works in a base class",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 14,
        #     question = "Which keyword is used to prevent a class from being inherited?",
        #     answer1 = "sealed",
        #     answer2 = "final",
        #     answer3 = "static",
        #     answer4 = "const",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 15,
        #     question = "What does the new keyword do in C++?",
        #     answer1 = "Allocates memory dynamically",
        #     answer2 = "Creates a new variable",   
        #     answer3 = "Declares a function",
        #     answer4 = "Creates a header file",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 16,
        #     question = "Which of the following is the correct way to declare a reference variable?",
        #     answer1 = "int &ref = x;",
        #     answer2 = "int *ref = x;",
        #     answer3 = "int ref = &x;",
        #     answer4 = "int ref = *x;",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 17,
        #     question = "What is the output of the following statement: cout << 2 * 3 + 4;?",
        #     answer1 = "10",
        #     answer2 = "12",
        #     answer3 = "14",
        #     answer4 = "24",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 18,
        #     question = "Which of the following is true about destructors in C++?",
        #     answer1 = "They have the same name as the class, preceded by a tilde ~.",
        #     answer2 = "They return an integer value.",
        #     answer3 = "They are called automatically when an object is created.",
        #     answer4 = "They must be explicitly called.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 19,
        #     question = "What is the purpose of the static keyword when used with a variable inside a function?",
        #     answer1 = "The variable is global.",
        #     answer2 = "The variable retains its value between function calls.",
        #     answer3 = "The variable is private to the function.",
        #     answer4 = "The variable is initialized each time the function is called.",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # Test.objects.create(
        #     id = 20,
        #     question = "What does std:: indicate in C++?",
        #     answer1 = "It declares a standard variable.",
        #     answer2 = "It indicates the standard namespace.",
        #     answer3 = "It defines a structure.",
        #     answer4 = "It denotes a static data member.",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 1
        # )
        # # C#
        # Test.objects.create(
        #     id = 21,
        #     question = "Which of the following is the correct syntax for a single-line comment in C#?",
        #     answer1 = "// This is a comment",
        #     answer2 = "/* This is a comment */",
        #     answer3 = "# This is a comment",
        #     answer4 = "<!-- This is a comment -->",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 22,
        #     question = "What is the default value of a bool in C#?",
        #     answer1 = "true",
        #     answer2 = "false",
        #     answer3 = "null",
        #     answer4 = "0",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 23,
        #     question = "Which of the following is the correct way to declare a string variable in C#?",
        #     answer1 = "string varName = 'Hello';",
        #     answer2 = "string varName = \"Hello\";",
        #     answer3 = "String varName = 'Hello';",
        #     answer4 = "String varName = Hello;",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 24,
        #     question = "Which keyword is used to define a method that cannot be overridden in a derived class?",
        #     answer1 = "abstract",
        #     answer2 = "sealed",
        #     answer3 = "static",
        #     answer4 = "virtual",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 25,
        #     question = "What is the output of the following code: Console.WriteLine(5 / 2);?",
        #     answer1 = "2.5",
        #     answer2 = "2",
        #     answer3 = "3",
        #     answer4 = "2.0",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 26,
        #     question = "Which of the following is a reference type in C#?",
        #     answer1 = "int",
        #     answer2 = "string",
        #     answer3 = "char",
        #     answer4 = "bool",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 27,
        #     question = "How do you declare an array of integers in C#?",
        #     answer1 = "int[] arr = new int[5];",
        #     answer2 = "int arr = new int[5];",
        #     answer3 = "int arr[5];",
        #     answer4 = "int[] arr = new int;",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 28,
        #     question = "Which of the following is true about a static method in C#?",
        #     answer1 = "It can only be accessed within the class it is defined.",
        #     answer2 = "It can be called without creating an instance of the class.",
        #     answer3 = "It must return a value.",
        #     answer4 = "It can access instance variables.",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 29,
        #     question = "Which access modifier makes a member visible only within its own class?",
        #     answer1 = "public",
        #     answer2 = "private",
        #     answer3 = "protected",
        #     answer4 = "internal",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 30,
        #     question = "What is the purpose of the using statement in C#?",
        #     answer1 = "To include a namespace",
        #     answer2 = "To ensure the disposal of resources",
        #     answer3 = "To declare a variable",
        #     answer4 = "To import a class",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 31,
        #     question = "Which of the following is used to handle exceptions in C#?",
        #     answer1 = "try-catch",
        #     answer2 = "if-else",
        #     answer3 = "for-loop",
        #     answer4 = "switch-case",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 32,
        #     question = "What does null represent in C#?",
        #     answer1 = "A number",
        #     answer2 = "The absence of a value",
        #     answer3 = "An empty string",
        #     answer4 = "A boolean false",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 33,
        #     question = "Which keyword is used to inherit a class in C#?",
        #     answer1 = "implements",
        #     answer2 = "inherits",
        #     answer3 = ": (Colon)",
        #     answer4 = "extends",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 34,
        #     question = "What is the base class for all data types in C#?",
        #     answer1 = "System.ValueType",
        #     answer2 = "System.Object",
        #     answer3 = "System.Type",
        #     answer4 = "System.Base",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 35,
        #     question = "How do you create an instance of a class in C#?",
        #     answer1 = "MyClass obj = new MyClass();",
        #     answer2 = "MyClass obj = MyClass();",
        #     answer3 = "MyClass obj = new();",
        #     answer4 = "MyClass obj;",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 36,
        #     question = "Which of the following operators is used for logical AND in C#?",
        #     answer1 = "++",
        #     answer2 = "&&",
        #     answer3 = "&",
        #     answer4 = "||",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 37,
        #     question = "Which loop structure will execute the code block at least once, regardless of the condition?",
        #     answer1 = "for",
        #     answer2 = "while",
        #     answer3 = "do-while",
        #     answer4 = "foreach",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 38,
        #     question = "Which of the following keywords is used to define an interface in C#?",
        #     answer1 = "abstract",
        #     answer2 = "interface",
        #     answer3 = "class",
        #     answer4 = "implements",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 39,
        #     question = "What is a delegate in C#?",
        #     answer1 = "A type that represents references to methods",
        #     answer2 = "A variable that can hold multiple values",
        #     answer3 = "A loop structure",
        #     answer4 = "A way to inherit from multiple classes",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 2
        # )
        # Test.objects.create(
        #     id = 40,
        #     question = "What is the keyword used to exit a loop prematurely in C#?",
        #     answer1 = "break",
        #     answer2 = "continue",
        #     answer3 = "return",
        #     answer4 = "exit",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 2
        # )
        # # Java
        # Test.objects.create(
        #     id = 41,
        #     question = "Which of the following is the correct way to declare a variable in Java?",
        #     answer1 = "int x = 10;",
        #     answer2 = "int x := 10;",
        #     answer3 = "int x == 10;",
        #     answer4 = "int x -> 10;",
        #     correct_answer = 0,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 42,
        #     question = "Which of the following data types is used to store a single character in Java?",
        #     answer1 = "String",
        #     answer2 = "char",
        #     answer3 = "int",
        #     answer4 = "boolean",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 43,
        #     question = "Which keyword is used to create an instance of a class in Java?",
        #     answer1 = "class",
        #     answer2 = "new",
        #     answer3 = "this",
        #     answer4 = "void",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 44,
        #     question = "Which of the following is a valid method declaration in Java?",
        #     answer1 = "public void myMethod() {}",
        #     answer2 = "public void myMethod[] {}",
        #     answer3 = "public void myMethod;",
        #     answer4 = "public myMethod() {}",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 45,
        #     question = "What is the size of an int data type in Java?",
        #     answer1 = "2 bytes",
        #     answer2 = "1 byte",
        #     answer3 = "8 bytes",
        #     answer4 = "4 bytes",
        #     correct_answer = 4,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 46,
        #     question = "Which of the following is the correct syntax to print \"Hello, World!\" in Java?",
        #     answer1 = "System.out.println(\"Hello, World!\");",
        #     answer2 = "print(\"Hello, World!\");",
        #     answer3 = "echo \"Hello, World!\";",
        #     answer4 = "Console.WriteLine(\"Hello, World!\");",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 47,
        #     question = "Which of the following is the correct way to declare an array of integers in Java?",
        #     answer1 = "int arr = new int[5];",
        #     answer2 = "int[] arr = new int[5];",
        #     answer3 = "int arr[5];",
        #     answer4 = "int arr = new int;",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 48,
        #     question = "Which of the following is true about constructors in Java?",
        #     answer1 = "They must have a return type.",
        #     answer2 = "They have the same name as the class.",
        #     answer3 = "They must be declared as public.",
        #     answer4 = "They can be called multiple times.",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 49,
        #     question = "What is the purpose of the this keyword in Java?",
        #     answer1 = "It refers to the superclass of the current object.",
        #     answer2 = "It refers to the current object.",
        #     answer3 = "It refers to a static variable.",
        #     answer4 = "It refers to a method of the current class.",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 50,
        #     question = "Which of the following is not a valid access modifier in Java?",
        #     answer1 = "public",
        #     answer2 = "private",
        #     answer3 = "internal",
        #     answer4 = "protected",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 51,
        #     question = "What is the output of the following code? System.out.println(5 / 2);",
        #     answer1 = "2",
        #     answer2 = "2.5",
        #     answer3 = "3",
        #     answer4 = "5",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 52,
        #     question = "Which keyword is used to inherit a class in Java?",
        #     answer1 = "implements",
        #     answer2 = "extends",
        #     answer3 = "inherits",
        #     answer4 = "derives",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 53,
        #     question = "Which of the following is a marker interface in Java?",
        #     answer1 = "Serializable",
        #     answer2 = "Cloneable",
        #     answer3 = "Comparable",
        #     answer4 = "Runnable",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 54,
        #     question = "Which of the following is true about the final keyword in Java?",
        #     answer1 = "It can be used with classes but not with variables.",
        #     answer2 = "It can be used with classes, methods, and variables.",
        #     answer3 = "It can be used with variables but not with methods.",
        #     answer4 = "It can only be used with methods.",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 55,
        #     question = "Which of the following loops is guaranteed to execute at least once?",
        #     answer1 = "for",
        #     answer2 = "while",
        #     answer3 = "do-while",
        #     answer4 = "None of the above",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 56,
        #     question = "What does the static keyword mean in Java?",
        #     answer1 = "The member belongs to the class rather than an instance of the class.",
        #     answer2 = "The member cannot be modified.",
        #     answer3 = "The member is only accessible within the current package.",
        #     answer4 = "The member is immutable.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 57,
        #     question = "Which of the following is used to handle exceptions in Java?",
        #     answer1 = "try-catch",
        #     answer2 = "if-else",
        #     answer3 = "for-loop",
        #     answer4 = "switch-case",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 58,
        #     question = "Which of the following correctly defines a main method in Java?",
        #     answer1 = "public static void main(String[] args)",
        #     answer2 = "public void main(String args)",
        #     answer3 = "static public void main()",
        #     answer4 = "public void static Main(String[] args)",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 59,
        #     question = "Which of the following is the parent class of all classes in Java?",
        #     answer1 = "Object",
        #     answer2 = "java.lang.Object",
        #     answer3 = "Class",
        #     answer4 = "Root",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 3
        # )
        # Test.objects.create(
        #     id = 60,
        #     question = "What is the purpose of the super keyword in Java?",
        #     answer1 = "It is used to call the superclass's constructor.",
        #     answer2 = "It is used to define a subclass.",
        #     answer3 = "It is used to call a method from the subclass.",
        #     answer4 = "It is used to create an instance of a class.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 3
        # )
        # # Python
        # Test.objects.create(
        #     id = 61,
        #     question = "Which of the following is the correct way to declare a variable in Python?",
        #     answer1 = "int x = 10",
        #     answer2 = "x = 10",
        #     answer3 = "var x = 10",
        #     answer4 = "declare x = 10",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 62,
        #     question = "Which of the following is used to define a function in Python?",
        #     answer1 = "function",
        #     answer2 = "defun",
        #     answer3 = "def",
        #     answer4 = "define",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 63,
        #     question = "What will be the output of the following code? print(3 * 'Hello ')",
        #     answer1 = "Hello Hello Hello ",
        #     answer2 = "HelloHelloHello",
        #     answer3 = "Hello 3",
        #     answer4 = "3Hello",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 64,
        #     question = "How do you create a list in Python?",
        #     answer1 = "list = {}",
        #     answer2 = "list = []",
        #     answer3 = "list = ()",
        #     answer4 = "list = <>",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 65,
        #     question = "Which of the following is the correct syntax for a multi-line comment in Python?",
        #     answer1 = "''' This is a comment '''",
        #     answer2 = "/* This is a comment */",
        #     answer3 = "<!-- This is a comment -->",
        #     answer4 = "// This is a comment",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 66,
        #     question = "Which of the following is used to handle exceptions in Python?",
        #     answer1 = "try-except",
        #     answer2 = "try-catch",
        #     answer3 = "if-else",
        #     answer4 = "do-except",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 67,
        #     question = "What is the output of the following code? print(type(5))",
        #     answer1 = "<class 'float'>",
        #     answer2 = "<class 'int'>",
        #     answer3 = "<class 'str'>",
        #     answer4 = "<class 'list'>",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 68,
        #     question = "How do you add an element to the end of a list in Python?",
        #     answer1 = "list.append(element)",
        #     answer2 = "list.add(element)",
        #     answer3 = "list.insert(element)",
        #     answer4 = "list.push(element)",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 69,
        #     question = "What is the output of the following code? print(10 // 3)",
        #     answer1 = "3.333",
        #     answer2 = "3",
        #     answer3 = "4",
        #     answer4 = "3.0",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 70,
        #     question = "Which of the following is a mutable data type in Python?",
        #     answer1 = "tuple",
        #     answer2 = "str",
        #     answer3 = "list",
        #     answer4 = "int",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 71,
        #     question = "Which of the following is the correct syntax to import a module in Python?",
        #     answer1 = "import module as mod",
        #     answer2 = "import module",
        #     answer3 = "module import",
        #     answer4 = "import module from python",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 72,
        #     question = "How do you start a Python script from the command line?",
        #     answer1 = "python script.py",
        #     answer2 = "run script.py",
        #     answer3 = "start script.py",
        #     answer4 = "execute script.py",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 73,
        #     question = "Which of the following statements is true about Python?",
        #     answer1 = "Python is an interpreted language.",
        #     answer2 = "Python is a compiled language.",
        #     answer3 = "Python is a statically typed language.",
        #     answer4 = "Python does not support object-oriented programming.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 74,
        #     question = "What is the output of the following code? print(2 ** 3)",
        #     answer1 = "5",
        #     answer2 = "8",
        #     answer3 = "6",
        #     answer4 = "9",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 75,
        #     question = "Which of the following keywords is used to define a class in Python?",
        #     answer1 = "function",
        #     answer2 = "class",
        #     answer3 = "define",
        #     answer4 = "type",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 76,
        #     question = "Which of the following is the correct way to create an empty dictionary in Python?",
        #     answer1 = "dict = []",
        #     answer2 = "dict = {}",
        #     answer3 = "dict = ()",
        #     answer4 = "dict = None",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 77,
        #     question = "What does the len() function do in Python?",
        #     answer1 = "Returns the number of elements in a list",
        #     answer2 = "Returns the length of a string",
        #     answer3 = "Returns the number of keys in a dictionary",
        #     answer4 = "All of the above",
        #     correct_answer = 4,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 78,
        #     question = "Which of the following is true about the break statement in Python?",
        #     answer1 = "It terminates the current function.",
        #     answer2 = "It skips the rest of the code inside a loop and starts the next iteration.",
        #     answer3 = "It exits the current loop.",
        #     answer4 = "It ends the entire program.",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 79,
        #     question = "Which of the following is the correct way to open a file for reading in Python?",
        #     answer1 = "file = open('filename.txt', 'r')",
        #     answer2 = "file = open('filename.txt', 'w')",
        #     answer3 = "file = open('filename.txt', 'a')",
        #     answer4 = "file = open('filename.txt')",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # Test.objects.create(
        #     id = 80,
        #     question = "Which of the following statements is used to create a new class that inherits from another class in Python?",
        #     answer1 = "class NewClass(BaseClass):",
        #     answer2 = "class NewClass extends BaseClass:",
        #     answer3 = "class NewClass inherits BaseClass:",
        #     answer4 = "class NewClass implements BaseClass:",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 4
        # )
        # # Ruby
        # Test.objects.create(
        #     id = 81,
        #     question = "Which of the following is the correct way to declare a variable in Ruby?",
        #     answer1 = "x = 10",
        #     answer2 = "int x = 10",
        #     answer3 = "var x = 10",
        #     answer4 = "declare x = 10",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 82,
        #     question = "Which of the following is used to define a method in Ruby?",
        #     answer1 = "def",
        #     answer2 = "function",
        #     answer3 = "method",
        #     answer4 = "define",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 83,
        #     question = "What will be the output of the following code? puts 3 * \"Hello \"",
        #     answer1 = "Hello Hello Hello ",
        #     answer2 = "HelloHelloHello",
        #     answer3 = "Hello 3",
        #     answer4 = "3Hello",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 84,
        #     question = "How do you create an array in Ruby?",
        #     answer1 = "array = []",
        #     answer2 = "array = {}",
        #     answer3 = "array = ()",
        #     answer4 = "array = <>",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 85,
        #     question = "Which of the following is the correct syntax for a multi-line comment in Ruby?",
        #     answer1 = "/* This is a comment */",
        #     answer2 = "=begin ... =end",
        #     answer3 = "<!-- This is a comment -->",
        #     answer4 = "''' This is a comment '''",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 86,
        #     question = "Which of the following is used to handle exceptions in Ruby?",
        #     answer1 = "begin-rescue",
        #     answer2 = "try-catch",
        #     answer3 = "if-else",
        #     answer4 = "do-rescue",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 87,
        #     question = "What is the output of the following code? puts 10 / 3",
        #     answer1 = "3",
        #     answer2 = "3.333",
        #     answer3 = "4",
        #     answer4 = "3.0",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 88,
        #     question = "How do you add an element to the end of an array in Ruby?",
        #     answer1 = "array << element",
        #     answer2 = "array.add(element)",
        #     answer3 = "array.append(element)",
        #     answer4 = "array.push(element)",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 89,
        #     question = "What is the output of the following code? puts 10 ** 2",
        #     answer1 = "100",
        #     answer2 = "20",
        #     answer3 = "10",
        #     answer4 = "200",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 90,
        #     question = "Which of the following is a mutable data type in Ruby?",
        #     answer1 = "Symbol",
        #     answer2 = "Fixnum",
        #     answer3 = "Array",
        #     answer4 = "NilClass",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 91,
        #     question = "Which of the following is the correct syntax to require a file in Ruby?",
        #     answer1 = "import 'file'",
        #     answer2 = "require 'file'",
        #     answer3 = "include 'file'",
        #     answer4 = "use 'file'",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 92,
        #     question = "How do you start a Ruby script from the command line?",
        #     answer1 = "ruby script.rb",
        #     answer2 = "run script.rb",
        #     answer3 = "start script.rb",
        #     answer4 = "execute script.rb",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 93,
        #     question = "Which of the following statements is true about Ruby?",
        #     answer1 = "Ruby is an interpreted language.",
        #     answer2 = "Ruby is a compiled language.",
        #     answer3 = "Ruby is a statically typed language.",
        #     answer4 = "Ruby does not support object-oriented programming.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 94,
        #     question = "What is the output of the following code? puts 2 ** 3",
        #     answer1 = "5",
        #     answer2 = "8",
        #     answer3 = "6",
        #     answer4 = "9",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 95,
        #     question = "Which of the following keywords is used to define a class in Ruby?",
        #     answer1 = "class",
        #     answer2 = "define",
        #     answer3 = "function",
        #     answer4 = "type",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 96,
        #     question = "Which of the following is the correct way to create an empty hash in Ruby?",
        #     answer1 = "hash = []",
        #     answer2 = "hash = {}",
        #     answer3 = "hash = ()",
        #     answer4 = "hash = None",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 97,
        #     question = "What does the length method do in Ruby?",
        #     answer1 = "Returns the number of elements in a list",
        #     answer2 = "Returns the length of a string",
        #     answer3 = "Returns the number of keys in a hash",
        #     answer4 = "All of the above",
        #     correct_answer = 4,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 98,
        #     question = "Which of the following is true about the break statement in Ruby?",
        #     answer1 = "It terminates the current function.",
        #     answer2 = "It skips the rest of the code inside a loop and starts the next iteration.",
        #     answer3 = "It exits the current loop.",
        #     answer4 = "It ends the entire program.",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 99,
        #     question = "Which of the following is the correct way to open a file for reading in Ruby?",
        #     answer1 = "file = File.open('filename.txt', 'r')",
        #     answer2 = "file = File.open('filename.txt', 'w')",
        #     answer3 = "file = File.open('filename.txt', 'a')",
        #     answer4 = "file = File.open('filename.txt')",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # Test.objects.create(
        #     id = 100,
        #     question = "Which of the following statements is used to create a new class that inherits from another class in Ruby?",
        #     answer1 = "class NewClass < BaseClass",
        #     answer2 = "class NewClass extends BaseClass",
        #     answer3 = "class NewClass inherits BaseClass",
        #     answer4 = "class NewClass implements BaseClass",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 5
        # )
        # # PHP
        # Test.objects.create(
        #     id = 101,
        #     question = "Which of the following is the correct way to declare a variable in PHP?",
        #     answer1 = "$x = 10;",
        #     answer2 = "int $x = 10;",
        #     answer3 = "var $x = 10;",
        #     answer4 = "declare $x = 10;",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 102,
        #     question = "Which of the following is used to define a function in PHP?",
        #     answer1 = "function()",
        #     answer2 = "function",
        #     answer3 = "def",
        #     answer4 = "define",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 103,
        #     question = "What will be the output of the following code? echo 3 * \"Hello \";",
        #     answer1 = "HelloHelloHello",
        #     answer2 = "3",
        #     answer3 = "Hello 3",
        #     answer4 = "Error",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 104,
        #     question = "How do you create an array in PHP?",
        #     answer1 = "$array = array();",
        #     answer2 = "$array = {};",
        #     answer3 = "$array = [];",
        #     answer4 = "$array = <>;",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 105,
        #     question = "Which of the following is the correct syntax for a single-line comment in PHP?",
        #     answer1 = "// This is a comment",
        #     answer2 = "/* This is a comment */",
        #     answer3 = "<!-- This is a comment -->",
        #     answer4 = "# This is a comment",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 106,
        #     question = "Which of the following is used to handle exceptions in PHP?",
        #     answer1 = "try-catch",
        #     answer2 = "if-else",
        #     answer3 = "do-catch",
        #     answer4 = "try-catch-finally",
        #     correct_answer = 4,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 107,
        #     question = "What is the output of the following code? echo 10 / 3;",
        #     answer1 = "3",
        #     answer2 = "3.3333333333333",
        #     answer3 = "3.0",
        #     answer4 = "4",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 108,
        #     question = "How do you add an element to the end of an array in PHP?",
        #     answer1 = "array_push($array, $element);",
        #     answer2 = "$array.add($element);",
        #     answer3 = "$array[] = $element;",
        #     answer4 = "$array.append($element);",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 109,
        #     question = "What is the output of the following code? echo 10 ** 2;",
        #     answer1 = "100",
        #     answer2 = "20",
        #     answer3 = "10",
        #     answer4 = "200",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 110,
        #     question = "Which of the following is a scalar data type in PHP?",
        #     answer1 = "int",
        #     answer2 = "array",
        #     answer3 = "object",
        #     answer4 = "resource",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 111,
        #     question = "Which of the following is the correct syntax to include a file in PHP?",
        #     answer1 = "include 'file.php';",
        #     answer2 = "require 'file.php';",
        #     answer3 = "use 'file.php';",
        #     answer4 = "import 'file.php';",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 112,
        #     question = "How do you start a PHP script?",
        #     answer1 = "<?php",
        #     answer2 = "<?",
        #     answer3 = "<php>",
        #     answer4 = "<?php start; ?>",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 113,
        #     question = "Which of the following statements is true about PHP?",
        #     answer1 = "PHP is a server-side scripting language.",
        #     answer2 = "PHP is a client-side scripting language.",
        #     answer3 = "PHP is a statically typed language.",
        #     answer4 = "PHP does not support object-oriented programming.",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 114,
        #     question = "What is the output of the following code? echo 2 ** 3;",
        #     answer1 = "5",
        #     answer2 = "8",
        #     answer3 = "6",
        #     answer4 = "9",
        #     correct_answer = 2,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 115,
        #     question = "Which of the following keywords is used to define a class in PHP?",
        #     answer1 = "class",
        #     answer2 = "define",
        #     answer3 = "function",
        #     answer4 = "type",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 116,
        #     question = "Which of the following is the correct way to create an empty array in PHP?",
        #     answer1 = "$array = array();",
        #     answer2 = "$array = {};",
        #     answer3 = "$array = ();",
        #     answer4 = "$array = None;",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 117,
        #     question = "What does the count() function do in PHP?",
        #     answer1 = "Returns the number of elements in an array",
        #     answer2 = "Returns the length of a string",
        #     answer3 = "Returns the number of keys in a dictionary",
        #     answer4 = "Returns the number of lines in a file",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 118,
        #     question = "Which of the following is true about the break statement in PHP?",
        #     answer1 = "It terminates the current function.",
        #     answer2 = "It skips the rest of the code inside a loop and starts the next iteration.",
        #     answer3 = "It exits the current loop.",
        #     answer4 = "It ends the entire program.",
        #     correct_answer = 3,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 119,
        #     question = "Which of the following is the correct way to open a file for reading in PHP?",
        #     answer1 = "$file = fopen('filename.txt', 'r');",
        #     answer2 = "$file = fopen('filename.txt', 'w');",
        #     answer3 = "$file = fopen('filename.txt', 'a');",
        #     answer4 = "$file = open('filename.txt');",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )
        # Test.objects.create(
        #     id = 120,
        #     question = "Which of the following statements is used to create a new class that inherits from another class in PHP?",
        #     answer1 = "class NewClass extends BaseClass {}",
        #     answer3 = "class NewClass implements BaseClass {}",
        #     answer4 = "class NewClass includes BaseClass {}",
        #     correct_answer = 1,
        #     points = 20,
        #     course_id = 6
        # )

        # #C++
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 1,
        #     lesson_id = 1
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 1,
        #     lesson_id = 2
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 1,
        #     lesson_id = 3
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 1,
        #     lesson_id = 4
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 1,
        #     lesson_id = 5
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 1,
        #     lesson_id = 6
        # )

        # #C#
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 2,
        #     lesson_id = 7
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 2,
        #     lesson_id = 8
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 2,
        #     lesson_id = 9
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 2,
        #     lesson_id = 10
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 2,
        #     lesson_id = 11
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 2,
        #     lesson_id = 12
        # )

        # #Java
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 3,
        #     lesson_id = 13
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 3,
        #     lesson_id = 14
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 3,
        #     lesson_id = 15
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 3,
        #     lesson_id = 16
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 3,
        #     lesson_id = 17
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 3,
        #     lesson_id = 18
        # )

        # #Python
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 4,
        #     lesson_id = 19
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 4,
        #     lesson_id = 20
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 4,
        #     lesson_id = 21
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 4,
        #     lesson_id = 22
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 4,
        #     lesson_id = 23
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 4,
        #     lesson_id = 24
        # )

        # #Ruby
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 5,
        #     lesson_id = 25
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 5,
        #     lesson_id = 26
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 5,
        #     lesson_id = 27
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 5,
        #     lesson_id = 28
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 5,
        #     lesson_id = 29
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 5,
        #     lesson_id = 30
        # )

        # #PHP
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 6,
        #     lesson_id = 31
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 6,
        #     lesson_id = 32
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 6,
        #     lesson_id = 33
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 6,
        #     lesson_id = 34
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 6,
        #     lesson_id = 35
        # )
        # Homework.objects.create(
        #     title = '',
        #     description = '',
        #     deadline = '',
        #     course_id = 6,
        #     lesson_id = 36
        # )

        name = ''