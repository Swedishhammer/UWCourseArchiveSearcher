//This program is in javascript as eventually it will be integrated into a website using js
//This program is written to be used separate from webpage and local
//  and is just to help develop and test search logic
console.log("This is a js program");
const jsonFilePath = '/CourseDataTest.json';

fetch(jsonFilePath)
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP error! Status: ${response.status}');
        }
        return response.json();
    })
    .then(data => {
        console.log("Parsed JSON data successfully");
        console.log("Data: " + JSON.stringify(data, null, 2));
    })
    .catch(error => {
        console.error("Error loading JSON: ", error);
    })