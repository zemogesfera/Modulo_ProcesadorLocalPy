document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const resultadoDiv = document.getElementById("resultado");
    const descargarBtn = document.getElementById("descargar-btn");
    const spinner = document.getElementById("spinner");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevenir el comportamiento por defecto del formulario
        
        // Mostrar el spinner y ocultar resultados previos
        spinner.style.display = "block";
        resultadoDiv.textContent = "";
        descargarBtn.style.display = "none";

        const formData = new FormData(form);
        
        fetch("/procesar", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Ocultar el spinner
            spinner.style.display = "none";

            if (data.error) {
                resultadoDiv.textContent = data.error;
                descargarBtn.style.display = "none";
            } else {
                // Mostrar el resultado en el <pre>
                resultadoDiv.textContent = JSON.stringify(data.resultado, null, 4);
                
                // Mostrar el botón de descargar y agregarle el enlace al archivo JSON
                descargarBtn.style.display = "block";
                descargarBtn.onclick = function() {
                    window.location.href = `/descargar?ruta=${formData.get('ruta')}`;
                };
            }
        })
        .catch(error => {
            // Ocultar el spinner en caso de error
            spinner.style.display = "none";
            console.error("Error al procesar:", error);
            resultadoDiv.textContent = "Error al procesar la solicitud.";
        });
    });
});