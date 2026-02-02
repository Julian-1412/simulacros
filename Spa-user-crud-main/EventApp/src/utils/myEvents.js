import { getRegist } from '../services/regist.js';

export async function myRegistrationsLogic() {
    // 1. Capturar el contenedor donde se mostrarán los datos
    const container = document.getElementById("my-events-list");
    const userData = JSON.parse(localStorage.getItem("userData"));

    // Verificación de seguridad para evitar errores de "null"
    if (!container) return;

    const render = async () => {
        // 2. Obtener todos los registros desde el servicio
        const allRegs = await getRegist();
        
        // 3. Filtrar para mostrar solo los eventos del usuario logueado
        const myRegs = allRegs.filter(reg => reg.userId === userData.userEmail);

        // 4. Si no tiene registros, mostrar mensaje amigable
        if (myRegs.length === 0) {
            container.innerHTML = `
                <div class="no-data">
                    <p>Aún no te has inscrito a ningún evento.</p>
                </div>`;
            return;
        }

        // 5. Renderizar las tarjetas (Sin botón de cancelar)
        container.innerHTML = myRegs.map(reg => `
            <div class="registration-card">
                <div class="reg-info">
                    <h4>✅ ${reg.eventTitle}</h4>
                    <p><strong>Inscrito el:</strong> ${reg.date}</p>
                </div>
            </div>
        `).join("");
    };

    // Ejecutar la función de carga
    render();
}