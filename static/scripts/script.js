/*
--------------------------
Project:
Temperature Conversion API
using Python APIs

Joy Williams Morales
Date: 14 December 2025

Filename: scripts.js
-----------------------------
*/

async function convertCtoF() {
    const value = document.getElementById("celsiusInput").value;
    const resultDiv = document.getElementById("celsiusResult");

    resultDiv.innerText = "";

    if (value === "") {
        resultDiv.innerText = "Please enter a Celsius value.";
        return;
    }

    try {
        const response = await fetch(`/celsius-to-fahrenheit?value=${value}`);
        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = `Error: ${data.detail}`;
            return;
        }

        resultDiv.innerText = `${data.celsius}°C = ${data.fahrenheit}°F`;

    } catch (error) {
        resultDiv.innerText = "Unexpected error occurred.";
    }
}

async function convertFtoC() {
    const value = document.getElementById("fahrenheitInput").value;
    const resultDiv = document.getElementById("fahrenheitResult");

    resultDiv.innerText = "";

    if (value === "") {
        resultDiv.innerText = "Please enter a Fahrenheit value";
        return;
    }

    try {
        const response = await fetch(`/fahrenheit-to-celsius?value=${value}`);
        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = `Error: ${data.detail}`;
            return;
        }

        resultDiv.innerText = `${data.fahrenheit}°F = ${data.celsius}°C`;
    } catch (error) {
        resultDiv.innerText = "Unexpected Error Occurred";
    }
}