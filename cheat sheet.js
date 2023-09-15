//*1. Variables and Data Types
// Declare variables using var, let, or const
let name = "John";
const age = 30;
var job = "developer";
// Data types: string, number, boolean, null, undefined, object, symbol

//*2. Functions
// Define a function
function greet(name) {
    console.log(`Hello, ${name}!`);
}

// Call a function
greet("Alice");

//*3. Consitional Statements 
if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}

//*4. Arrays
const fruits = ["apple", "banana", "orange"];
console.log(fruits[0]); // Output: apple
fruits.push("grape");   // Add an element

//*5. Objects
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
};

console.log(person.firstName); // Output: John

//*6. Loops
for (let i = 0; i < 5; i++) {
    console.log(i);
}

fruits.forEach(fruit => {
    console.log(fruit);
});

//*7. Arrow Functions
const add = (a, b) => a + b;
console.log(add(3, 5)); // Output: 8

//*8. Classes and Objects(ES6)
class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }
}

const myCar = new Car("Toyota", "Corolla");

//*9. Promises (Async Programming)
const fetchData = () => {
    return new Promise((resolve, reject) => {
        // Fetch data from an API
        if (dataReceived) {
            resolve(data);
        } else {
            reject("Data not available.");
        }
    });
};

fetchData()
    .then(data => console.log(data))
    .catch(error => console.log(error));


//*10. ES6 Modules (Module System)
// In a separate file (e.g., utils.js)
export const add = (a, b) => a + b;

// In another file
import { add } from './utils';
console.log(add(2, 3)); // Output: 5

// *Class declaration
class ClassName {
    constructor(/* constructor parameters */) {
        // constructor code
    }

    method1(/* parameters */) {
        // method code
    }

    method2(/* parameters */) {
        // method code
    }

    // ... more methods
}

//* Constructor
class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

const person = new Person("John", "Doe");
console.log(person.firstName); // Output: John

//* Methods
class Circle {
    constructor(radius) {
        this.radius = radius;
    }

    calculateArea() {
        return Math.PI * this.radius ** 2;
    }
}

const circle = new Circle(5);
console.log(circle.calculateArea()); // Output: 78.53981633974483

//* Inheritance
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}

const dog = new Dog("Buddy");
dog.speak(); // Output: Buddy barks.

//*Getters and Setters
class Temperature {
    constructor(celsius) {
        this.celsius = celsius;
    }

    get fahrenheit() {
        return this.celsius * 9/5 + 32;
    }

    set fahrenheit(value) {
        this.celsius = (value - 32) * 5/9;
    }
}

const temp = new Temperature(25);
console.log(temp.fahrenheit); // Output: 77
temp.fahrenheit = 68;
console.log(temp.celsius);    // Output: 20

//* Static Methods
class MathOperations {
    static square(x) {
        return x * x;
    }
}

console.log(MathOperations.square(4)); // Output: 16

