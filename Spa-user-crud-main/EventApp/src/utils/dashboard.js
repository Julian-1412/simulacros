import {getEvents} from '../services/events.js';
import {getRegist} from '../services/regist.js'

export async function adminDashboardLogic() {
    const dashboardList = document.getElementById("dashboard-list");
    
    try {
        const [events, regs] = await Promise.all([getEvents(), getRegist()]);

        // Métricas rápidas
        const totalCap = events.reduce((acc, e) => acc + (parseInt(e.capacity) || 0), 0);
        document.getElementById("stat-total-events").textContent = events.length;
        document.getElementById("stat-total-regs").textContent = regs.length;
        document.getElementById("stat-global-capacity").textContent = totalCap;

        dashboardList.innerHTML = events.map(event => {
            const eventRegs = regs.filter(r => r.eventId === event.id);
            const percent = ((eventRegs.length / event.capacity) * 100).toFixed(1);

            return `
            <div class="dashboard-card">
                <div class="card-header">
                    <h4>${event.title}</h4>
                    <span class="badge">${percent}% Lleno</span>
                </div>
                <progress value="${eventRegs.length}" max="${event.capacity}"></progress>
                <div class="attendees">
                    <strong>Asistentes (${eventRegs.length}):</strong>
                    <ul>
                        ${eventRegs.map(r => `<li>${r.userId}</li>`).join('') || '<li>Sin registros</li>'}
                    </ul>
                </div>
            </div>`;
        }).join("");

    } catch (err) {
        dashboardList.innerHTML = "<p>Error cargando datos del dashboard.</p>";
    }
}