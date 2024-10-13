from django.core.management.base import BaseCommand
from lessons.models import Lesson

class Command(BaseCommand):
    help = 'Seeds the database with initial lesson data'

    def handle(self, *args, **kwargs):
        # C++
        Lesson.objects.create(
            id = 1,
            title = "Introduction to C++ Syntax and Structure",
            info = "C++ is a versatile, high-performance programming language that extends C by adding object-oriented features. The basic structure of a C++ program starts with the #include directive for including libraries, followed by the main() function, which serves as the entry point. Statements end with semicolons, and the language supports various data types like int, float, and char. For handling input and output, C++ uses cin and cout, respectively. Comments can be added using // for single-line or /*...*/ for multi-line.",
            course_id = 1
        )
        Lesson.objects.create(
            id = 2,
            title = "Control Structures and Functions",
            info = "Control structures in C++ include loops (for, while, do-while), conditional statements (if, else, switch), and branching (break, continue, return). Functions are blocks of reusable code that can take parameters and return values. They help in organizing code and improving reusability. Functions in C++ can be declared before their use or defined inline, and the language supports both pass-by-value and pass-by-reference.",
            course_id = 1
        )
        Lesson.objects.create(
            id = 3,
            title = "Pointers, References, and Dynamic Memory",
            info = "Pointers are variables that store memory addresses, allowing direct manipulation of memory. They are crucial for dynamic memory management, which is handled through operators like new and delete. References are another way to access variables, similar to pointers but safer and more convenient. C++ supports dynamic memory allocation, enabling the creation of variables during runtime, which is essential for managing resources efficiently in larger applications.",
            course_id = 1
        )
        Lesson.objects.create(
            id = 4,
            title = "Object-Oriented Programming with C++",
            info = "C++ is known for its strong support for object-oriented programming (OOP), which revolves around concepts like classes and objects. A class is a blueprint for creating objects, encapsulating data, and functions. Key OOP principles in C++ include inheritance (extending classes), polymorphism (using a unified interface), and encapsulation (hiding data). These principles help in creating modular, scalable, and maintainable code.",
            course_id = 1
        )
        Lesson.objects.create(
            id = 5,
            title = "Templates and Standard Template Library (STL)",
            info = "Templates in C++ allow for generic programming, enabling functions and classes to operate with any data type. This is especially useful for creating flexible and reusable code. The Standard Template Library (STL) is a powerful feature of C++ that provides a collection of generic classes and functions, including containers (like vector, list, map), algorithms (like sorting, searching), and iterators. STL helps in reducing development time and improving code quality.",
            course_id = 1
        )
        Lesson.objects.create(
            id = 6,
            title = "Advanced Concepts: Multi-threading, Exception Handling",
            info = "C++ also offers advanced features like multi-threading and exception handling. Multi-threading allows for concurrent execution of code, improving performance in multi-core systems. The C++ standard library includes <thread>, <mutex>, and other utilities to manage threads and synchronization. Exception handling in C++ is done using try, catch, and throw blocks, allowing programs to handle errors gracefully without crashing. This ensures that resources are managed properly, even in the face of errors.",
            course_id = 1
        )
        # C#
        Lesson.objects.create(
            id = 7,
            title = "Getting Started with C# and .NET Framework",
            info = "C# is a modern, object-oriented programming language developed by Microsoft as part of the .NET framework. It is designed for building a wide range of applications, from desktop to web to mobile. The .NET Framework provides a large library of pre-coded solutions to common programming tasks and manages the execution of programs written in C# through the Common Language Runtime (CLR). A basic C# program begins with the using directive to include necessary namespaces, followed by a namespace declaration, and the Main() method, which serves as the entry point. C# syntax is similar to other C-based languages, making it easy to learn for those familiar with C, C++, or Java.",
            course_id = 2
        )
        Lesson.objects.create(
            id = 8,
            title = "Object-Oriented Programming in C#",
            info = "C# is a fully object-oriented language, which means it supports key OOP principles like encapsulation, inheritance, and polymorphism. Classes and objects are the core building blocks. A class is a blueprint for creating objects (instances of classes). Encapsulation is achieved by keeping the data (attributes) and the methods (functions) that operate on the data together. Inheritance allows a new class to inherit the members of an existing class, promoting code reuse. Polymorphism enables methods to do different things based on the object they are acting upon, achieved through method overloading and overriding.",
            course_id = 2
        )
        Lesson.objects.create(
            id = 9,
            title = "Collections, Generics, and LINQ",
            info = "C# provides a robust set of collection classes in the System.Collections and System.Collections.Generic namespaces, including lists, dictionaries, queues, and stacks. These collections allow for the efficient storage and manipulation of groups of objects. Generics enhance collections by allowing them to operate with any data type while ensuring type safety. LINQ (Language Integrated Query) is a powerful feature in C# that allows developers to write queries directly in their code using a SQL-like syntax, making it easier to retrieve and manipulate data from various sources like arrays, collections, XML, and databases.",
            course_id = 2
        )
        Lesson.objects.create(
            id = 10,
            title = "Exception Handling and Debugging",
            info = "In C#, exception handling is a structured way to handle runtime errors, ensuring that the program can continue to run or fail gracefully. This is done using try, catch, finally, and throw statements. The try block contains the code that might cause an exception, the catch block handles the exception, and finally is used for cleanup code that should run regardless of whether an exception occurred. The throw statement is used to trigger an exception. Debugging tools in Visual Studio, such as breakpoints, watch windows, and step-through debugging, help developers identify and fix issues in their code efficiently.",
            course_id = 2
        )
        Lesson.objects.create(
            id = 11,
            title = "Asynchronous Programming with async and await",
            info = "Asynchronous programming in C# allows tasks to run concurrently, which improves the responsiveness of applications, especially those with I/O-bound operations like reading files, making web requests, or accessing databases. The async and await keywords are central to writing asynchronous code in C#. An async method runs asynchronously and can contain one or more await expressions that pause the method execution until the awaited task is completed. This approach makes it easier to write, read, and maintain asynchronous code without blocking the main thread, thus keeping the UI responsive.",
            course_id = 2
        )
        Lesson.objects.create(
            id = 12,
            title = "Developing Applications with Windows Forms and WPF",
            info = "C# is often used to develop desktop applications using Windows Forms or Windows Presentation Foundation (WPF). Windows Forms is a graphical API for creating rich desktop applications with event-driven programming, where controls like buttons, text boxes, and labels can be added to forms. WPF is a more modern and flexible framework that allows for the development of visually rich user interfaces using XAML (Extensible Application Markup Language). WPF supports advanced features like data binding, animation, and styles, making it ideal for creating complex and dynamic applications.",
            course_id = 2
        )
        # Java
        Lesson.objects.create(
            id = 13,
            title = "Java Basics: Syntax, Data Types, and Operators",
            info = "Java is a widely-used, platform-independent programming language known for its portability and robustness. The syntax of Java is similar to C and C++, making it familiar to those who have experience with these languages. Java programs start with the public static void main(String[] args) method, which serves as the entry point. Data types in Java are categorized into primitive types (like int, float, char, boolean) and reference types (like arrays and objects). Java supports various operators including arithmetic (+, -, *, /), relational (==, !=, >, <), logical (&&, ||, !), and bitwise operators. Java’s strong typing and automatic memory management via garbage collection contribute to its stability and security.",
            course_id = 3
        )
        Lesson.objects.create(
            id = 14,
            title = "Object-Oriented Programming in Java",
            info = "Java is an object-oriented programming language, and its OOP features are fundamental to creating reusable and maintainable code. The four main principles of OOP in Java are encapsulation, inheritance, polymorphism, and abstraction. Encapsulation involves bundling the data (fields) and methods (functions) that operate on the data into a single unit, usually a class, and restricting access to some of the object's components. Inheritance allows one class to inherit fields and methods from another, promoting code reuse. Polymorphism enables objects to be treated as instances of their parent class, allowing for flexible code design through method overriding and overloading. Abstraction hides complex implementation details and exposes only the essential features of an object.",
            course_id = 3
        )
        Lesson.objects.create(
            id = 15,
            title = "Exception Handling and File I/O",
            info = "Java has a robust exception-handling mechanism that helps manage runtime errors, ensuring that programs can handle unexpected situations gracefully. This is done using try, catch, finally, and throw blocks. The try block contains the code that might throw an exception, while the catch block handles specific exceptions. The finally block is executed regardless of whether an exception is thrown, often used for resource cleanup. Java also provides extensive support for file input/output (I/O) operations through classes in the java.io and java.nio packages. These classes allow reading from and writing to files, handling streams, and performing other file operations efficiently.",
            course_id = 3
        )
        Lesson.objects.create(
            id = 16,
            title = "Multi-threading and Concurrency",
            info = "Java's multi-threading capabilities allow for the concurrent execution of two or more threads (lightweight processes), making programs more efficient, especially on multi-core systems. Java provides built-in support for multi-threading through the Thread class and the Runnable interface. Key concepts in multi-threading include thread creation, synchronization (using synchronized blocks or methods to prevent thread interference), and inter-thread communication. Concurrency utilities in the java.util.concurrent package provide higher-level abstractions like thread pools, executors, and locks, which simplify the development of concurrent applications.",
            course_id = 3
        )
        Lesson.objects.create(
            id = 17,
            title = "Data Structures and Algorithms in Java",
            info = "Java provides a rich set of data structures and algorithms through its Collections Framework, which includes interfaces like List, Set, Queue, and Map, and their implementations like ArrayList, HashSet, LinkedList, and HashMap. These data structures are essential for efficiently managing and organizing data. Algorithms such as sorting, searching, and iteration are built into the framework, making it easier to implement common operations. Java also supports custom implementations of data structures and algorithms, allowing developers to optimize performance for specific use cases.",
            course_id = 3
        )
        Lesson.objects.create(
            id = 18,
            title = "Introduction to Java Web Development: Servlets and JSP",
            info = "Java is a popular choice for building web applications, and two key technologies for server-side development are Servlets and JavaServer Pages (JSP). Servlets are Java classes that handle HTTP requests and responses, providing dynamic content to web clients. They are the foundation of Java web applications, and they run on a web server or application server. JSP is a technology that simplifies the creation of dynamic web content by allowing developers to embed Java code directly into HTML pages. JSP is compiled into Servlets by the server, combining the power of Java with the ease of creating web pages. Together, Servlets and JSP form a powerful combination for building robust, scalable web applications.",
            course_id = 3
        )
        # Python
        Lesson.objects.create(
            id = 19,
            title = "Python Fundamentals: Variables, Data Types, and Control Flow",
            info = "Python is a high-level, interpreted programming language known for its readability and simplicity. Variables in Python are dynamically typed, meaning you do not need to declare their type explicitly. Common data types include integers, floats, strings, lists, tuples, dictionaries, and sets. Control flow in Python is managed through statements like if, elif, and else for conditional execution, as well as loops such as for and while for iteration. Python’s indentation-based syntax promotes clean and readable code, making it accessible for beginners and experienced programmers alike.",
            course_id = 4
        )
        Lesson.objects.create(
            id = 20,
            title = "Functions, Modules, and Packages",
            info = "Functions in Python are defined using the def keyword and can take parameters and return values. They promote code reusability and modularity. Python supports first-class functions, allowing functions to be passed as arguments, returned from other functions, and assigned to variables. Modules are Python files that contain definitions and statements, allowing for code organization. You can import modules using the import statement. Packages are collections of related modules, facilitating structured code organization. The Python Standard Library provides a wealth of built-in modules for various tasks, enhancing development efficiency.",
            course_id = 4
        )
        Lesson.objects.create(
            id = 21,
            title = "Working with Files and Exception Handling",
            info = "Python provides built-in functions for file handling, enabling reading from and writing to files easily using the open() function. File operations include reading, writing, and appending data, and files can be managed in different modes such as text and binary. Exception handling in Python is done using try, except, else, and finally blocks, allowing developers to handle errors gracefully without crashing the program. This mechanism helps in managing runtime errors effectively, ensuring that resources are properly cleaned up, regardless of whether an error occurred.",
            course_id = 4
        )
        Lesson.objects.create(
            id = 22,
            title = "Object-Oriented Programming in Python",
            info = "Python is an object-oriented language that supports the principles of encapsulation, inheritance, and polymorphism. Classes are defined using the class keyword, and objects are instances of these classes. Encapsulation in Python involves bundling data and methods within classes, restricting access to certain attributes. Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse. Polymorphism enables methods to be defined in a way that they can operate on different types of objects, facilitating flexible code design. Python also supports multiple inheritance, allowing a class to inherit from multiple parent classes.",
            course_id = 4
        )
        Lesson.objects.create(
            id = 23,
            title = "Web Development with Django and Flask",
            info = "Python is widely used for web development, with Django and Flask being two popular frameworks. Django is a high-level framework that promotes rapid development and clean design, featuring an ORM (Object-Relational Mapping) for database management, an admin interface, and built-in authentication. It follows the MVC (Model-View-Controller) architectural pattern. Flask, on the other hand, is a micro-framework that is lightweight and flexible, making it easy to get started with web applications. It provides the essentials for building web apps, allowing developers to add libraries and extensions as needed, thus giving them control over application design.",
            course_id = 4
        )
        Lesson.objects.create(
            id = 24,
            title = "Data Analysis and Visualization with Pandas and Matplotlib",
            info = "Python is a powerful tool for data analysis and visualization, with libraries like Pandas and Matplotlib being widely used. Pandas is a library that provides data structures like Series and DataFrames, enabling easy manipulation and analysis of structured data. It offers functions for data cleaning, filtering, aggregation, and merging, making it ideal for data manipulation tasks. Matplotlib is a plotting library that allows for the creation of static, interactive, and animated visualizations in Python. It supports various types of plots, including line charts, bar charts, histograms, and scatter plots, enabling effective data visualization to convey insights clearly.",
            course_id = 4
        )
        # Ruby
        Lesson.objects.create(
            id = 25,
            title = "Introduction to Ruby Syntax and Data Types",
            info = "Ruby is a dynamic, object-oriented programming language known for its elegant syntax and flexibility. The basic structure of a Ruby program includes defining classes and methods, with everything being an object. Ruby uses a clear and concise syntax, where statements do not require semicolons at the end. Data types in Ruby include numbers (integers and floats), strings, symbols, arrays, hashes, and booleans. Ruby’s dynamic typing allows variables to change types easily, enhancing flexibility. Comments can be added using # for single-line comments and =begin and =end for multi-line comments.",
            course_id = 5
        )
        Lesson.objects.create(
            id = 26,
            title = "Control Structures and Loops",
            info = "Ruby provides various control structures to manage the flow of execution. Conditional statements like if, unless, elsif, and case enable branching logic based on conditions. Ruby supports several types of loops, including while, until, and for loops, as well as iterators like .each, which simplify iteration over collections. The break and next keywords allow for exiting loops or skipping to the next iteration, respectively. Ruby's flexible syntax makes it easy to implement complex control flow in a readable manner.",
            course_id = 5
        )
        Lesson.objects.create(
            id = 27,
            title = "Working with Arrays, Hashes, and Strings",
            info = "Arrays and hashes are fundamental data structures in Ruby. An array is an ordered collection of elements, allowing for easy storage and manipulation of lists. Methods like .push, .pop, .shift, and .map provide powerful tools for working with arrays. A hash is an unordered collection of key-value pairs, ideal for associating related data. Hashes can be created using {} and support various methods for manipulation. Ruby strings are mutable and come with numerous built-in methods for string manipulation, including concatenation, slicing, and formatting. String interpolation is a unique feature that allows for embedding variables directly within string literals.",
            course_id = 5
        )
        Lesson.objects.create(
            id = 28,
            title = "Object-Oriented Programming in Ruby",
            info = "Ruby is designed with object-oriented programming as a core principle. Classes are defined using the class keyword, and objects are instances of these classes. Ruby supports the four main OOP principles: encapsulation, inheritance, polymorphism, and abstraction. Encapsulation is achieved by using private and protected methods to restrict access to certain data. Inheritance allows a class to inherit methods and attributes from another class, facilitating code reuse. Polymorphism in Ruby enables objects to respond to the same method in different ways, while abstraction hides complex implementation details from the user.",
            course_id = 5
        )
        Lesson.objects.create(
            id = 29,
            title = "Metaprogramming and Ruby Gems",
            info = "One of Ruby’s standout features is its metaprogramming capabilities, allowing developers to write code that modifies or extends the behavior of classes and methods at runtime. This dynamic feature can be used to create domain-specific languages (DSLs) or to simplify repetitive code. Ruby Gems are packages of Ruby code that can be easily shared and reused across applications. The RubyGems package manager simplifies the process of installing, managing, and distributing these libraries, providing access to a vast ecosystem of pre-built functionality that enhances development productivity.",
            course_id = 5
        )
        Lesson.objects.create(
            id = 30,
            title = "Web Development with Ruby on Rails",
            info = "Ruby on Rails (often referred to as Rails) is a powerful web application framework written in Ruby that follows the MVC (Model-View-Controller) architectural pattern. Rails promotes convention over configuration, allowing developers to create database-backed web applications quickly and efficiently. Key features of Rails include an integrated ORM called ActiveRecord for database interactions, built-in testing frameworks, and a strong emphasis on RESTful architecture. Rails also provides scaffolding capabilities, enabling rapid prototyping and development of web applications, making it a popular choice for startups and web developers.",
            course_id = 5
        )
        # PHP
        Lesson.objects.create(
            id = 31,
            title = "PHP Basics: Syntax, Variables, and Operators",
            info = "PHP (Hypertext Preprocessor) is a widely-used server-side scripting language designed for web development. PHP code is embedded within HTML using <?php ... ?> tags, allowing dynamic content generation. The syntax is similar to C and Java, making it accessible to those familiar with these languages. Variables in PHP are declared using the $ sign, and they are dynamically typed, meaning their types can change at runtime. Common data types include strings, integers, floats, booleans, arrays, and objects. PHP supports a wide range of operators, including arithmetic (+, -, *, /), comparison (==, ===, !=, >), and logical operators (&&, ||, !), facilitating various operations in scripts.",
            course_id = 6
        )
        Lesson.objects.create(
            id = 32,
            title = "Control Structures and Functions in PHP",
            info = "PHP provides control structures such as conditional statements (if, else, elseif, switch) that allow developers to execute code based on specific conditions. Looping structures, including for, while, and foreach, enable iteration over arrays or other iterable data types. Functions in PHP are defined using the function keyword and can take parameters and return values. PHP also supports variable-length argument lists, allowing functions to accept any number of arguments. Built-in functions cover a wide range of tasks, from string manipulation to array handling and file operations, promoting code reuse and modularity.",
            course_id = 6
        )
        Lesson.objects.create(
            id = 33,
            title = "Working with Forms and User Input",
            info = "PHP is commonly used for handling form submissions and user input in web applications. Forms are created using HTML, and when submitted, the data can be accessed in PHP via the $_GET, $_POST, or $_REQUEST superglobals, depending on the method used. Input validation and sanitization are crucial for security and data integrity, often performed using built-in functions like filter_var() and htmlspecialchars(). PHP also provides support for file uploads through forms, enabling users to submit files to the server for processing.",
            course_id = 6
        )
        Lesson.objects.create(
            id = 34,
            title = "Database Interaction with MySQL and PDO",
            info = "PHP excels in database interaction, particularly with MySQL, which is a popular relational database management system. Developers can use the MySQLi extension or PDO (PHP Data Objects) for database connections and queries. PDO offers a consistent interface for accessing various database types and provides prepared statements, enhancing security against SQL injection attacks. Basic operations such as connecting to the database, executing queries, fetching results, and managing transactions are essential skills for building data-driven applications in PHP.",
            course_id = 6
        )
        Lesson.objects.create(
            id = 35,
            title = "Building Secure and Scalable Web Applications",
            info = "Security is a critical concern in PHP web applications. Best practices include using prepared statements to prevent SQL injection, validating and sanitizing user input, managing sessions securely, and protecting against cross-site scripting (XSS) and cross-site request forgery (CSRF) attacks. PHP’s built-in session management allows developers to maintain user state across requests. For scalability, leveraging caching mechanisms, optimizing database queries, and using load balancers can significantly enhance application performance and user experience.",
            course_id = 6
        )
        Lesson.objects.create(
            id = 36,
            title = "Introduction to PHP Frameworks: Laravel and Symfony",
            info = "PHP frameworks such as Laravel and Symfony provide powerful tools for building robust web applications. Laravel is known for its elegant syntax, built-in tools for routing, authentication, and session management, and its ORM called Eloquent for database interactions. Laravel follows the MVC (Model-View-Controller) architectural pattern, promoting clean code organization. Symfony, on the other hand, is a highly flexible framework that emphasizes reusable components and best practices, making it suitable for large-scale applications. Both frameworks offer extensive documentation, community support, and a wide array of packages and libraries to extend functionality, significantly accelerating development processes.",
            course_id = 6
        )