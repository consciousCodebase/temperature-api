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
    const loading = document.getElementById("celsiusLoading");
    const button = document.getElementById("celsiusBtn");

    resultDiv.innerText = "";
    loading.hidden = false;
    button.disabled = true;

    try {
        if (value === "") {
        resultDiv.innerText = "Please enter a Celsius value.";
        return;
        }  
        
        const response = await fetch(`/celsius-to-fahrenheit?value=${value}`);
        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = `Error: ${data.detail}`;
            return;
        }

        resultDiv.innerText = `${data.celsius}°C = ${data.fahrenheit}°F`;

    } catch (error) {
        resultDiv.innerText = "Unexpected error occurred.";
    } finally {
        loading.hidden = true;
        button.disabled = false;
    }
}

async function convertFtoC() {
    const value = document.getElementById("fahrenheitInput").value;
    const resultDiv = document.getElementById("fahrenheitResult");
    const loading = document.getElementById("fahrenheitLoading");
    const button = document.getElementById("fahrenheitBtn");

    resultDiv.innerText = "";
    loading.hidden = false;
    button.disabled = true;

    try {
        if (value === "") {
        resultDiv.innerText = "Please enter a Fahrenheit value";
        return;
    }

        const response = await fetch(`/fahrenheit-to-celsius?value=${value}`);
        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = `Error: ${data.detail}`;
            return;
        }

        resultDiv.innerText = `${data.fahrenheit}°F = ${data.celsius}°C`;
    } catch (error) {
        resultDiv.innerText = "Unexpected Error Occurred";
    } finally {
        loading.hidden = true;
        button.disabled = false;
    }
}