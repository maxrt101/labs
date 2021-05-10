# IoT labs
## Lab 9
### Task
The task is to create REST service using java language and JAX-RS library.

 - Create REST service and implement CRUD operations on object from 8-th lab.
 - GET operation should use id
 - GET operation without id should return list of all objects
 - To implement REST service base class from 8-th lab should be expanded with `id` field of type `int`
 - Code should be checked with findbugs, checkstyle and pmd plugins
 - Code should be in a different pull request than lab8
 - Controller and RestApplication should be in a different packages
 - Objects should be stored in a `Map`

### To run:
 - Clone/download lab8 branch
 - `cd` into repo folder
 - Run `mvn install`
 - Run `java -jar target/lab9-VERSION.jar`