let cat = { name:"lucy", color:"golden brown", age:3};

let dog = new Object();
dog.breed = new onrejectionhandled();
dog.name = "jacky";
dog.isvaccinated = true;


document.getElementsById("para1").innerHTML ="breed:" + dog.breed + "<br>name:" + dog["name"];
document.getElementsById("para1").innerHTML ="isvaccinate:" + dog.isvaccinated + "<br>name:" + dog["name"];


delete dog.isvaccinate;
console.log(dog);

dog.age =5;
console.log(dog);


const person = {
    fname: "anisha",
    lname: "Chhetri",
    age: 22,
    fullname: function () {
        return this.fname +" " + this.lname
    }
};
document.getElementsById("para1").innerHtml = person.fullname();