async function convertCtoF() {
    const value = document.getElementById("celsiusInput").value;
    const response = await fetch(`/celsius-to-fahrenheit?value=${value}`);
    const data = await response.json();
    document.getElementById("celsiusResult").innerText = 
        `${data.celsius}°C = ${data.fahrenheit}°F`;
}

async function convertFtoC() {
    const value = document.getElementById("fahrenheitInput").value;
    const response = await fetch(`/fahrenheit-to-celsius?value=${value}`);
    const data = await response.json();
    document.getElementById("fahrenheitResult").innerText = 
        `${data.fahrenheit}°F = ${data.celsius}°C`;
}