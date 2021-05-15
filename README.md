# IoT labs
## Lab 10
### Task
Implement saving of one of the classes from 8-th lab in a table in a database using `spring.boot` and `spring.data`
 - 9-th lab code should be changed in such way, that permits saving/reading data to/from database
 - Code should comply with code convention
 - Code should be checked with findbugs, pmd and checkstyle plugins
 - A separate pull request should be created
 - Code must contain separate `*Controller`, `*Service` and `*Repository` classes
 - Configuration of database accessing should be done through properties file

### To run:
 - Clone/download lab10 branch
 - `cd` into repo folder
 - Run `mvn install`
 - Run `java -jar target/lab10-VERSION.jar`, where `VERSION` is version of the app  
   (can be found in `pom.xml`, under `<version>` tag)