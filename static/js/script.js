async function enviarCafe(cafe = null) {
    if (!cafe) {
        const input = document.getElementById("cafeInput");
        cafe = input.value.trim();
        if (cafe === "") {
            alert("Escribe tu nombre porfavor");
            return;
        }
        input.value = ""; 
    }
  }
async function enviarCafe(cafe) {
    try {
        const response = await fetch("/api/cafe", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({cafe: cafe})
        });
        const data = await response.json();
        window.location.href = "/otra";
    } catch (error) {
        console.error("Error al enviar café:", error);
      }
}