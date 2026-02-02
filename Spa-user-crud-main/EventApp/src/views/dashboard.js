

export function dashboardView() {
    return `
    <div class="dashboard-container">
        <header class="dashboard-header">
            <h2>📊 Dashboard de Control</h2>
            <div class="metrics-grid">
                <div class="metric-card">
                    <h4>Total Eventos</h4>
                    <p id="stat-total-events">0</p>
                </div>
                <div class="metric-card">
                    <h4>Total Registros</h4>
                    <p id="stat-total-regs">0</p>
                </div>
                <div class="metric-card">
                    <h4>Cupos Globales</h4>
                    <p id="stat-global-capacity">0</p>
                </div>
            </div>
        </header>

        <section class="dashboard-details">
            <h3>Asistencia Detallada por Evento</h3>
            <div id="dashboard-list">
                </div>
        </section>
    </div>
    `;
}