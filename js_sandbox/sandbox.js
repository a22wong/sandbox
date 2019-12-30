let shortid = require('shortid')

console.log(shortid.generate())

// var jwt = require('jsonwebtoken');
// var token = jwt.sign({ name: 'name', password: 'password'}, 'secretKey', { expiresIn: '365 days'});
// console.log(token)


// const users = [
//   {
//     name: 'admin',
//     password: 'admin1',
//   },
//   {
//     name: 'dev',
//     password: 'dev1',
//   },
//   {
//     name: 'app',
//     password: 'app1',
//   },
// ]


// const validate = function (decoded, request) {
//   let user = users.filter(user => user.name === decoded.name)

//   if(user.length == 0) {
//     console.log('invalid username:', decoded.name)
//     return { isValid: false};
//   }

//   let authUser = user.filter(user => user.password === decoded.password)

//   if(authUser.length == 0) {
//     console.log('invalid password for username:', decoded.name)
//     return { isValid: false};
//   }
//   return {isValid: true}
// }

// var decoded = { name: "app", password: "app1" }
// var validity = validate(decoded, null)
// console.log(validity)





// const moment = require('moment')
// console.log(moment().format())
// // var now = new Date().toLocaleString("en-US", {timeZone: "Asia/Singapore"});
// var then = moment.utc('2019-05-05T16:20:00+08:00')
// console.log(`then: ${then}`)
// var now = moment.utc()
// console.log(`now: ${now}`)
// console.log((now-then)/1000)

// console.log('hello world')
// const admin = require('firebase-admin');
// const functions = require('firebase-functions');
// admin.initializeApp({
//     credential: admin.credential.cert(serviceAccount)
// });
// var db = admin.firestore()
// var people = db.collection('people')
// var person = people.doc('alex').get()
// .then(doc => {
//     if (!doc.exists) {
//         console.log('No such document!');
//     } else {
//         console.log('Document data:', doc.data().phone_number);
//     }
//     return
// })
// .catch(err => {
//     console.log('Error getting document', err);
// });

// console.log(recommended_worker)

// var asiaTime = new Date().toLocaleString("en-US", {timeZone: "Asia/Singapore"});
// asiaTime = new Date(asiaTime);
// asiaTime = asiaTime.toISOString()
// var currTime;
// currTime = asiaTime.slice(0, -5)
// console.log(currTime)

// const request = require("request");

// let get_dad_joke = async function() {
//   var options = { method: 'GET',
//     url: 'http://icanhazdadjoke.com',
//     headers: 
//      {'cache-control': 'no-cache',
//        Accept: 'application/json' } };

//   request(options, function (error, response, body) {
//     if (error) throw new Error(error);

//     console.log(body)
//     return body
//   });
// };

// var joke = await get_dad_joke()
// console.log(joke)

// var date = new Date();
// var hour = date.getHours()
// if (hour > 12) {
//     hour = hour - 12
// }
// var min = date.getMinutes()
// var now = hour + ' ' + min
// if (Math.random() < 0.9) {
//     console.log(`It is ${now}.`);
// } else {
//     console.log(`It's time for you to get a watch.`);
// }