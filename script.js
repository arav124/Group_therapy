async function submitForm() {

    let en = [
        parseInt(document.getElementById("en1").value)
    ];

    let ia_an = [
        parseInt(document.getElementById("ia_an1").value)
    ];

    let ia_av = [
        parseInt(document.getElementById("ia_av1").value)
    ];

    let psy = [
        parseInt(document.getElementById("psy1").value)
    ];

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            en: en,
            ia_an: ia_an,
            ia_av: ia_av,
            psy: psy
        })
    });

    let data = await response.json();

    // Store result
    localStorage.setItem("result", JSON.stringify(data));

    window.location.href = "result.html";
}
