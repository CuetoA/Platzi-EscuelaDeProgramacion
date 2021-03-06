// OPTIONAL PARAMETERS
// -es6
function newFunction (name, age, country){
    var name = name || 'oscar';
    var age = age || 32;
    var country = country || 'MX';
    console.log(name, age, country);
}

// +es6
function newFunction2(name = "oscar", age = 23, country = "Mx"){
    console.log(name, age, country);
}

newFunction2();
newFunction2("Andrés", 23);


// SPLIT IN STRINGS
// -es6
let lorem = "I just want to split this thing \n" 
+ "another phrase";
// +es6
let lorem2 = `Another phrase we need 
another phrase`

console.log(lorem);
console.log(lorem2);


// VARIABLES IN OBJECTS
// -es6
let person = {
    'name': 'Andrés',
    'age': 32,
    'country': 'Mexico'
}
console.log(person.name, person.age)
// +es6
let {name, country} = person;
console.log(name, country);


// JOIN ARRAYS
// +es6
let team1 = ['Scarlette', 'Andrés'];
let team2 = ['Ceres', 'Boni'];
let new_team = ['Pablo', ...team1, ...team2]
console.log(new_team);


// LET AND VAR
// +es6
{
    var globalVar = "Global variable";
}
{
    let globalLet = "Global Let"    // just inside scope
}
console.log(globalVar);     // avialable
console.log(globalLet);     // not avialable


// CONSTANT
// +es6
const a = 'b'; // it cannot chenge from ecmascript6


// CREATE OBJECTS WITH VARIABLES
// -es6
let name = "andres";
let age = 23;
obj = {name: name, age: age};
// +es6
obj2 = {name, age};
console.log(obj);
console.log(obj2);


// ARROW FUNCTIONS
// -es6
let names = [
    {name: "Scarlette", age: 25},
    {name: "Andrés", age: 23}
]
let list_names = names.map( function(item){
    console.log(item.name);
})
// +es6
let list_names2 = names.map(item => console.log(item.name));
const arrow_f = (element1, element2) => {console.log(`${element1}  ${element2}`)}
const arrow_f2 = element => console.log(`${element}`)

arrow_f("Boni bb", 14);
arrow_f2('Print this');

// ARROW FUNCTIONS
// +es6
const helloPromise = () =>{
    return new Promise((resolve, reject)=>{
        if(false){
            resolve('Hey!');
        }else{
            reject('Ups!');
        }
    })
}

helloPromise()
    .then(response => console.log(response))
    .then(() => console.log('void'))
    .catch(error => console.log(error));


// OOP
// +es6
class calculator {
    constructor(){
        this.valueA = 0;
        this.valueB = 0;
    }

    sum(valueA, valueA){
        this.valueA = valueA;
        this.valueB = valueB;
        return this.valueA + this.valueB
    }
}

const calc = new calculator();
console.log(calc.sum(2,2));


// MODULES
// -es6
const module= require('./module')
console.log(module.hello());
console.log(module.bye());
// +es6
import {hello} from './module';
module();

// GENERATORS
// +es6
function* helloWorld(){
    if(true){
        yield "Hello "
    }
    if (true){
        yield "world"
    }
}

const generatorHello = helloWorld();
console.log(generatorHello.next().value);
console.log(generatorHello.next().value);
console.log(generatorHello.next().value);


// -es6

// +es6


// -es6

// +es6