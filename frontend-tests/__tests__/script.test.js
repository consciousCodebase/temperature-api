/* Temperature Conversion API Frontend Test Suite */

const { convertCtoF, convertFtoC } = require("../../static/scripts/script");

/* Testing convertCtoF                            */
describe("Celsius to Fahrenheit UI", () => {
    beforeEach(() => {
        document.body.innerHTML = `
            <input id="celsiusInput" />
            <div id="celsiusResult"></div>
            <div id="celsiusLoading" hidden></div>
            <button id="celsiusBtn"></button>
        `;

        fetch.mockClear();
    });

    /* Test convertCtoF Valid Input */
    test("displays converted temperature on success", async () => {
        fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => ({
                celsius: 0,
                fahrenheit: 32
            })
        });

    document.getElementById("celsiusInput").value = "0";

    await convertCtoF();

    expect(
        document.getElementById("celsiusResult").innerText
    ).toBe("0°C = 32°F");
    });

    /* Test convertCtoF Error Case */
    test("shows error message on convertCtoF API failure", async() => {
    fetch.mockResolvedValueOnce({
        ok: false,
        json: async() => ({
            detail: "Value must be a finite number"
        })
    });

    document.getElementById("celsiusInput").value = "NaN";

    await convertCtoF();

    expect(
        document.getElementById("celsiusResult").innerText
    ).toContain("Error");
    });
});

/* Testing convertFtoC                              */

describe("Fahreinheit to Celsius UI", () => {
    beforeEach(() => {
        document.body.innerHTML = `
            <input id="fahrenheitInput" />
            <div id="fahrenheitResult"></div>
            <div id="fahrenheitLoading"></div>
            <button id="fahrenheitBtn"></button>
        `;
            
    fetch.mockClear();
    });

    /* Test convertFtoC Valid Input */
    test("displays converted temperature on success", async () => {
        fetch.mockResolvedValueOnce({
            ok: true,
            json: async() => ({
                fahrenheit: 212,
                celsius: 100
            })
        })

        document.getElementById("fahrenheitInput").value = "32";

        await convertFtoC();

        expect(
        document.getElementById("fahrenheitResult").innerText
        ).toBe("212°F = 100°C");
    });

    /* Test convertFtoC Error Case */
    test("shows error message on convertFtoC API failure", async () => {
        fetch.mockResolvedValueOnce({
            ok: false,
            json: async () => ({
                detail: "Value must be a finite number"
            })
        });

        document.getElementById("fahrenheitInput").value = "NaN";

        await convertFtoC();

        expect(
            document.getElementById("fahrenheitResult").innerText
        ).toContain("Error");
    })
});